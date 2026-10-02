from Modules.pdf_parser import extract_text_from_pdf
from Modules.text_cleaner import clean_text
from Modules.resume_parser import parse_resume_sections
from Modules.skill_extractor import extract_skills
from Modules.jd_parser import extract_jd_skills
from Modules.keyword_matcher import match_skills

from Modules.ats_score import (
    calculate_skill_match_score,
    calculate_keyword_match_score,
    calculate_structure_score,
    calculate_education_score,
    calculate_experience_score,
    calculate_overall_ats_score
)

from Modules.similarity import calculate_similarity_score
from Modules.recommendations import generate_recommendations


def analyze_resume(
    resume_file,
    job_role,
    job_description
):
    """
    Complete Resume + Job Description analysis.

    Pipeline:
        PDF
        ↓
        Text Extraction
        ↓
        Text Cleaning
        ↓
        Section Detection
        ↓
        Resume Skill Extraction
        ↓
        JD Skill Extraction
        ↓
        Skill Matching
        ↓
        Keyword Matching
        ↓
        TF-IDF Similarity
        ↓
        Structure Analysis
        ↓
        Education Analysis
        ↓
        Experience Analysis
        ↓
        ATS Score
        ↓
        Recommendations

    Returns:
        dict containing all analysis results.
    """

    # =================================================
    # 1. VALIDATE INPUTS
    # =================================================

    if resume_file is None:
        raise ValueError(
            "Please upload a resume PDF."
        )

    if not job_role or not job_role.strip():
        raise ValueError(
            "Please enter the job role."
        )

    if not job_description or not job_description.strip():
        raise ValueError(
            "Please paste the job description."
        )

    job_role = job_role.strip()
    job_description = job_description.strip()

    # =================================================
    # 2. EXTRACT RESUME TEXT
    # =================================================

    resume_text = extract_text_from_pdf(
        resume_file
    )

    if not resume_text or not resume_text.strip():
        raise ValueError(
            "No readable text was found in the resume PDF."
        )

    # =================================================
    # 3. CLEAN RESUME TEXT
    # =================================================

    cleaned_text = clean_text(
        resume_text
    )

    if not cleaned_text:
        raise ValueError(
            "Resume text could not be processed."
        )

    # =================================================
    # 4. DETECT RESUME SECTIONS
    # =================================================

    sections = parse_resume_sections(
        cleaned_text
    )

    # =================================================
    # 5. EXTRACT RESUME SKILLS
    # =================================================

    resume_skills = extract_skills(
        cleaned_text
    )

    # =================================================
    # 6. EXTRACT JOB DESCRIPTION SKILLS
    # =================================================

    jd_skills = extract_jd_skills(
        job_description
    )

    # =================================================
    # 7. MATCH RESUME SKILLS WITH JD SKILLS
    # =================================================

    matched_skills, missing_skills = match_skills(
        resume_skills,
        jd_skills
    )

    # =================================================
    # 8. SKILL MATCH SCORE
    # =================================================

    skill_match_score = calculate_skill_match_score(
        matched_skills,
        missing_skills
    )

    # =================================================
    # 9. KEYWORD MATCH SCORE
    # =================================================

    keyword_match_score = calculate_keyword_match_score(
        cleaned_text,
        job_description
    )

    # =================================================
    # 10. RESUME-JD SIMILARITY SCORE
    # =================================================

    similarity_score = calculate_similarity_score(
        cleaned_text,
        job_description
    )

    # =================================================
    # 11. RESUME STRUCTURE SCORE
    # =================================================

    structure_score = calculate_structure_score(
        sections
    )

    # =================================================
    # 12. EDUCATION MATCH SCORE
    # =================================================

    education_score = calculate_education_score(
        cleaned_text,
        job_description
    )

    # =================================================
    # 13. EXPERIENCE MATCH SCORE
    # =================================================

    experience_score = calculate_experience_score(
        cleaned_text,
        job_description
    )

    # =================================================
    # 14. OVERALL ATS SCORE
    # =================================================

    overall_ats_score = calculate_overall_ats_score(
        skill_match_score,
        keyword_match_score,
        similarity_score,
        structure_score,
        education_score,
        experience_score
    )

    # =================================================
    # 15. GENERATE RECOMMENDATIONS
    # =================================================

    recommendations = generate_recommendations(
        skill_match_score,
        keyword_match_score,
        similarity_score,
        structure_score,
        education_score,
        experience_score,
        missing_skills
    )

    # =================================================
    # 16. BUILD COMPLETE RESULT
    # =================================================

    result = {

        # -----------------------------
        # Job information
        # -----------------------------

        "job_role":
            job_role,

        "job_description":
            job_description,

        # -----------------------------
        # Resume text
        # -----------------------------

        "resume_text":
            resume_text,

        "cleaned_text":
            cleaned_text,

        # -----------------------------
        # Resume sections
        # -----------------------------

        "sections":
            sections,

        # -----------------------------
        # Skills
        # -----------------------------

        "resume_skills":
            resume_skills,

        "jd_skills":
            jd_skills,

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills,

        # -----------------------------
        # Individual scores
        # -----------------------------

        "skill_match_score":
            skill_match_score,

        "keyword_match_score":
            keyword_match_score,

        "similarity_score":
            similarity_score,

        "structure_score":
            structure_score,

        "education_score":
            education_score,

        "experience_score":
            experience_score,

        # -----------------------------
        # Final score
        # -----------------------------

        "overall_ats_score":
            overall_ats_score,

        # -----------------------------
        # Recommendations
        # -----------------------------

        "recommendations":
            recommendations
    }

    return result