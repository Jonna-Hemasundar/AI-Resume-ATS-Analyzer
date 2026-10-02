# =========================================================
# RECOMMENDATION GENERATOR
# =========================================================

def generate_recommendations(
    skill_match_score,
    keyword_match_score,
    similarity_score,
    structure_score,
    education_score,
    experience_score,
    missing_skills
):
    """
    Generates actionable resume recommendations
    based on ATS analysis scores.

    Parameters
    ----------
    skill_match_score : float
        Percentage of required JD skills found.

    keyword_match_score : float
        Percentage of meaningful JD keywords found.

    similarity_score : float
        TF-IDF similarity between resume and JD.

    structure_score : float
        Resume structure completeness score.

    education_score : float
        Education requirement match score.

    experience_score : float
        Experience requirement match score.

    missing_skills : dict
        Categorized list of missing skills.

    Returns
    -------
    list
        List of recommendation strings.
    """

    recommendations = []


    # =====================================================
    # 1. SKILL MATCH
    # =====================================================

    if skill_match_score < 40:

        recommendations.append(
            "Your resume has low skill alignment with "
            "the job description. Review the required "
            "skills and add only those you genuinely possess."
        )

    elif skill_match_score < 60:

        recommendations.append(
            "Your resume is missing several skills "
            "mentioned in the job description. Highlight "
            "relevant skills you genuinely possess and "
            "consider developing important missing skills."
        )

    elif skill_match_score < 80:

        recommendations.append(
            "Your skill alignment is moderate. Review "
            "the missing skills and make sure your relevant "
            "technical skills are clearly visible."
        )

    else:

        recommendations.append(
            "Your technical skill alignment is strong. "
            "Keep the most relevant skills clearly visible "
            "for the target role."
        )


    # =====================================================
    # 2. KEYWORD MATCH
    # =====================================================

    if keyword_match_score < 40:

        recommendations.append(
            "Many important terms from the job description "
            "were not detected in the resume. Naturally "
            "include relevant terminology where it accurately "
            "describes your experience."
        )

    elif keyword_match_score < 60:

        recommendations.append(
            "Your keyword coverage can be improved. "
            "Review the job description and incorporate "
            "relevant terms into your summary, skills, "
            "projects, and experience sections."
        )

    elif keyword_match_score < 80:

        recommendations.append(
            "Your keyword coverage is reasonable, but some "
            "job-specific terminology could be added naturally "
            "to improve alignment."
        )


    # =====================================================
    # 3. RESUME-JD SIMILARITY
    # =====================================================

    if similarity_score < 30:

        recommendations.append(
            "The resume content has relatively low similarity "
            "to the job description. Tailor your professional "
            "summary, experience, and projects toward the "
            "responsibilities of the target role."
        )

    elif similarity_score < 50:

        recommendations.append(
            "The resume has moderate content similarity with "
            "the job description. Use role-relevant terminology "
            "and emphasize experience that directly relates "
            "to the position."
        )

    elif similarity_score < 70:

        recommendations.append(
            "The resume content is reasonably aligned with "
            "the job description. Further tailoring of project "
            "and experience descriptions may improve relevance."
        )


    # =====================================================
    # 4. RESUME STRUCTURE
    # =====================================================

    if structure_score < 50:

        recommendations.append(
            "Several important resume sections were not detected. "
            "Use clear headings such as Summary, Skills, Experience, "
            "Education, Projects, and Certifications."
        )

    elif structure_score < 80:

        recommendations.append(
            "Your resume structure can be improved. Make sure "
            "common sections such as Summary, Experience, "
            "Education, Skills, Projects, and Certifications "
            "have clear headings."
        )


    # =====================================================
    # 5. EDUCATION
    # =====================================================

    if education_score < 50:

        recommendations.append(
            "The education information detected in your resume "
            "does not strongly match the education requirements "
            "in the job description. Check that your degree, "
            "specialization, and relevant qualifications are "
            "clearly stated."
        )

    elif education_score < 80:

        recommendations.append(
            "Some education requirements may not be clearly "
            "represented in the resume. Make your degree and "
            "specialization easy to identify."
        )


    # =====================================================
    # 6. EXPERIENCE
    # =====================================================

    if experience_score < 50:

        recommendations.append(
            "The detected experience level is below the "
            "requirement mentioned in the job description. "
            "If you have relevant internships, projects, "
            "freelance work, or other applicable experience, "
            "describe them clearly and accurately."
        )

    elif experience_score < 80:

        recommendations.append(
            "The experience requirement may only be partially "
            "satisfied. Clearly describe the duration and "
            "responsibilities of relevant internships or work "
            "experience."
        )


    # =====================================================
    # 7. MISSING SKILLS
    # =====================================================

    if missing_skills:

        missing_count = sum(
            len(skills)
            for skills in missing_skills.values()
        )

        # Flatten missing skills

        missing_skill_names = []

        for skills in missing_skills.values():

            for skill in skills:

                if skill not in missing_skill_names:

                    missing_skill_names.append(
                        skill
                    )

        # -------------------------------------------------
        # First few missing skills
        # -------------------------------------------------

        preview_skills = missing_skill_names[:8]

        preview_text = ", ".join(
            preview_skills
        )

        if missing_count > 8:

            preview_text += ", ..."

        recommendations.append(
            f"{missing_count} required skill(s) were not "
            f"detected in the resume: {preview_text}. "
            "Add them only when they genuinely reflect "
            "your knowledge or experience."
        )


    # =====================================================
    # 8. GENERAL RESUME IMPROVEMENT
    # =====================================================

    if keyword_match_score < 60:

        recommendations.append(
            "Use specific, role-relevant wording instead of "
            "generic descriptions. For example, describe the "
            "tools used, analysis performed, and measurable "
            "outcomes of your projects."
        )


    if similarity_score < 50:

        recommendations.append(
            "Prioritize the most relevant projects and "
            "experience near the top of the resume so the "
            "content quickly communicates your fit for the "
            "target role."
        )


    # =====================================================
    # 9. NO MAJOR ISSUES
    # =====================================================

    if not recommendations:

        recommendations.append(
            "The resume shows good alignment with the "
            "provided job description. Continue tailoring "
            "the resume to each specific role and keep the "
            "information accurate and easy to scan."
        )


    # =====================================================
    # 10. REMOVE DUPLICATES
    # =====================================================

    unique_recommendations = []

    for recommendation in recommendations:

        if recommendation not in unique_recommendations:

            unique_recommendations.append(
                recommendation
            )


    return unique_recommendations