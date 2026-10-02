import re


# =========================================================
# CLEAN TEXT
# =========================================================

def clean_text(text):
    """
    Cleans extracted resume or job description text.

    Keeps meaningful line breaks because they are useful
    for resume section detection.
    """

    if not text:
        return ""

    text = str(text)

    # -----------------------------------------------------
    # Normalize line endings
    # -----------------------------------------------------

    text = text.replace(
        "\r\n",
        "\n"
    )

    text = text.replace(
        "\r",
        "\n"
    )

    # -----------------------------------------------------
    # Replace non-breaking spaces
    # -----------------------------------------------------

    text = text.replace(
        "\u00a0",
        " "
    )

    # -----------------------------------------------------
    # Normalize dash characters
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # Normalize tabs and multiple spaces
    # -----------------------------------------------------

    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    # -----------------------------------------------------
    # Remove spaces from otherwise empty lines
    # -----------------------------------------------------

    text = re.sub(
        r"\n[ \t]+",
        "\n",
        text
    )

    # -----------------------------------------------------
    # Normalize excessive blank lines
    # -----------------------------------------------------

    text = re.sub(
        r"\n\s*\n+",
        "\n\n",
        text
    )

    # -----------------------------------------------------
    # Remove leading/trailing whitespace
    # -----------------------------------------------------

    return text.strip()


# =========================================================
# NORMALIZE TEXT FOR MATCHING
# =========================================================

def normalize_for_matching(text):
    """
    Normalizes text for keyword and skill matching.

    This function keeps the text readable while making
    common skill variations consistent.
    """

    if not text:
        return ""

    text = str(text).lower()

    # -----------------------------------------------------
    # Normalize dash characters
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # Common skill variations
    # -----------------------------------------------------

    replacements = {

        # Power BI
        "power-bi": "power bi",
        "powerbi": "power bi",

        # Scikit-learn
        "scikit learn": "scikit-learn",
        "sklearn": "scikit-learn",

        # Generative AI
        "gen-ai": "generative ai",
        "genai": "generative ai",

        # Problem solving
        "problem-solving": "problem solving",

        # A/B testing
        "a-b testing": "a/b testing",
        "ab testing": "a/b testing",

        # K-Means
        "kmeans": "k-means",
        "k means": "k-means",

        # MongoDB
        "mongo db": "mongodb",

        # JavaScript
        "java script": "javascript",

        # TypeScript
        "type script": "typescript",

        # Data visualization
        "data visualisation": "data visualization",

        # Web scraping
        "web scrapping": "web scraping",
    }

    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )

    # -----------------------------------------------------
    # Normalize whitespace
    # -----------------------------------------------------

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# NORMALIZE LIST ITEM
# =========================================================

def normalize_line(line):
    """
    Cleans a single resume line.
    """

    if not line:
        return ""

    line = str(line)

    line = line.replace(
        "\u00a0",
        " "
    )

    line = re.sub(
        r"[ \t]+",
        " ",
        line
    )

    return line.strip()


# =========================================================
# SPLIT INTO CLEAN LINES
# =========================================================

def get_clean_lines(text):
    """
    Converts text into a list of clean, non-empty lines.

    Useful for resume section parsing.
    """

    if not text:
        return []

    text = clean_text(
        text
    )

    if not text:
        return []

    lines = text.split(
        "\n"
    )

    clean_lines = []

    for line in lines:

        line = normalize_line(
            line
        )

        if line:

            clean_lines.append(
                line
            )

    return clean_lines