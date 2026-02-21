# EduGuide AI - Parent Dashboard
import streamlit as st


def show():
    st.title("👨‍👩‍👧 Parent Dashboard")
    st.markdown("### Understanding your child's progress under CBC")
    st.markdown("---")

    # Student selector
    student_name = st.text_input("Enter your child's name",
                                 placeholder="e.g. Amina Wanjiru")
    g1 = st.slider("Your child's Term 1 Grade", 0, 20, 12)
    g2 = st.slider("Your child's Term 2 Grade", 0, 20, 13)

    if st.button("View My Child's Report", use_container_width=True):
        st.markdown("---")
        name = student_name if student_name else "Your Child"

        # ── Performance Summary ────────────────────────
        st.subheader(f"📊 {name}'s Progress Summary")

        col1, col2, col3 = st.columns(3)
        col1.metric("Term 1 Grade", f"{g1}/20")
        col2.metric("Term 2 Grade", f"{g2}/20",
                    delta=f"{g2 - g1:+d} from Term 1")
        col3.metric("Status",
                    "✅ On Track" if g2 >= 10 else "⚠️ Needs Support")

        st.markdown("---")

        # ── CBC Explainer ──────────────────────────────
        st.subheader("📚 What does this mean under CBC?")

        if g2 >= 16:
            st.success("""
            **Exceeding Expectations** 🌟

            Your child is performing excellently. Under CBC, this means they 
            have fully mastered the competencies for this level and are ready 
            for more challenging work. Keep encouraging them!
            """)
        elif g2 >= 10:
            st.info("""
            **Meeting Expectations** ✅

            Your child is on track. Under CBC, this means they have 
            demonstrated the core competencies expected at this level. 
            Continue supporting their studies at home.
            """)
        elif g2 >= 5:
            st.warning("""
            **Approaching Expectations** ⚠️

            Your child needs some support. Under CBC, this means they are 
            developing the required competencies but need extra attention 
            in certain areas. Please speak with their teacher about 
            specific support strategies.
            """)
        else:
            st.error("""
            **Below Expectations** 🔴

            Your child needs urgent support. Please schedule a meeting 
            with the class teacher as soon as possible to discuss a 
            personalised support plan.
            """)

        st.markdown("---")

        # ── What You Can Do ────────────────────────────
        st.subheader("🏠 How You Can Help at Home")
        st.markdown("""
        - **Create a study routine** — set aside 1 hour daily for homework
        - **Ask about their day** — simple conversations build confidence
        - **Attend school meetings** — stay connected with their teacher
        - **Celebrate small wins** — every improvement deserves recognition
        - **Limit screen time** during school nights
        """)

        st.markdown("---")

        # ── Career Preview ─────────────────────────────
        st.subheader("🌟 Your Child's Potential Pathways")
        st.info("Based on CBC competency areas, here are broad pathways "
                "to explore as your child grows:")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**🔬 STEM Pathway**")
            st.markdown("Engineering, Medicine, Technology, Agriculture")
        with col2:
            st.markdown("**🎨 Arts & Humanities**")
            st.markdown("Design, Media, Education, Social Work")
        with col3:
            st.markdown("**💼 Business & Entrepreneurship**")
            st.markdown("Trade, Finance, Tourism, Innovation")

        st.markdown("---")
        st.caption("💡 Full career pathway analysis with Kenyan job market "
                   "data — Coming Soon")