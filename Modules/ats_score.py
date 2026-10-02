import re


# =========================================================
# 1. SKILL MATCH SCORE
# =========================================================

def calculate_skill_match_score(
    matched_skills,
    missing_skills
):
    """
    Calculates the percentage of JD-required skills
    that are detected in the resume.
    """

    matched_count = sum(
        len(skills)
        for skills in matched_skills.values()
    )

    missing_count = sum(
        len(skills)
        for skills in missing_skills.values()
    )

    total_required = (
        matched_count + missing_count
    )

    if total_required == 0:
        return 0

    score = (
        matched_count
        / total_required
    ) * 100

    return round(score, 2)


# =========================================================
# 2. KEYWORD NORMALIZATION
# =========================================================

def normalize_keyword(text):
    """
    Normalizes common variations of keywords.
    """

    if not text:
        return ""

    text = text.lower()

    replacements = {

        "power-bi":
            "power bi",

        "powerbi":
            "power bi",

        "scikit learn":
            "scikit-learn",

        "machine-learning":
            "machine learning",

        "data-analytics":
            "data analytics",

        "data-analysis":
            "data analysis",

        "data-cleaning":
            "data cleaning",

        "data-preprocessing":
            "data preprocessing",

        "data-validation":
            "data validation",

        "data-visualization":
            "data visualization",

        "problem-solving":
            "problem solving",

        "a / b testing":
            "a/b testing",

        "a-b testing":
            "a/b testing",

        "ab testing":
            "a/b testing",

        "natural-language-processing":
            "natural language processing",

        "generative-ai":
            "generative ai",

        "gen-ai":
            "generative ai",

        "large-language-model":
            "large language model",

        "large-language-models":
            "large language models",

        "retrieval-augmented-generation":
            "retrieval augmented generation",
    }

    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# 3. KEYWORD MATCH SCORE
# =========================================================

def calculate_keyword_match_score(
    resume_text,
    job_description
):
    """
    Calculates overlap between meaningful words
    in the resume and job description.
    """

    if not resume_text or not job_description:
        return 0

    resume_text = normalize_keyword(
        resume_text
    )

    job_description = normalize_keyword(
        job_description
    )

    stop_words = {

        "the",
        "and",
        "or",
        "to",
        "of",
        "in",
        "for",
        "a",
        "an",
        "with",
        "on",
        "is",
        "are",
        "as",
        "be",
        "this",
        "that",
        "will",
        "you",
        "your",
        "we",
        "our",
        "from",
        "by",
        "at",
        "it",
        "their",
        "they",
        "have",
        "has",
        "using",
        "use",
        "work",
        "working",
        "role",
        "responsibilities",
        "requirements",
        "candidate",
        "looking",
        "including",
        "such",
        "also",
        "should",
        "can",
        "may",
        "must",
        "within",
        "into",
        "about",
        "will",
        "who",
        "what",
        "which",
        "while",
        "where",
        "our",
        "their",
        "than",
        "then",
        "these",
        "those",
        "all",
        "any",
        "both",
        "been",
        "being",
        "more",
        "most",
        "other",
        "some",
        "each",
        "per",
    }

    resume_words = set(
        re.findall(
            r"[a-zA-Z0-9+#.-]+",
            resume_text
        )
    )

    jd_words = set(
        re.findall(
            r"[a-zA-Z0-9+#.-]+",
            job_description
        )
    )

    jd_keywords = {
        word
        for word in jd_words
        if word not in stop_words
        and len(word) > 2
    }

    if not jd_keywords:
        return 0

    matched_words = (
        jd_keywords
        .intersection(
            resume_words
        )
    )

    word_score = (
        len(matched_words)
        / len(jd_keywords)
    ) * 100

    return round(
        min(word_score, 100),
        2
    )


# =========================================================
# 4. RESUME STRUCTURE SCORE
# =========================================================

def calculate_structure_score(
    sections
):
    """
    Checks whether important resume sections
    were detected.
    """

    important_sections = [

        "summary",

        "experience",

        "education",

        "skills",

        "projects",

        "certifications"
    ]

    if not sections:
        return 0

    found_sections = 0

    for section in important_sections:

        if (
            section in sections
            and sections[section]
            and sections[section].strip()
        ):

            found_sections += 1

    score = (
        found_sections
        / len(important_sections)
    ) * 100

    return round(
        score,
        2
    )


# =========================================================
# 5. EDUCATION SCORE
# =========================================================

def calculate_education_score(
    resume_text,
    job_description
):
    """
    Compares education-related requirements
    in the JD with education information in the resume.
    """

    if not job_description:
        return 100

    resume_text = resume_text.lower()

    job_description = (
        job_description.lower()
    )

    degree_groups = {

        "bachelor": [

            "bachelor",

            "bachelors",

            "bachelor's",

            "b.tech",

            "btech",

            "b.e",

            "b.e.",

            "undergraduate"
        ],

        "master": [

            "master",

            "masters",

            "master's",

            "m.tech",

            "mtech",

            "m.e",

            "m.e.",

            "mba"
        ],

        "degree": [

            "degree",

            "graduation",

            "graduate"
        ],

        "computer science": [

            "computer science",

            "computer engineering",

            "computer applications"
        ],

        "engineering": [

            "engineering",

            "engineer"
        ]
    }

    required_groups = []

    for group, keywords in degree_groups.items():

        if any(
            keyword in job_description
            for keyword in keywords
        ):

            required_groups.append(
                group
            )

    if not required_groups:
        return 100

    matched_groups = 0

    for group in required_groups:

        keywords = degree_groups[
            group
        ]

        if any(
            keyword in resume_text
            for keyword in keywords
        ):

            matched_groups += 1

    score = (
        matched_groups
        / len(required_groups)
    ) * 100

    return round(
        score,
        2
    )


