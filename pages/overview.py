# EduGuide AI - Overview Page
import streamlit as st
import pandas as pd
import plotly.express as px
from interventions import predict_student
import io

def load_data(file=None):
    """Load uploaded file or fall back to default dataset"""
    if file is not None:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file, sep=',')
        elif file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)
        else:
            st.error("Unsupported file type. Please upload CSV or Excel.")
            return None
    else:
        df = pd.read_csv('data/student-mat.csv', sep=',')

    # Standardise columns
    df['at_risk'] = (df['G3'] < 10).astype(int) if 'G3' in df.columns else 0
    df['higher'] = (df['higher'] == 'yes').astype(int) if 'higher' in df.columns else 0
    df['famsup'] = (df['famsup'] == 'yes').astype(int) if 'famsup' in df.columns else 0
    df['schoolsup'] = (df['schoolsup'] == 'yes').astype(int) if 'schoolsup' in df.columns else 0

    return df

def show():
    st.title("🏠 School Overview")
    st.markdown("### Mukuru Primary School — Term 1, 2026")
    st.markdown("---")

    # ── File Upload Section ────────────────────────────
    with st.expander("📂 Upload Student Data", expanded=False):
        st.markdown("Upload your school's student results file:")
        uploaded_file = st.file_uploader(
            "Drag and drop or browse",
            type=['csv', 'xlsx', 'xls'],
            help="Accepted formats: CSV, Excel (.xlsx, .xls)"
        )

        col1, col2 = st.columns(2)
        with col1:
            if uploaded_file:
                st.success(f"✅ {uploaded_file.name} uploaded successfully")
        with col2:
            if st.button("🔄 Clear — Use Demo Data"):
                uploaded_file = None
                st.session_state['uploaded_file'] = None
                st.rerun()

        st.markdown("**Expected format:**")
        sample = pd.DataFrame({
            'G1': [12, 4, 8],
            'G2': [11, 5, 9],
            'G3': [12, 4, 8],
            'failures': [0, 2, 1],
            'absences': [3, 20, 8],
            'studytime': [2, 1, 2],
            'higher': ['yes', 'no', 'yes'],
            'famsup': ['yes', 'no', 'no'],
            'schoolsup': ['no', 'no', 'yes']
        })
        st.dataframe(sample, use_container_width=True)

        # Download sample template
        csv = sample.to_csv(index=False)
        st.download_button(
            "⬇️ Download Sample Template",
            data=csv,
            file_name="eduguide_template.csv",
            mime="text/csv"
        )

    # ── Save upload state ──────────────────────────────
    if uploaded_file:
        st.session_state['uploaded_file'] = uploaded_file

    # ── Load data ──────────────────────────────────────
    file_to_load = st.session_state.get('uploaded_file', None)
    df = load_data(file_to_load)

    if df is None:
        st.error("Could not load data. Please check your file format.")
        return

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
        if 'G3' in df.columns:
            fig2 = px.histogram(
                df, x='G3', nbins=20,
                color_discrete_sequence=['#2E5496'],
                labels={'G3': 'Final Grade (out of 20)'}
            )
            fig2.add_vline(x=10, line_dash="dash",
                           line_color="red",
                           annotation_text="Pass Mark")
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("Upload a file with G3 column to see grade distribution")

    st.markdown("---")

    # ── At Risk Students Table ─────────────────────────
    st.subheader("⚠️ Students Requiring Attention")
    cols_to_show = [c for c in ['G1', 'G2', 'G3', 'absences',
                                 'failures', 'studytime'] if c in df.columns]
    at_risk_df = df[df['at_risk'] == 1][cols_to_show].reset_index()
    st.dataframe(at_risk_df, use_container_width=True)