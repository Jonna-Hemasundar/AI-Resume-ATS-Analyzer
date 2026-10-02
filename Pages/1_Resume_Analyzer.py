import json
import os
from datetime import datetime

import streamlit as st

from Modules.analyzer import analyze_resume


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("📄 AI Resume & ATS Analyzer")

st.write(
    "Analyze your resume against a specific job description "
    "and discover how well your resume matches the role."
)

st.caption(
    "🎯 ATS Score  •  🛠️ Skill Matching  •  🔑 Keywords  •  "
    "📊 Similarity  •  📑 Structure  •  💡 Recommendations"
)


# =========================================================
# JOB INFORMATION
# =========================================================

st.divider()

with st.container(border=True):

    st.header("💼 Job Information")

    st.info(
        "Enter the target job role and paste the complete job "
        "description below."
    )

    col1, col2 = st.columns([1, 2])

    with col1:

        job_role = st.text_input(
            "🎯 Job Role",
            placeholder="Example: Data Analyst"
        )

    with col2:

        job_description = st.text_area(
            "📋 Job Description",
            placeholder=(
                "Paste the complete job description here..."
            ),
            height=180
        )


    if job_role.strip() and job_description.strip():

        st.success(
            "✅ Job information is ready for analysis."
        )

    elif job_role.strip():

        st.warning(
            "⚠️ Please paste the job description."
        )

    elif job_description.strip():

        st.warning(
            "⚠️ Please enter the job role."
        )

    else:

        st.caption(
            "💡 Example: Data Analyst | Business Analyst | Associate Analyst"
        )


# =========================================================
# RESUME UPLOAD
# =========================================================

st.divider()

with st.container(border=True):

    st.header("📄 Resume Upload")

    st.write(
        "Upload your resume as a PDF file."
    )

    resume_file = st.file_uploader(
        "Choose your Resume PDF",
        type=["pdf"],
        help="Upload a text-based PDF resume."
    )


    if resume_file:

        st.success(
            f"✅ Resume uploaded: **{resume_file.name}**"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "📄 File",
                resume_file.name
            )

        with col2:

            file_size_kb = resume_file.size / 1024

            st.metric(
                "📦 File Size",
                f"{file_size_kb:.1f} KB"
            )

        with col3:

            st.metric(
                "📌 Format",
                "PDF"
            )

    else:

        st.info(
            "📥 Please upload your resume PDF."
        )


# =========================================================
# WHAT WILL BE ANALYZED
# =========================================================

st.divider()

st.header("🔍 What Will Be Analyzed?")


col1, col2, col3 = st.columns(3)


with col1:

    with st.container(border=True):

        st.subheader("🎯 ATS Score")

        st.write(
            "Overall alignment between your resume "
            "and the job description."
        )


    with st.container(border=True):

        st.subheader("🛠️ Skill Matching")

        st.write(
            "Identify matched and missing skills."
        )


with col2:

    with st.container(border=True):

        st.subheader("🔑 Keyword Analysis")

        st.write(
            "Find important keywords from the job description."
        )


    with st.container(border=True):

        st.subheader("📊 JD Similarity")

        st.write(
            "Compare resume and job-description content."
        )


with col3:

    with st.container(border=True):

        st.subheader("📑 Resume Structure")

        st.write(
            "Check important resume sections."
        )


    with st.container(border=True):

        st.subheader("💡 Recommendations")

        st.write(
            "Generate suggestions for improving your resume."
        )


# =========================================================
# ANALYSIS READY STATUS
# =========================================================

st.divider()

with st.container(border=True):

    st.header("🚀 Ready to Analyze?")


    ready_resume = resume_file is not None
    ready_role = bool(job_role.strip())
    ready_jd = bool(job_description.strip())


    col1, col2, col3 = st.columns(3)


    with col1:

        if ready_resume:

            st.success("✅ Resume Ready")

        else:

            st.warning("⏳ Resume Required")


    with col2:

        if ready_role:

            st.success("✅ Job Role Ready")

        else:

            st.warning("⏳ Job Role Required")


    with col3:

        if ready_jd:

            st.success("✅ Job Description Ready")

        else:

            st.warning("⏳ Job Description Required")


    st.write("")


    analyze_button = st.button(
        "🚀 Analyze My Resume",
        type="primary",
        use_container_width=True
    )


