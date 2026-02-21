# EduGuide AI - Student Risk Tracker
import streamlit as st
from interventions import predict_student

def show():
    st.title("🔍 Student Risk Tracker")
    st.markdown("### Enter a student's details to predict their risk level")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Student Details")
        name = st.text_input("Student Name", placeholder="e.g. John Kamau")
        g1 = st.slider("Term 1 Grade (G1)", 0, 20, 10)
        g2 = st.slider("Term 2 Grade (G2)", 0, 20, 10)
        absences = st.slider("Number of Absences", 0, 75, 5)

    with col2:
        st.subheader("Background")
        failures = st.selectbox("Past Failures", [0, 1, 2, 3])
        studytime = st.selectbox(
            "Weekly Study Time",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "Less than 2 hours",
                2: "2 to 5 hours",
                3: "5 to 10 hours",
                4: "More than 10 hours"
            }[x]
        )
        higher = st.radio(
            "Wants to pursue higher education?",
            ["Yes", "No"]
        )
        famsup = st.radio("Family support at home?", ["Yes", "No"])
        schoolsup = st.radio("Receiving school support?", ["Yes", "No"])

    st.markdown("---")

    if st.button("🔍 Predict Risk Level", use_container_width=True):
        student = {
            'G1': g1,
            'G2': g2,
            'failures': failures,
            'absences': absences,
            'studytime': studytime,
            'higher': 1 if higher == "Yes" else 0,
            'famsup': 1 if famsup == "Yes" else 0,
            'schoolsup': 1 if schoolsup == "Yes" else 0,
        }

        result = predict_student(student)

        # ── Result Display ─────────────────────────────
        st.markdown("---")
        st.subheader(f"Results for {name if name else 'Student'}")

        # Risk level badge
        if "High" in result['risk_level']:
            st.error(f"## {result['risk_level']}")
            st.error(f"**{result['probability']}% probability of failing**")
        elif "At Risk" in result['risk_level']:
            st.warning(f"## {result['risk_level']}")
            st.warning(f"**{result['probability']}% probability of failing**")
        else:
            st.success(f"## {result['risk_level']}")
            st.success(f"**{result['probability']}% probability of failing**")

        # Interventions
        st.markdown("### 📋 Recommended Teacher Interventions")
        for intervention in result['interventions']:
            st.markdown(f"- {intervention}")