import streamlit as st
import pandas as pd
import plotly.express as px

from Modules.ats_score import get_score_level


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Analysis Report",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# GET ANALYSIS RESULT
# =========================================================

result = st.session_state.get(
    "analysis_result"
)


# =========================================================
# PAGE TITLE
# =========================================================

st.title(
    "📊 Resume Analysis Report"
)

st.write(
    "Detailed ATS-style analysis of your resume against the selected job description."
)


# =========================================================
# CHECK RESULT
# =========================================================

if not result:

    st.warning(
        "⚠️ No analysis result is available yet."
    )

    st.info(
        "Please go to Resume Analyzer, upload your resume, "
        "enter a job description, and run the analysis."
    )

    if st.button(
        "📄 Go to Resume Analyzer",
        type="primary",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Resume_Analyzer.py"
        )

    st.stop()


# =========================================================
# BASIC INFORMATION
# =========================================================

st.divider()

st.header(
    "💼 Analysis Information"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        f"**🎯 Target Role**\n\n"
        f"{result.get('job_role', 'Not available')}"
    )


with col2:

    st.success(
        f"**📄 Resume**\n\n"
        f"{st.session_state.get('resume_filename', 'Uploaded Resume')}"
    )


with col3:

    st.warning(
        f"**📊 Analysis Type**\n\n"
        f"ATS + Skills + Keywords + Similarity"
    )


# =========================================================
# OVERALL ATS SCORE
# =========================================================

st.divider()

st.header(
    "🎯 Overall ATS Score"
)


overall_score = float(
    result.get(
        "overall_ats_score",
        0
    )
)


score_level = get_score_level(
    overall_score
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "🎯 ATS Score",
        f"{overall_score:.1f}%"
    )


with col2:

    st.metric(
        "📌 Score Level",
        score_level
    )


with col3:

    if overall_score >= 80:

        status = "🟢 Strong"

    elif overall_score >= 65:

        status = "🔵 Good"

    elif overall_score >= 50:

        status = "🟡 Moderate"

    else:

        status = "🔴 Improve"


    st.metric(
        "📈 Alignment",
        status
    )


st.progress(
    min(
        max(
            int(overall_score),
            0
        ),
        100
    )
)


# =========================================================
# SCORE STATUS
# =========================================================

if overall_score >= 80:

    st.success(
        "🟢 Strong alignment with the supplied job description."
    )

elif overall_score >= 65:

    st.info(
        "🔵 Good alignment with the supplied job description. "
        "Some improvements can further strengthen the resume."
    )

elif overall_score >= 50:

    st.warning(
        "🟡 Moderate alignment. Review the missing skills and recommendations."
    )

else:

    st.error(
        "🔴 Several areas of the resume may need improvement for this job."
    )


# =========================================================
# SCORE DATA
# =========================================================

score_data = pd.DataFrame(
    {
        "Component": [
            "Skill Match",
            "Keyword Match",
            "JD Similarity",
            "Resume Structure",
            "Education Match",
            "Experience Match"
        ],

        "Score": [
            result.get(
                "skill_match_score",
                0
            ),

            result.get(
                "keyword_match_score",
                0
            ),

            result.get(
                "similarity_score",
                0
            ),

            result.get(
                "structure_score",
                0
            ),

            result.get(
                "education_score",
                0
            ),

            result.get(
                "experience_score",
                0
            )
        ]
    }
)


score_data["Score"] = pd.to_numeric(
    score_data["Score"],
    errors="coerce"
).fillna(0)


# =========================================================
# TABS
# =========================================================

st.divider()

tab_overview, tab_skills, tab_structure, tab_recommendations, tab_details = st.tabs(
    [
        "📊 Overview",
        "🛠️ Skills",
        "📑 Structure",
        "💡 Recommendations",
        "📋 Details"
    ]
)


# =========================================================
# TAB 1 - OVERVIEW
# =========================================================

