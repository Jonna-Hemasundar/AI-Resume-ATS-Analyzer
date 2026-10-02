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
# HOME PAGE
# =========================================================

st.title(
    "🤖 AI Resume & ATS Analyzer"
)

st.subheader(
    "Analyze your resume against any job description"
)

st.write(
    "Upload your resume, provide a target job description, "
    "and get an ATS-style analysis with skill matching, "
    "keyword analysis, similarity scoring, resume structure "
    "analysis, and personalized recommendations."
)


# =========================================================
# MAIN ACTION
# =========================================================

st.divider()

st.header(
    "🚀 Get Started"
)

st.write(
    "Start by uploading your resume and entering the "
    "job description."
)

if st.button(
    "📄 Analyze My Resume",
    type="primary",
    use_container_width=True
):
    st.switch_page(
        "pages/1_Resume_Analyzer.py"
    )


# =========================================================
# FEATURES
# =========================================================

st.divider()

st.header(
    "✨ What This Tool Analyzes"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        "### 🎯 ATS Score\n\n"
        "Get an overall ATS-style score based on "
        "multiple resume and job-description factors."
    )


with col2:

    st.success(
        "### 🛠️ Skill Matching\n\n"
        "Identify skills that match the job description "
        "and skills that are not detected in your resume."
    )


with col3:

    st.warning(
        "### 🔑 Keyword Analysis\n\n"
        "Check how well important job-description "
        "keywords appear in your resume."
    )


col4, col5, col6 = st.columns(3)


with col4:

    st.info(
        "### 📊 JD Similarity\n\n"
        "Compare resume and job-description content "
        "using TF-IDF similarity."
    )


with col5:

    st.success(
        "### 📑 Resume Structure\n\n"
        "Check whether important resume sections "
        "are clearly detected."
    )


with col6:

    st.warning(
        "### 💡 Recommendations\n\n"
        "Receive practical suggestions for improving "
        "resume-job alignment."
    )


# =========================================================
# ANALYSIS PIPELINE
# =========================================================

st.divider()

st.header(
    "🔄 How It Works"
)

steps = [
    "📄 Upload your resume PDF",
    "💼 Enter the target job role",
    "📋 Paste the job description",
    "🔍 Analyze resume content",
    "🧠 Extract skills and keywords",
    "🎯 Match resume against the job",
    "📊 Calculate ATS-style scores",
    "💡 Generate recommendations",
    "📈 View the detailed analysis report",
]


for index, step in enumerate(
    steps,
    start=1
):

    st.write(
        f"**{index}.** {step}"
    )


# =========================================================
# SCORE COMPONENTS
# =========================================================

st.divider()

st.header(
    "📊 Analysis Components"
)


score_components = {
    "Skill Match": "35%",
    "Keyword Match": "15%",
    "JD Similarity": "20%",
    "Resume Structure": "10%",
    "Education Match": "10%",
    "Experience Match": "10%"
}


for component, weight in score_components.items():

    col1, col2 = st.columns(
        [4, 1]
    )

    with col1:

        st.write(
            component
        )

    with col2:

        st.write(
            weight
        )


# =========================================================
# IMPORTANT NOTE
# =========================================================

st.divider()

st.header(
    "ℹ️ Important"
)

st.info(
    "This application provides an ATS-style analysis based "
    "on the supplied resume and job description. The score "
    "is an analytical indicator, not a guarantee of passing "
    "an employer's actual ATS."
)


# =========================================================
# BOTTOM ACTION
# =========================================================

st.divider()

st.subheader(
    "Ready to analyze your resume?"
)


if st.button(
    "🚀 Start Resume Analysis",
    type="primary",
    use_container_width=True
):

    st.switch_page(
        "pages/1_Resume_Analyzer.py"
    )