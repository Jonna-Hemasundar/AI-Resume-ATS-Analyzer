from Modules.skill_extractor import (
    SKILL_ALIASES,
    normalize_text
)


# =========================================================
# NORMALIZE SKILL
# =========================================================

def normalize_skill(skill):
    """
    Normalizes an individual skill for comparison.
    """

    if not skill:
        return ""

    return normalize_text(
        skill
    ).strip()


# =========================================================
# BUILD RESUME SKILL SET
# =========================================================

def build_resume_skill_set(
    resume_skills
):
    """
    Converts categorized resume skills into
    one normalized searchable set.
    """

    resume_skill_set = set()

    if not resume_skills:
        return resume_skill_set

    for skills in resume_skills.values():

        if not skills:
            continue

        for skill in skills:

            normalized_skill = normalize_skill(
                skill
            )

            if normalized_skill:

                resume_skill_set.add(
                    normalized_skill
                )

    return resume_skill_set


# =========================================================
# CHECK DIRECT MATCH
# =========================================================

def direct_skill_match(
    required_skill,
    resume_skill_set
):
    """
    Checks whether the required skill directly
    exists in the resume skill set.
    """

    required_skill = normalize_skill(
        required_skill
    )

    return (
        required_skill in resume_skill_set
    )


# =========================================================
# CHECK ALIAS MATCH
# =========================================================

def alias_skill_match(
    required_skill,
    resume_skill_set
):
    """
    Checks whether any known alias of the
    required skill exists in the resume.
    """

    required_skill = normalize_skill(
        required_skill
    )

    aliases = SKILL_ALIASES.get(
        required_skill,
        [required_skill]
    )

    for alias in aliases:

        alias = normalize_skill(
            alias
        )

        if alias in resume_skill_set:
            return True

    return False


# =========================================================
# CHECK WHETHER SKILL EXISTS
# =========================================================

def contains_skill(
    text,
    skill
):
    """
    Checks whether a skill exists in arbitrary text.

    Uses boundary-aware matching to reduce false
    positives from short terms.
    """

    if not text or not skill:
        return False

    normalized_text = normalize_text(
        text
    )

    normalized_skill = normalize_skill(
        skill
    )

    if not normalized_skill:
        return False

    # -----------------------------------------------------
    # Phrase matching
    # -----------------------------------------------------

    if normalized_skill in normalized_text:
        return True

    return False


# =========================================================
# MATCH SKILLS
# =========================================================

def match_skills(
    resume_skills,
    jd_skills
):
    """
    Compares resume skills against skills detected
    from the job description.

    Parameters
    ----------
    resume_skills : dict
        Categorized skills extracted from the resume.

    jd_skills : dict
        Categorized skills extracted from the JD.

    Returns
    -------
    tuple
        (
            matched_skills,
            missing_skills
        )
    """

    matched_skills = {}
    missing_skills = {}

    # -----------------------------------------------------
    # Create searchable resume skill set
    # -----------------------------------------------------

    resume_skill_set = build_resume_skill_set(
        resume_skills
    )

    if not jd_skills:
        return (
            matched_skills,
            missing_skills
        )

    # -----------------------------------------------------
    # Compare every JD skill
    # -----------------------------------------------------

    for category, required_skills in jd_skills.items():

        if not required_skills:
            continue

        matched = []
        missing = []

        for required_skill in required_skills:

            required_normalized = normalize_skill(
                required_skill
            )

            if not required_normalized:
                continue

            # -------------------------------------------------
            # Direct match
            # -------------------------------------------------

            if direct_skill_match(
                required_normalized,
                resume_skill_set
            ):

                matched.append(
                    required_skill
                )

                continue

            # -------------------------------------------------
            # Alias match
            # -------------------------------------------------

            if alias_skill_match(
                required_normalized,
                resume_skill_set
            ):

                matched.append(
                    required_skill
                )

                continue

            # -------------------------------------------------
            # Missing skill
            # -------------------------------------------------

            missing.append(
                required_skill
            )

        # -----------------------------------------------------
        # Save category results
        # -----------------------------------------------------

        if matched:

            matched_skills[
                category
            ] = matched

        if missing:

            missing_skills[
                category
            ] = missing

    return (
        matched_skills,
        missing_skills
    )


# =========================================================
# FLATTEN MATCHED SKILLS
# =========================================================

def flatten_matched_skills(
    matched_skills
):
    """
    Converts categorized matched skills into a list.
    """

    result = []

    if not matched_skills:
        return result

    for skills in matched_skills.values():

        for skill in skills:

            if skill not in result:

                result.append(
                    skill
                )

    return result


# =========================================================
# FLATTEN MISSING SKILLS
# =========================================================

def flatten_missing_skills(
    missing_skills
):
    """
    Converts categorized missing skills into a list.
    """

    result = []

    if not missing_skills:
        return result

    for skills in missing_skills.values():

        for skill in skills:

            if skill not in result:

                result.append(
                    skill
                )

    return result