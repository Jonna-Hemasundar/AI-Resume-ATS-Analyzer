import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Resume & ATS Analyzer",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# PAGE DEFINITIONS
# =========================================================

home = st.Page(
    "pages/0_Home.py",
    title="Home",
    icon="🏠"
)

resume_analyzer = st.Page(
    "pages/1_Resume_Analyzer.py",
    title="Resume Analyzer",
    icon="📄"
)

analysis_report = st.Page(
    "pages/2_Analysis_Report.py",
    title="Analysis Report",
    icon="📊"
)

history = st.Page(
    "pages/3_History.py",
    title="History",
    icon="🕒"
)


# =========================================================
# NAVIGATION
# =========================================================

pg = st.navigation(
    [
        home,
        resume_analyzer,
        analysis_report,
        history
    ],
    position="sidebar",
    expanded=True
)


# =========================================================
# RUN SELECTED PAGE
# =========================================================

pg.run()