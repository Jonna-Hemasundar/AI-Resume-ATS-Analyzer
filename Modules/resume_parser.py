import re


# =========================================================
# STANDARD RESUME SECTION NAMES
# =========================================================

SECTION_PATTERNS = {

    "summary": [
        "summary",
        "professional summary",
        "career objective",
        "objective",
        "career profile",
        "professional profile",
        "profile",
        "about me",
        "about",
    ],

    "experience": [
        "work experience",
        "professional experience",
        "employment history",
        "employment",
        "work history",
        "career history",
        "experience",
        "internship",
        "internships",
        "work",
    ],

    "education": [
        "education",
        "educational background",
        "academic background",
        "academic qualifications",
        "qualifications",
        "education background",
        "academic history",
    ],

    "skills": [
        "skills",
        "technical skills",
        "core skills",
        "key skills",
        "professional skills",
        "technical expertise",
        "expertise",
        "competencies",
        "core competencies",
        "areas of expertise",
        "technical knowledge",
    ],

    "projects": [
        "projects",
        "project experience",
        "academic projects",
        "personal projects",
        "professional projects",
        "key projects",
        "selected projects",
    ],

    "certifications": [
        "certifications",
        "certificates",
        "professional certifications",
        "licenses certifications",
        "licenses and certifications",
        "certification",
    ],

    "achievements": [
        "achievements",
        "accomplishments",
        "awards",
        "honors",
        "honours",
    ],

    "languages": [
        "languages",
        "language skills",
        "languages known",
    ],

    "interests": [
        "interests",
        "hobbies",
        "hobbies and interests",
        "personal interests",
    ],

    "references": [
        "references",
        "professional references",
    ],
}


# =========================================================
# HEADING LOOKUP
# =========================================================

HEADING_LOOKUP = {}

for section, patterns in SECTION_PATTERNS.items():

    for pattern in patterns:

        HEADING_LOOKUP[
            pattern
        ] = section


# =========================================================
# TEXT NORMALIZATION
# =========================================================

def normalize_text(text):
    """
    Cleans PDF-extracted resume text while preserving
    line breaks.

    Parameters
    ----------
    text : str
        Raw PDF text.

    Returns
    -------
    str
        Normalized text.
    """

    if not text:
        return ""

    text = str(text)

    # Normalize line endings
    text = text.replace(
        "\r\n",
        "\n"
    )

    text = text.replace(
        "\r",
        "\n"
    )

    # Replace non-breaking spaces
    text = text.replace(
        "\u00a0",
        " "
    )

    # Normalize different dash characters
    text = text.replace(
        "–",
        "-"
    )

    text = text.replace(
        "—",
        "-"
    )

    text = text.replace(
        "−",
        "-"
    )

    lines = text.split("\n")

    cleaned_lines = []

    for line in lines:

        # Normalize multiple spaces
        line = re.sub(
            r"[ \t]+",
            " ",
            line
        )

        line = line.strip()

        if line:
            cleaned_lines.append(
                line
            )

    return "\n".join(
        cleaned_lines
    )


# =========================================================
# NORMALIZE HEADING
# =========================================================

def normalize_heading(heading):
    """
    Converts a possible section heading into a
    standard comparable format.
    """

    if not heading:
        return ""

    heading = str(
        heading
    ).lower().strip()

    # Remove bullets / decorative symbols / numbering
    heading = re.sub(
        r"^[\s\-\*\u2022\u00b7\d\.\)\(]+",
        "",
        heading
    )

    # Remove punctuation
    heading = re.sub(
        r"[^a-z0-9& ]",
        "",
        heading
    )

    # Normalize spaces
    heading = re.sub(
        r"\s+",
        " ",
        heading
    )

    return heading.strip()


# =========================================================
# COLLAPSE SPACED HEADINGS
# =========================================================

def collapse_spaced_heading(line):
    """
    Detects headings where every character is separated.

    Example
    -------
    C A R E E R O B J E C T I V E
    ->
    CAREEROBJECTIVE

    W O R K E X P E R I E N C E
    ->
    WORKEXPERIENCE
    """

    if not line:
        return ""

    words = line.strip().split()

    if len(words) < 2:
        return line.strip()

    # Every token must be one alphabetic character
    if all(
        len(word) == 1
        and word.isalpha()
        for word in words
    ):

        joined = "".join(words)

        if len(joined) <= 60:
            return joined

    return line.strip()


# =========================================================
# HEADING VARIATIONS
# =========================================================

def get_heading_variations(line):
    """
    Generates multiple normalized versions of a line.

    This helps handle different PDF resume heading formats.
    """

    if not line:
        return set()

    variations = set()

    original = line.strip()

    # Normal heading
    normalized = normalize_heading(
        original
    )

    if normalized:
        variations.add(
            normalized
        )

    # Spaced heading
    collapsed = collapse_spaced_heading(
        original
    )

    collapsed_normalized = normalize_heading(
        collapsed
    )

    if collapsed_normalized:
        variations.add(
            collapsed_normalized
        )

    # Remove spaces for comparison
    if normalized:
        variations.add(
            normalized.replace(
                " ",
                ""
            )
        )

    if collapsed_normalized:
        variations.add(
            collapsed_normalized.replace(
                " ",
                ""
            )
        )

    return variations


# =========================================================
# IDENTIFY SECTION
# =========================================================

def identify_section(line):
    """
    Identifies whether a line is a resume section heading.

    Returns
    -------
    str or None
        Section name if detected.
    """

    if not line:
        return None

    variations = get_heading_variations(
        line
    )

    for pattern, section in HEADING_LOOKUP.items():

        pattern_normalized = normalize_heading(
            pattern
        )

        pattern_without_spaces = (
            pattern_normalized.replace(
                " ",
                ""
            )
        )

        if (
            pattern_normalized in variations
            or pattern_without_spaces in variations
        ):
            return section

    return None


