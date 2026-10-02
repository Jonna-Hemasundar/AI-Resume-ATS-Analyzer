import pandas as pd
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Analysis History",
    page_icon="🕘",
    layout="wide"
)


# =========================================================
# PAGE TITLE
# =========================================================

st.title(
    "🕘 Analysis History"
)

st.write(
    "View previous resume analyses and their ATS-style scores."
)


# =========================================================
# LOAD SESSION HISTORY
# =========================================================

history = st.session_state.get(
    "history",
    []
)


# =========================================================
# EMPTY HISTORY
# =========================================================

if not history:

    st.info(
        "📭 No analysis history available yet."
    )

    st.write(
        "Analyze a resume first to see your results here."
    )

    if st.button(
        "📄 Analyze Resume",
        type="primary",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Resume_Analyzer.py"
        )

    st.stop()


# =========================================================
# OVERVIEW METRICS
# =========================================================

st.divider()

st.header(
    "📊 History Overview"
)


scores = []


for item in history:

    try:

        score = float(
            item.get(
                "overall_ats_score",
                0
            )
        )

        scores.append(
            score
        )

    except Exception:

        continue


total_analyses = len(
    history
)


average_score = (
    sum(scores) / len(scores)
    if scores
    else 0
)


highest_score = (
    max(scores)
    if scores
    else 0
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Analyses",
        total_analyses
    )


with col2:

    st.metric(
        "Average ATS Score",
        f"{average_score:.1f}%"
    )


with col3:

    st.metric(
        "Highest ATS Score",
        f"{highest_score:.1f}%"
    )


# =========================================================
# SCORE TREND
# =========================================================

st.divider()

st.header(
    "📈 ATS Score Trend"
)


trend_rows = []


for index, item in enumerate(
    history,
    start=1
):

    try:

        score = float(
            item.get(
                "overall_ats_score",
                0
            )
        )

    except Exception:

        score = 0


    trend_rows.append(
        {
            "Analysis": index,
            "ATS Score": score
        }
    )


trend_df = pd.DataFrame(
    trend_rows
)


st.line_chart(
    trend_df.set_index(
        "Analysis"
    )
)


# =========================================================
# HISTORY TABLE
# =========================================================

st.divider()

st.header(
    "📋 Previous Analyses"
)


table_rows = []


for index, item in enumerate(
    history,
    start=1
):

    table_rows.append(
        {
            "No.": index,

            "Date": item.get(
                "date",
                "N/A"
            ),

            "Resume": item.get(
                "resume_filename",
                "N/A"
            ),

            "Job Role": item.get(
                "job_role",
                "N/A"
            ),

            "ATS Score": f"{float(item.get('overall_ats_score', 0)):.1f}%",

            "Skill Match": f"{float(item.get('skill_match_score', 0)):.1f}%",

            "Keyword Match": f"{float(item.get('keyword_match_score', 0)):.1f}%",

            "JD Similarity": f"{float(item.get('similarity_score', 0)):.1f}%"
        }
    )


history_df = pd.DataFrame(
    table_rows
)


st.dataframe(
    history_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# DETAILED HISTORY
# =========================================================

st.divider()

st.header(
    "🔎 Analysis Details"
)


# Show newest analysis first

for index in range(
    len(history) - 1,
    -1,
    -1
):

    item = history[index]


    job_role = item.get(
        "job_role",
        "Unknown Role"
    )

    resume_name = item.get(
        "resume_filename",
        "Unknown Resume"
    )

    date = item.get(
        "date",
        "Unknown Date"
    )

    try:

        ats_score = float(
            item.get(
                "overall_ats_score",
                0
            )
        )

    except Exception:

        ats_score = 0


    with st.expander(
        f"📄 {job_role} | {resume_name} | {date} | ATS: {ats_score:.1f}%"
    ):

        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "ATS Score",
                f"{ats_score:.1f}%"
            )


        with col2:

            st.metric(
                "Skill Match",
                f"{float(item.get('skill_match_score', 0)):.1f}%"
            )


        with col3:

            st.metric(
                "Keyword Match",
                f"{float(item.get('keyword_match_score', 0)):.1f}%"
            )


        with col4:

            st.metric(
                "JD Similarity",
                f"{float(item.get('similarity_score', 0)):.1f}%"
            )


        st.subheader(
            "📊 Other Scores"
        )


        other_scores = pd.DataFrame(
            {
                "Component": [
                    "Resume Structure",
                    "Education Match",
                    "Experience Match"
                ],

                "Score": [
                    float(
                        item.get(
                            "structure_score",
                            0
                        )
                    ),

                    float(
                        item.get(
                            "education_score",
                            0
                        )
                    ),

                    float(
                        item.get(
                            "experience_score",
                            0
                        )
                    )
                ]
            }
        )


        other_scores["Score"] = (
            other_scores["Score"]
            .round(1)
            .astype(str)
            + "%"
        )


        st.dataframe(
            other_scores,
            use_container_width=True,
            hide_index=True
        )


        # -------------------------------------------------
        # MATCHED SKILLS
        # -------------------------------------------------

        st.subheader(
            "✅ Matched Skills"
        )


        matched = item.get(
            "matched_skills",
            {}
        )


        matched_list = []


        if isinstance(matched, dict):

            for skills in matched.values():

                if isinstance(skills, list):

                    for skill in skills:

                        if skill not in matched_list:

                            matched_list.append(
                                skill
                            )


        if matched_list:

            st.write(
                ", ".join(
                    matched_list
                )
            )

        else:

            st.write(
                "No matched skills recorded."
            )


        # -------------------------------------------------
        # MISSING SKILLS
        # -------------------------------------------------

        st.subheader(
            "❌ Missing Skills"
        )


        missing = item.get(
            "missing_skills",
            {}
        )


        missing_list = []


        if isinstance(missing, dict):

            for skills in missing.values():

                if isinstance(skills, list):

                    for skill in skills:

                        if skill not in missing_list:

                            missing_list.append(
                                skill
                            )


        if missing_list:

            st.write(
                ", ".join(
                    missing_list
                )
            )

        else:

            st.write(
                "No missing skills recorded."
            )


        # -------------------------------------------------
        # RECOMMENDATIONS
        # -------------------------------------------------

        st.subheader(
            "💡 Recommendations"
        )


        recommendations = item.get(
            "recommendations",
            []
        )


        if recommendations:

            for recommendation in recommendations:

                st.info(
                    recommendation
                )

        else:

            st.write(
                "No recommendations recorded."
            )


# =========================================================
# CLEAR HISTORY
# =========================================================

st.divider()

st.header(
    "🗑️ Manage History"
)


st.warning(
    "Clearing history will remove all analysis records from this session."
)


if st.button(
    "🗑️ Clear All History",
    type="secondary",
    use_container_width=True
):

    st.session_state["history"] = []

    st.success(
        "✅ Analysis history has been cleared."
    )

    st.rerun()


# =========================================================
# BOTTOM ACTION
# =========================================================

st.divider()

if st.button(
    "📄 Analyze a New Resume",
    type="primary",
    use_container_width=True
):

    st.switch_page(
        "pages/1_Resume_Analyzer.py"
    )