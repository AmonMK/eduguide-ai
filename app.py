# EduGuide AI - Streamlit Dashboard
import streamlit as st

# ── Page Configuration ──────────────────────────────────
st.set_page_config(
    page_title="EduGuide AI",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True
)

# ── Sidebar Navigation ──────────────────────────────────
st.sidebar.image("https://img.icons8.com/color/96/graduation-cap.png")
st.sidebar.title("EduGuide AI")
st.sidebar.markdown("*Kenya's CBC Student Intelligence Platform*")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", [
    "🏠 Overview",
    "🔍 Student Risk Tracker",
    "👨‍🏫 Teacher Interventions",
    "👨‍👩‍👧 Parent Dashboard",
    "💼 Career Pathways"
])

# ── Load pages based on selection ──────────────────────
if page == "🏠 Overview":
    from pages import overview
    overview.show()

elif page == "🔍 Student Risk Tracker":
    from pages import risk_tracker
    risk_tracker.show()

elif page == "👨‍🏫 Teacher Interventions":
    from pages import interventions_page
    interventions_page.show()

elif page == "👨‍👩‍👧 Parent Dashboard":
    from pages import parent_dashboard
    parent_dashboard.show()

elif page == "💼 Career Pathways":
    from pages import career_pathways
    career_pathways.show()
