import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# TEXT PREPARATION
# =========================================================

def prepare_text(text):
    """
    Prepares resume/JD text for TF-IDF similarity analysis.
    """

    if not text:
        return ""

    text = str(text)

    # Normalize line breaks
    text = text.replace(
        "\r\n",
        "\n"
    )

    text = text.replace(
        "\r",
        "\n"
    )

    # Normalize common PDF characters
    text = text.replace(
        "\u00a0",
        " "
    )

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

    # Normalize common skill variations
    replacements = {
        "power-bi": "power bi",
        "powerbi": "power bi",
        "scikit learn": "scikit-learn",
        "gen-ai": "generative ai",
        "genai": "generative ai",
        "problem-solving": "problem solving",
        "a-b testing": "a/b testing",
        "ab testing": "a/b testing",
        "kmeans": "k-means",
        "k means": "k-means",
    }

    text = text.lower()

    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )

    # Replace excessive whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# CALCULATE TF-IDF SIMILARITY
# =========================================================

def calculate_similarity_score(
    resume_text,
    job_description
):
    """
    Calculates semantic/content similarity between
    a resume and a job description using TF-IDF
    and cosine similarity.

    Parameters
    ----------
    resume_text : str
        Extracted resume text.

    job_description : str
        Job description text.

    Returns
    -------
    float
        Similarity score from 0 to 100.
    """

    # =====================================================
    # 1. VALIDATE INPUT
    # =====================================================

    if not resume_text or not job_description:

        return 0.0

    resume_text = prepare_text(
        resume_text
    )

    job_description = prepare_text(
        job_description
    )

    if not resume_text or not job_description:

        return 0.0


    # =====================================================
    # 2. CREATE DOCUMENTS
    # =====================================================

    documents = [
        resume_text,
        job_description
    ]


    # =====================================================
    # 3. CREATE TF-IDF VECTORIZER
    # =====================================================

    vectorizer = TfidfVectorizer(

        stop_words="english",

        # Unigrams + bigrams
        ngram_range=(1, 2),

        # Prevent unnecessarily large vocabulary
        max_features=5000,

        # Ignore extremely rare terms
        min_df=1
    )


    # =====================================================
    # 4. CALCULATE TF-IDF
    # =====================================================

    try:

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )

    except ValueError:

        # Happens when there are no usable terms
        return 0.0


    # =====================================================
    # 5. CALCULATE COSINE SIMILARITY
    # =====================================================

    try:

        similarity = cosine_similarity(

            tfidf_matrix[0:1],

            tfidf_matrix[1:2]

        )[0][0]

    except Exception:

        return 0.0


    # =====================================================
    # 6. CONVERT TO PERCENTAGE
    # =====================================================

    score = similarity * 100


    # =====================================================
    # 7. KEEP SCORE BETWEEN 0 AND 100
    # =====================================================

    score = max(
        0.0,
        min(
            score,
            100.0
        )
    )


    return round(
        score,
        2
    )