with tab_overview:

    st.header(
        "📊 Score Overview"
    )

    st.write(
        "The chart below shows how the resume performed across each analysis component."
    )


    fig = px.bar(
        score_data,
        x="Component",
        y="Score",
        range_y=[0, 100],
        text="Score",
        title="ATS Analysis Breakdown"
    )


    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )


    fig.update_layout(
        yaxis_title="Score (%)",
        xaxis_title="Analysis Component"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader(
        "📋 Score Details"
    )


    score_table = score_data.copy()


    score_table["Score"] = (
        score_table["Score"]
        .round(2)
        .astype(str)
        + "%"
    )


    st.dataframe(
        score_table,
        use_container_width=True,
        hide_index=True
    )


    st.subheader(
        "⚖️ ATS Score Weights"
    )


    weight_data = pd.DataFrame(
        {
            "Component": [
                "Skill Match",
                "Keyword Match",
                "JD Similarity",
                "Resume Structure",
                "Education Match",
                "Experience Match"
            ],

            "Weight": [
                35,
                15,
                20,
                10,
                10,
                10
            ]
        }
    )


    fig_weight = px.pie(
        weight_data,
        names="Component",
        values="Weight",
        title="ATS Score Weight Distribution"
    )


    st.plotly_chart(
        fig_weight,
        use_container_width=True
    )


# =========================================================
# TAB 2 - SKILLS
# =========================================================

with tab_skills:

    st.header(
        "🛠️ Skill Analysis"
    )


    resume_skills = result.get(
        "resume_skills",
        {}
    )


    jd_skills = result.get(
        "jd_skills",
        {}
    )


    matched_skills = result.get(
        "matched_skills",
        {}
    )


    missing_skills = result.get(
        "missing_skills",
        {}
    )


    # -----------------------------------------------------
    # SKILL METRICS
    # -----------------------------------------------------

    matched_list = []


    for skills in matched_skills.values():

        for skill in skills:

            if skill not in matched_list:

                matched_list.append(
                    skill
                )


    missing_list = []


    for skills in missing_skills.values():

        for skill in skills:

            if skill not in missing_list:

                missing_list.append(
                    skill
                )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Skills in Resume",
            sum(
                len(skills)
                for skills in resume_skills.values()
            )
        )


    with col2:

        st.metric(
            "✅ Matched Skills",
            len(matched_list)
        )


    with col3:

        st.metric(
            "❌ Missing Skills",
            len(missing_list)
        )


    st.divider()


    # -----------------------------------------------------
    # MATCHED SKILLS
    # -----------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            "✅ Matched Skills"
        )


        if matched_list:

            for skill in matched_list:

                st.success(
                    f"✓ {skill}"
                )

        else:

            st.info(
                "No matching skills were detected."
            )


    # -----------------------------------------------------
    # MISSING SKILLS
    # -----------------------------------------------------

    with col2:

        st.subheader(
            "❌ Missing Skills"
        )


        if missing_list:

            for skill in missing_list:

                st.warning(
                    f"⚠ {skill}"
                )

        else:

            st.success(
                "No major missing skills detected."
            )


    st.divider()


    # -----------------------------------------------------
    # RESUME SKILLS
    # -----------------------------------------------------

    st.subheader(
        "📄 Skills Detected in Resume"
    )


    resume_skill_rows = []


    for category, skills in resume_skills.items():

        for skill in skills:

            resume_skill_rows.append(
                {
                    "Category": category.title(),
                    "Skill": skill
                }
            )


    if resume_skill_rows:

        resume_skill_df = pd.DataFrame(
            resume_skill_rows
        )


        st.dataframe(
            resume_skill_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No skills detected."
        )


    # -----------------------------------------------------
    # JD SKILLS
    # -----------------------------------------------------

    st.subheader(
        "💼 Skills Detected in Job Description"
    )


    jd_skill_rows = []


    for category, skills in jd_skills.items():

        for skill in skills:

            jd_skill_rows.append(
                {
                    "Category": category.title(),
                    "Skill": skill
                }
            )


    if jd_skill_rows:

        jd_skill_df = pd.DataFrame(
            jd_skill_rows
        )


        st.dataframe(
            jd_skill_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No specific skills detected in the job description."
        )


# =========================================================
# TAB 3 - STRUCTURE
# =========================================================

