# EduGuide AI - Teacher Interventions Page
import streamlit as st
import pandas as pd
from interventions import predict_student

def show():
    st.title("👨‍🏫 Teacher Interventions")
    st.markdown("### Class-wide intervention recommendations")
    st.markdown("---")

    df = pd.read_csv('data/student-mat.csv', sep=',')
    df['higher'] = (df['higher'] == 'yes').astype(int)
    df['famsup'] = (df['famsup'] == 'yes').astype(int)
    df['schoolsup'] = (df['schoolsup'] == 'yes').astype(int)
    df['at_risk'] = (df['G3'] < 10).astype(int)

    at_risk_df = df[df['at_risk'] == 1].reset_index()

    st.info(f"⚠️ {len(at_risk_df)} students currently require intervention")

    for i, row in at_risk_df.iterrows():
        student = {
            'G1': row['G1'], 'G2': row['G2'],
            'failures': row['failures'],
            'absences': row['absences'],
            'studytime': row['studytime'],
            'higher': row['higher'],
            'famsup': row['famsup'],
            'schoolsup': row['schoolsup']
        }
        result = predict_student(student)

        with st.expander(f"Student #{row['index']} — {result['risk_level']} — {result['probability']}% risk"):
            st.markdown("**Recommended Interventions:**")
            for intervention in result['interventions']:
                st.markdown(f"- {intervention}")

        if i >= 9:
            st.markdown("*Showing top 10 at-risk students. Full list available on export.*")
            break