# EduGuide AI - Step 2: Build the Prediction Model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ── Load data ──────────────────────────────────────────
df = pd.read_csv('data/student-mat.csv', sep=',')

# ── Create the at-risk label ────────────────────────────
# G3 is the final grade out of 20. Below 10 = at risk
df['at_risk'] = (df['G3'] < 10).astype(int)
print("At-risk students:", df['at_risk'].sum())
print("Not at-risk students:", (df['at_risk'] == 0).sum())

# ── Select our features ─────────────────────────────────
# Only humane, relevant columns - no parental education
features = ['G1', 'G2', 'failures', 'absences',
            'studytime', 'higher', 'famsup', 'schoolsup']

# ── Convert yes/no columns to 1/0 ──────────────────────
df['higher']    = (df['higher'] == 'yes').astype(int)
df['famsup']    = (df['famsup'] == 'yes').astype(int)
df['schoolsup'] = (df['schoolsup'] == 'yes').astype(int)

# ── Split into input (X) and target (y) ─────────────────
X = df[features]
y = df['at_risk']

# ── Split into training and testing sets ────────────────
# 80% to train the model, 20% to test how well it learned
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Train the model ─────────────────────────────────────
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ── Test the model ──────────────────────────────────────
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.1f}%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred,
      target_names=['Not At Risk', 'At Risk']))

# ── Save the model for use in the dashboard ─────────────
joblib.dump(model, 'models/eduguide_model.pkl')
print("\nModel saved successfully!")
