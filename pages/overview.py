# EduGuide AI - Overview Page
import streamlit as st
import pandas as pd
import plotly.express as px
from interventions import predict_student

def show():
    st.title("🏠 School Overview")
    st.markdown("### Mukuru Primary School — Term 1, 2026")
    st.markdown("---")

    # Load data
    df = pd.read_csv('data/student-mat.csv', sep=',')

    # Create at-risk labels
    df['at_risk'] = (df['G3'] < 10).astype(int)
    df['higher'] = (df['higher'] == 'yes').astype(int)
    df['famsup'] = (df['famsup'] == 'yes').astype(int)
    df['schoolsup'] = (df['schoolsup'] == 'yes').astype(int)

    # ── Top Metric Cards ───────────────────────────────
    total = len(df)
    at_risk = df['at_risk'].sum()
    safe = total - at_risk
    rate = round((at_risk / total) * 100, 1)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", total)
    col2.metric("At Risk", at_risk, delta=f"{rate}%", delta_color="inverse")
    col3.metric("On Track", safe)
    col4.metric("Risk Rate", f"{rate}%")

    st.markdown("---")

    # ── Risk Distribution Chart ────────────────────────
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Risk Distribution")
        risk_counts = df['at_risk'].value_counts().reset_index()
        risk_counts.columns = ['Status', 'Count']
        risk_counts['Status'] = risk_counts['Status'].map(
            {0: 'On Track', 1: 'At Risk'}
        )
        fig = px.pie(
            risk_counts, values='Count', names='Status',
            color='Status',
            color_discrete_map={'On Track': '#2ecc71', 'At Risk': '#e74c3c'}
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Grade Distribution")
        fig2 = px.histogram(
            df, x='G3', nbins=20,
            color_discrete_sequence=['#2E5496'],
            labels={'G3': 'Final Grade (out of 20)'}
        )
        fig2.add_vline(x=10, line_dash="dash",
                       line_color="red",
                       annotation_text="Pass Mark")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ── At Risk Students Table ─────────────────────────
    st.subheader("⚠️ Students Requiring Attention")
    at_risk_df = df[df['at_risk'] == 1][
        ['G1', 'G2', 'G3', 'absences', 'failures', 'studytime']
    ].reset_index()
    at_risk_df.columns = [
        'ID', 'Term 1', 'Term 2', 'Final Grade',
        'Absences', 'Past Failures', 'Study Time'
    ]
    st.dataframe(at_risk_df, use_container_width=True)
