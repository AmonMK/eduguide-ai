# EduGuide AI - Career Pathways Page
import streamlit as st


def show():
    st.title("💼 Career Pathways")
    st.markdown("### Kenyan Career & Opportunity Explorer")
    st.markdown("---")

    st.info("""
    🚧 **Full AI-powered career matching with live Kenyan job market 
    data is coming in the next version of EduGuide AI.**

    Below is a preview of the career pathway framework 
    we are building toward.
    """)

    st.markdown("---")
    st.subheader("🗺️ CBC Competency to Career Pathway Map")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("🔬 STEM Pathway", expanded=True):
            st.markdown("""
            **Strong in:** Mathematics, Sciences, Problem Solving

            **Career Options:**
            - Software Engineer
            - Medical Doctor
            - Civil Engineer  
            - Agricultural Scientist
            - Data Analyst

            **Kenyan Opportunity:** High demand in tech 
            hubs — Nairobi, Kisumu, Mombasa
            """)

        with st.expander("🎨 Arts & Creative Pathway"):
            st.markdown("""
            **Strong in:** Languages, Art, Communication

            **Career Options:**
            - Graphic Designer
            - Journalist / Media
            - Teacher / Educator
            - Architect
            - Content Creator

            **Kenyan Opportunity:** Growing creative 
            economy and digital media sector
            """)

        with st.expander("⚖️ Social Sciences Pathway"):
            st.markdown("""
            **Strong in:** History, CRE, Social Studies

            **Career Options:**
            - Lawyer / Advocate
            - Social Worker
            - Politician / Public Service
            - Counsellor
            - HR Professional

            **Kenyan Opportunity:** Public sector, 
            NGOs, and legal industry
            """)

    with col2:
        with st.expander("💼 Business & Entrepreneurship", expanded=True):
            st.markdown("""
            **Strong in:** Business Studies, Economics

            **Career Options:**
            - Entrepreneur / Business Owner
            - Accountant
            - Banker / Financial Analyst
            - Marketing Professional
            - Supply Chain Manager

            **Kenyan Opportunity:** SME sector is 
            Kenya's largest employer
            """)

        with st.expander("🌍 Agriculture & Environment"):
            st.markdown("""
            **Strong in:** Agriculture, Biology, Geography

            **Career Options:**
            - Farmer / Agripreneur
            - Environmental Scientist
            - Veterinary Doctor
            - Food Technologist
            - Conservation Officer

            **Kenyan Opportunity:** AgriTech is one of 
            Kenya's fastest growing sectors
            """)

        with st.expander("🏥 Health & Caring Professions"):
            st.markdown("""
            **Strong in:** Biology, Chemistry, CRE

            **Career Options:**
            - Nurse / Clinical Officer
            - Pharmacist
            - Nutritionist
            - Physiotherapist
            - Community Health Worker

            **Kenyan Opportunity:** Universal Health 
            Coverage driving massive demand
            """)

    st.markdown("---")
    st.subheader("📈 Kenya Job Market Snapshot")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Fastest Growing Sector", "Technology", "↑ 34% yearly")
    col2.metric("Largest Employer", "Agriculture", "40% of workforce")
    col3.metric("Youth Unemployment", "~67%", "Opportunity gap")
    col4.metric("SMEs in Kenya", "7.4 Million", "Main job creators")

    st.markdown("---")
    st.subheader("🚀 Entrepreneurship Spotlight")
    st.markdown("""
    Kenya has one of Africa's most vibrant entrepreneurship ecosystems. 
    Notable sectors for young Kenyans:
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**AgriTech** 🌱\nFarm to market platforms, precision farming, crop monitoring")
    with col2:
        st.success("**FinTech** 💳\nMobile money, savings apps, digital lending — M-Pesa ecosystem")
    with col3:
        st.success("**EdTech** 📱\nOnline tutoring, CBC learning tools, skill development platforms")

    st.markdown("---")
    st.caption("📊 Data sources: KNBS Labour Force Report 2024, "
               "LinkedIn Kenya Workforce Insights, World Bank Kenya Economic Update. "
               "Full integration coming in EduGuide AI v2.0")