with tab_structure:

    st.header(
        "📑 Resume Structure"
    )


    sections = result.get(
        "sections",
        {}
    )


    expected_sections = [
        "summary",
        "experience",
        "education",
        "skills",
        "projects",
        "certifications"
    ]


    structure_rows = []


    for section in expected_sections:

        if section in sections:

            status = "✅ Detected"

        else:

            status = "❌ Missing"


        structure_rows.append(
            {
                "Section": section.title(),
                "Status": status
            }
        )


    structure_df = pd.DataFrame(
        structure_rows
    )


    st.dataframe(
        structure_df,
        use_container_width=True,
        hide_index=True
    )


    detected_count = sum(
        1
        for section in expected_sections
        if section in sections
    )


    structure_percentage = (
        detected_count
        / len(expected_sections)
        * 100
    )


    st.metric(
        "📑 Standard Sections Detected",
        f"{detected_count}/{len(expected_sections)}"
    )


    st.progress(
        int(structure_percentage)
    )


    st.subheader(
        "📄 Detected Sections"
    )


    if sections:

        for section, content in sections.items():

            with st.expander(
                f"📌 {section.title()}"
            ):

                st.write(
                    content
                )

    else:

        st.warning(
            "No resume sections were detected."
        )


# =========================================================
# TAB 4 - RECOMMENDATIONS
# =========================================================

with tab_recommendations:

    st.header(
        "💡 Resume Improvement Recommendations"
    )


    recommendations = result.get(
        "recommendations",
        []
    )


    if recommendations:

        for index, recommendation in enumerate(
            recommendations,
            start=1
        ):

            st.info(
                f"**{index}.** {recommendation}"
            )

    else:

        st.success(
            "🎉 No additional recommendations were generated."
        )


    if missing_list:

        st.divider()

        st.subheader(
            "🎯 Skills You May Want to Address"
        )


        for skill in missing_list:

            st.warning(
                f"Consider addressing: **{skill}**"
            )


# =========================================================
# TAB 5 - DETAILS
# =========================================================

with tab_details:

    st.header(
        "📋 Job Description"
    )


    with st.expander(
        "💼 View Job Description",
        expanded=True
    ):

        st.write(
            result.get(
                "job_description",
                "Not available"
            )
        )


    st.divider()


    st.header(
        "📄 Extracted Resume Text"
    )


    with st.expander(
        "View Extracted Resume Text"
    ):

        st.text(
            result.get(
                "resume_text",
                "No text available."
            )
        )


# =========================================================
# DOWNLOAD REPORT
# =========================================================

st.divider()

st.header(
    "📥 Export Report"
)


report_lines = []


report_lines.append(
    "AI RESUME & ATS ANALYZER"
)

report_lines.append(
    "=" * 40
)

report_lines.append(
    f"Job Role: {result.get('job_role', '')}"
)

report_lines.append(
    f"Resume: {st.session_state.get('resume_filename', '')}"
)

report_lines.append("")

report_lines.append(
    f"Overall ATS Score: {overall_score:.2f}%"
)

report_lines.append("")

report_lines.append(
    "SCORE BREAKDOWN"
)

report_lines.append(
    "-" * 30
)


for _, row in score_data.iterrows():

    report_lines.append(
        f"{row['Component']}: {row['Score']:.2f}%"
    )


report_lines.append("")

report_lines.append(
    "MATCHED SKILLS"
)

report_lines.append(
    "-" * 30
)


if matched_list:

    for skill in matched_list:

        report_lines.append(
            f"- {skill}"
        )

else:

    report_lines.append(
        "- None"
    )


report_lines.append("")

report_lines.append(
    "MISSING SKILLS"
)

report_lines.append(
    "-" * 30
)


if missing_list:

    for skill in missing_list:

        report_lines.append(
            f"- {skill}"
        )

else:

    report_lines.append(
        "- None"
    )


report_lines.append("")

report_lines.append(
    "RECOMMENDATIONS"
)

report_lines.append(
    "-" * 30
)


if recommendations:

    for recommendation in recommendations:

        report_lines.append(
            f"- {recommendation}"
        )

else:

    report_lines.append(
        "- None"
    )


report_text = "\n".join(
    report_lines
)


st.download_button(
    "📥 Download Analysis Report",
    data=report_text,
    file_name="resume_analysis_report.txt",
    mime="text/plain",
    use_container_width=True
)


# =========================================================
# NAVIGATION BUTTONS
# =========================================================

st.divider()

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "📄 Analyze Another Resume",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Resume_Analyzer.py"
        )


with col2:

    if st.button(
        "🕘 View History",
        use_container_width=True
    ):

        st.switch_page(
            "pages/3_History.py"
        )