# =========================================================
# RUN ANALYSIS
# =========================================================

if analyze_button:

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if resume_file is None:

        st.error(
            "❌ Please upload your resume PDF."
        )

        st.stop()


    if not job_role.strip():

        st.error(
            "❌ Please enter the job role."
        )

        st.stop()


    if not job_description.strip():

        st.error(
            "❌ Please paste the job description."
        )

        st.stop()


    # -----------------------------------------------------
    # ANALYSIS
    # -----------------------------------------------------

    try:

        with st.spinner(
            "🔍 Analyzing your resume... Please wait."
        ):

            result = analyze_resume(
                resume_file=resume_file,
                job_role=job_role,
                job_description=job_description
            )


        # -------------------------------------------------
        # SAVE RESULT TO SESSION
        # -------------------------------------------------

        st.session_state["analysis_result"] = result

        st.session_state["resume_filename"] = (
            resume_file.name
        )


        # -------------------------------------------------
        # HISTORY FILE
        # -------------------------------------------------

        history_directory = "data"

        history_file = os.path.join(
            history_directory,
            "history.json"
        )

        os.makedirs(
            history_directory,
            exist_ok=True
        )


        history = []


        if os.path.exists(history_file):

            try:

                with open(
                    history_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    history = json.load(file)


                if not isinstance(history, list):

                    history = []


            except Exception:

                history = []


        # -------------------------------------------------
        # HISTORY RECORD
        # -------------------------------------------------

        history_record = {

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "resume_filename": resume_file.name,

            "job_role": job_role,

            "overall_ats_score": result[
                "overall_ats_score"
            ],

            "skill_match_score": result[
                "skill_match_score"
            ],

            "keyword_match_score": result[
                "keyword_match_score"
            ],

            "similarity_score": result[
                "similarity_score"
            ],

            "structure_score": result[
                "structure_score"
            ],

            "education_score": result[
                "education_score"
            ],

            "experience_score": result[
                "experience_score"
            ],

            "matched_skills": result[
                "matched_skills"
            ],

            "missing_skills": result[
                "missing_skills"
            ],

            "recommendations": result[
                "recommendations"
            ]
        }


        history.append(
            history_record
        )


        # Keep latest 50 analyses

        history = history[-50:]


        with open(
            history_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )


        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        st.success(
            "✅ Resume analysis completed successfully!"
        )


        # =================================================
        # QUICK RESULTS
        # =================================================

        st.divider()

        st.header("📊 Quick Results")


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "🎯 ATS Score",
                f"{result['overall_ats_score']:.1f}%"
            )


        with col2:

            st.metric(
                "🛠️ Skill Match",
                f"{result['skill_match_score']:.1f}%"
            )


        with col3:

            st.metric(
                "🔑 Keyword Match",
                f"{result['keyword_match_score']:.1f}%"
            )


        with col4:

            st.metric(
                "📊 JD Similarity",
                f"{result['similarity_score']:.1f}%"
            )


        # =================================================
        # ATS PROGRESS
        # =================================================

        with st.container(border=True):

            st.subheader("🎯 ATS Score")

            score = float(
                result["overall_ats_score"]
            )

            st.progress(
                min(
                    max(
                        int(score),
                        0
                    ),
                    100
                )
            )


            if score >= 80:

                st.success(
                    "🟢 Strong alignment with the job description."
                )

            elif score >= 65:

                st.info(
                    "🔵 Good alignment with the job description."
                )

            elif score >= 50:

                st.warning(
                    "🟡 Moderate alignment. Review the missing areas."
                )

            else:

                st.error(
                    "🔴 Several areas may need improvement."
                )


        # =================================================
        # DETAILED REPORT
        # =================================================

        st.divider()

        with st.container(border=True):

            st.header("📊 Detailed Report")

            st.write(
                "Your complete analysis is ready. "
                "Open the detailed report to view skills, "
                "scores, structure, and recommendations."
            )


            if st.button(
                "📊 Open Detailed Analysis Report",
                type="primary",
                use_container_width=True
            ):

                st.switch_page(
                    "pages/2_Analysis_Report.py"
                )


    except Exception as error:

        st.error(
            f"❌ Analysis failed: {error}"
        )