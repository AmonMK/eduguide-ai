# EduGuide AI - Step 3: Intervention Recommender Engine
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('models/eduguide_model.pkl')

def get_risk_level(probability):
    """Convert a probability score to a risk level"""
    if probability >= 0.7:
        return "🔴 High Risk"
    elif probability >= 0.4:
        return "🟡 At Risk"
    else:
        return "🟢 Low Risk"

def get_interventions(student):
    """
    Look at why a student is struggling and recommend
    specific actions for the teacher
    """
    interventions = []

    # Low first term grade
    if student['G1'] < 10:
        interventions.append("📚 Enrol student in after-school academic support programme")

    # High absences
    if student['absences'] > 10:
        interventions.append("📞 Contact parent/guardian regarding frequent absences")

    # Past failures
    if student['failures'] > 0:
        interventions.append("👥 Assign peer tutoring — pair with a stronger student")

    # Low study time
    if student['studytime'] <= 1:
        interventions.append("📖 Discuss study habits with student — create a study plan")

    # No family support
    if student['famsup'] == 0:
        interventions.append("🏠 Schedule parent meeting to increase home involvement")

    # No school support already
    if student['schoolsup'] == 0:
        interventions.append("🏫 Refer student to school counsellor for additional support")

    # Does not want higher education
    if student['higher'] == 0:
        interventions.append("🎯 Have career guidance session — explore options beyond university")

    # If no specific triggers, give general advice
    if not interventions:
        interventions.append("👁️ Monitor student closely — check in weekly")

    return interventions

def predict_student(student_data):
    # Remove name before feeding to model
    features = {k: v for k, v in student_data.items() if k != 'name'}
    df = pd.DataFrame([features])
    # Get probability of being at risk
    prob = model.predict_proba(df)[0][1]
    risk_level = get_risk_level(prob)

    # Get interventions
    interventions = get_interventions(student_data)

    return {
        'risk_level': risk_level,
        'probability': round(prob * 100, 1),
        'interventions': interventions
    }

# ── Test it with 3 sample students ─────────────────────
if __name__ == "__main__":

    students = [
        {
            'name': 'Student A',
            'G1': 4, 'G2': 5, 'failures': 2,
            'absences': 20, 'studytime': 1,
            'higher': 0, 'famsup': 0, 'schoolsup': 0
        },
        {
            'name': 'Student B',
            'G1': 15, 'G2': 14, 'failures': 0,
            'absences': 2, 'studytime': 3,
            'higher': 1, 'famsup': 1, 'schoolsup': 0
        },
        {
            'name': 'Student C',
            'G1': 8, 'G2': 9, 'failures': 1,
            'absences': 8, 'studytime': 2,
            'higher': 1, 'famsup': 0, 'schoolsup': 1
        },
    ]

    for s in students:
        result = predict_student(s)
        print(f"\n{'='*40}")
        print(f"  {s['name']}")
        print(f"  Risk Level : {result['risk_level']}")
        print(f"  Probability: {result['probability']}% chance of failing")
        print(f"  Interventions:")
        for i in result['interventions']:
            print(f"    → {i}")