# =========================================================
# EXPERIENCE CONTENT DETECTION
# =========================================================

def looks_like_experience(line):
    """
    Checks whether a line looks like a work experience entry.
    """

    if not line:
        return False

    lower_line = line.lower()

    experience_words = [
        "analyst",
        "developer",
        "engineer",
        "manager",
        "intern",
        "consultant",
        "associate",
        "specialist",
        "designer",
        "trainee",
        "administrator",
        "executive",
        "architect",
        "scientist",
    ]

    has_experience_word = any(
        word in lower_line
        for word in experience_words
    )

    # Examples:
    # June 2026 - August 2026
    # 2024 - 2025
    # 2023 - Present
    date_pattern = re.search(
        r"\b(?:19|20)\d{2}"
        r"\s*-\s*"
        r"(?:"
        r"(?:19|20)\d{2}"
        r"|present"
        r"|current"
        r")\b",
        lower_line
    )

    # Month + year format
    month_year_pattern = re.search(
        r"\b("
        r"january|february|march|april|may|june|"
        r"july|august|september|october|november|december|"
        r"jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec"
        r")"
        r"\s+\d{4}",
        lower_line
    )

    return (
        has_experience_word
        and (
            date_pattern is not None
            or month_year_pattern is not None
        )
    )


# =========================================================
# EDUCATION CONTENT DETECTION
# =========================================================

def looks_like_education(line):
    """
    Checks whether a line looks like education information.
    """

    if not line:
        return False

    lower_line = line.lower()

    education_terms = [
        "b.tech",
        "btech",
        "b.e",
        "b.e.",
        "bachelor",
        "master",
        "m.tech",
        "mtech",
        "m.e",
        "m.e.",
        "mba",
        "degree",
        "university",
        "college",
        "graduation",
        "graduate",
        "intermediate",
        "secondary education",
        "school",
        "cgpa",
        "gpa",
    ]

    return any(
        term in lower_line
        for term in education_terms
    )


# =========================================================
# CONTENT BASED DETECTION
# =========================================================

def detect_section_from_content(line):
    """
    Attempts to detect a section from its content.

    This is used only as a fallback when a clear heading
    is not available.
    """

    if not line:
        return None

    if looks_like_experience(line):
        return "experience"

    if looks_like_education(line):
        return "education"

    return None


# =========================================================
# SECTION CONTENT CLEANING
# =========================================================

def clean_section_content(content):
    """
    Cleans extracted lines belonging to a section.
    """

    if not content:
        return ""

    cleaned_lines = []

    for line in content:

        line = line.strip()

        if not line:
            continue

        # Normalize excessive spaces
        line = re.sub(
            r"\s+",
            " ",
            line
        )

        cleaned_lines.append(
            line
        )

    return "\n".join(
        cleaned_lines
    ).strip()


# =========================================================
# PARSE RESUME SECTIONS
# =========================================================

def parse_resume_sections(text):
    """
    Parses a resume into logical sections.

    Parameters
    ----------
    text : str
        Extracted resume text.

    Returns
    -------
    dict
        Example:

        {
            "summary": "...",
            "experience": "...",
            "education": "...",
            "skills": "...",
            "projects": "...",
            "certifications": "..."
        }
    """

    text = normalize_text(
        text
    )

    if not text:
        return {}

    lines = text.split(
        "\n"
    )

    sections = {}

    current_section = None

    # =====================================================
    # PROCESS EVERY LINE
    # =====================================================

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # -------------------------------------------------
        # 1. Check for explicit section heading
        # -------------------------------------------------

        section = identify_section(
            line
        )

        if section:

            current_section = section

            if current_section not in sections:

                sections[
                    current_section
                ] = []

            continue

        # -------------------------------------------------
        # 2. Content-based fallback
        # -------------------------------------------------

        content_section = detect_section_from_content(
            line
        )

        # Only use content detection when we don't
        # already have an explicit section.
        #
        # This prevents a date/job line inside one section
        # from accidentally switching the parser.

        if (
            current_section is None
            and content_section
        ):

            current_section = content_section

            if current_section not in sections:

                sections[
                    current_section
                ] = []

        # -------------------------------------------------
        # 3. Store content
        # -------------------------------------------------

        if current_section:

            sections[
                current_section
            ].append(
                line
            )


    # =====================================================
    # CLEAN FINAL SECTIONS
    # =====================================================

    final_sections = {}

    for section, content in sections.items():

        cleaned_content = clean_section_content(
            content
        )

        if cleaned_content:

            final_sections[
                section
            ] = cleaned_content


    return final_sections


# =========================================================
# GET SECTION
# =========================================================

def get_section(
    sections,
    section_name
):
    """
    Safely retrieves a particular resume section.
    """

    if not sections:
        return ""

    if not section_name:
        return ""

    section_name = (
        section_name
        .lower()
        .strip()
    )

    return sections.get(
        section_name,
        ""
    )


# =========================================================
# GET AVAILABLE SECTIONS
# =========================================================

def get_available_sections(sections):
    """
    Returns the list of sections detected in the resume.
    """

    if not sections:
        return []

    return list(
        sections.keys()
    )


# =========================================================
# CHECK REQUIRED SECTIONS
# =========================================================

def get_missing_standard_sections(sections):
    """
    Identifies common resume sections that were not detected.
    """

    standard_sections = [
        "summary",
        "experience",
        "education",
        "skills",
        "projects",
        "certifications",
    ]

    if not sections:
        return standard_sections

    return [
        section
        for section in standard_sections
        if section not in sections
    ]