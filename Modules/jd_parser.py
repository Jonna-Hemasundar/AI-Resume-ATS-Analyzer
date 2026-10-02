from Modules.skill_extractor import extract_skills


def extract_jd_skills(job_description):
    """
    Extracts technical, analytical, business, and soft skills
    from the provided Job Description.

    Parameters
    ----------
    job_description : str
        Full text of the job description.

    Returns
    -------
    dict
        Skills grouped by category.
    """

    if not job_description:
        return {}

    if not isinstance(job_description, str):
        raise TypeError(
            "Job description must be a string."
        )

    job_description = job_description.strip()

    if not job_description:
        return {}

    skills = extract_skills(
        job_description
    )

    return skills