# =========================================================
# 6. REQUIRED EXPERIENCE
# =========================================================

def extract_required_experience(
    job_description
):
    """
    Extracts required years of experience
    from a job description.

    Examples:
        2-4 years
        2 to 4 years
        2+ years
        at least 2 years
        minimum of 2 years
        2 years of experience
    """

    if not job_description:
        return None

    text = job_description.lower()

    # -----------------------------------------------------
    # Example: 2-4 years
    # Example: 2 to 4 years
    # -----------------------------------------------------

    range_matches = re.findall(
        r"(\d+)\s*(?:-|–|to)\s*(\d+)"
        r"\s*(?:years?|yrs?)",
        text
    )

    if range_matches:

        return max(
            int(start)
            for start, end in range_matches
        )

    # -----------------------------------------------------
    # Example: 2+ years
    # -----------------------------------------------------

    plus_matches = re.findall(
        r"(\d+)\s*\+\s*"
        r"(?:years?|yrs?)",
        text
    )

    if plus_matches:

        return max(
            int(year)
            for year in plus_matches
        )

    # -----------------------------------------------------
    # Example: at least 2 years
    # Example: minimum of 2 years
    # Example: min 2 years
    # -----------------------------------------------------

    at_least_matches = re.findall(
        r"(?:at least|minimum of|min)"
        r"\s+(\d+)\s*"
        r"(?:years?|yrs?)",
        text
    )

    if at_least_matches:

        return max(
            int(year)
            for year in at_least_matches
        )

    # -----------------------------------------------------
    # Example: 2 years of experience
    # Example: 2 years experience
    # -----------------------------------------------------

    simple_matches = re.findall(
        r"(\d+)\s*"
        r"(?:years?|yrs?)"
        r"(?:\s+of)?\s+experience",
        text
    )

    if simple_matches:

        return max(
            int(year)
            for year in simple_matches
        )

    return None


# =========================================================
# 7. RESUME EXPERIENCE
# =========================================================

def calculate_resume_experience(
    resume_text
):
    """
    Estimates experience from resume text.

    Explicit year statements are checked first.
    Internship experience is treated as approximately
    one year for this prototype.
    """

    if not resume_text:
        return 0

    text = resume_text.lower()

    # -----------------------------------------------------
    # Explicit experience
    # -----------------------------------------------------

    year_matches = re.findall(
        r"(\d+)\s*"
        r"(?:years?|yrs?)",
        text
    )

    if year_matches:

        return max(
            int(year)
            for year in year_matches
        )

    # -----------------------------------------------------
    # Internship
    # -----------------------------------------------------

    if (
        "internship" in text
        or "intern" in text
        or "interned" in text
    ):

        return 1

    # -----------------------------------------------------
    # Fresh graduate
    # -----------------------------------------------------

    if (
        "fresh graduate" in text
        or "recent graduate" in text
        or "fresher" in text
    ):

        return 0

    return 0


# =========================================================
# 8. EXPERIENCE SCORE
# =========================================================

def calculate_experience_score(
    resume_text,
    job_description
):
    """
    Compares detected resume experience
    with job experience requirements.
    """

    if not job_description:
        return 100

    jd = job_description.lower()

    # -----------------------------------------------------
    # Fresher / entry-level roles
    # -----------------------------------------------------

    fresher_keywords = [

        "fresher",

        "freshers",

        "entry level",

        "entry-level",

        "graduate role",

        "recent graduate",

        "0-1 years",

        "0 to 1 years",

        "0-2 years",

        "0 to 2 years",

        "0 - 1 years",

        "0 - 2 years",

        "no experience",

        "graduates welcome",

        "fresh graduates"
    ]

    if any(
        keyword in jd
        for keyword in fresher_keywords
    ):

        return 100

    # -----------------------------------------------------
    # Find required experience
    # -----------------------------------------------------

    required_years = extract_required_experience(
        jd
    )

    if required_years is None:
        return 100

    # -----------------------------------------------------
    # Find resume experience
    # -----------------------------------------------------

    resume_years = calculate_resume_experience(
        resume_text
    )

    # -----------------------------------------------------
    # Compare
    # -----------------------------------------------------

    if resume_years >= required_years:
        return 100

    if required_years == 0:
        return 100

    if resume_years == 0:
        return 0

    score = (
        resume_years
        / required_years
    ) * 100

    return round(
        min(score, 100),
        2
    )


# =========================================================
# 9. OVERALL ATS SCORE
# =========================================================

def calculate_overall_ats_score(
    skill_score,
    keyword_score,
    similarity_score,
    structure_score,
    education_score,
    experience_score
):
    """
    Calculates the final ATS-style score.

    Weights:

        Skill Match      = 35%
        Keyword Match    = 15%
        JD Similarity    = 20%
        Structure        = 10%
        Education        = 10%
        Experience       = 10%

        Total            = 100%
    """

    overall_score = (

        skill_score * 0.35

        + keyword_score * 0.15

        + similarity_score * 0.20

        + structure_score * 0.10

        + education_score * 0.10

        + experience_score * 0.10
    )

    return round(
        overall_score,
        2
    )


# =========================================================
# 10. SCORE LEVEL
# =========================================================

def get_score_level(
    score
):
    """
    Converts numerical ATS score
    into a descriptive alignment level.
    """

    if score >= 80:

        return "Strong Alignment"

    if score >= 65:

        return "Good Alignment"

    if score >= 50:

        return "Moderate Alignment"

    if score >= 35:

        return "Needs Improvement"

    return "Low Alignment"