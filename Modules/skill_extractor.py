import re


# =========================================================
# SKILL DATABASE
# =========================================================

SKILL_ALIASES = {

    # =====================================================
    # PROGRAMMING
    # =====================================================

    "python": [
        "python"
    ],

    "java": [
        "java"
    ],

    "javascript": [
        "javascript",
        "java script"
    ],

    "typescript": [
        "typescript",
        "type script"
    ],

    "c++": [
        "c++"
    ],

    "r programming": [
        "r programming",
        "r language"
    ],


    # =====================================================
    # DATA ANALYSIS
    # =====================================================

    "pandas": [
        "pandas"
    ],

    "numpy": [
        "numpy"
    ],

    "matplotlib": [
        "matplotlib"
    ],

    "seaborn": [
        "seaborn"
    ],

    "scipy": [
        "scipy"
    ],

    "excel": [
        "excel",
        "microsoft excel",
        "ms excel"
    ],

    "advanced excel": [
        "advanced excel"
    ],

    "data analysis": [
        "data analysis",
        "data analytics",
        "data analyst",
        "data analysis and analytics"
    ],

    "data cleaning": [
        "data cleaning",
        "data cleansing"
    ],

    "data preprocessing": [
        "data preprocessing",
        "preprocessing"
    ],

    "data validation": [
        "data validation"
    ],

    "data visualization": [
        "data visualization",
        "data visualisation"
    ],

    "eda": [
        "eda",
        "exploratory data analysis"
    ],

    "exploratory data analysis": [
        "exploratory data analysis",
        "eda"
    ],


    # =====================================================
    # DATABASE
    # =====================================================

    "sql": [
        "sql",
        "structured query language"
    ],

    "mysql": [
        "mysql"
    ],

    "postgresql": [
        "postgresql",
        "postgres"
    ],

    "mongodb": [
        "mongodb",
        "mongo db"
    ],

    "oracle": [
        "oracle database",
        "oracle"
    ],

    "database": [
        "database",
        "databases"
    ],

    "joins": [
        "joins",
        "sql joins"
    ],

    "subqueries": [
        "subqueries",
        "subqueries in sql",
        "sub queries"
    ],

    "aggregations": [
        "aggregations",
        "sql aggregations",
        "data aggregation"
    ],


    # =====================================================
    # BUSINESS INTELLIGENCE
    # =====================================================

    "power bi": [
        "power bi",
        "power-bi",
        "powerbi"
    ],

    "tableau": [
        "tableau"
    ],

    "looker": [
        "looker"
    ],

    "qlik": [
        "qlik",
        "qlik sense"
    ],

    "dax": [
        "dax"
    ],

    "power query": [
        "power query"
    ],

    "business intelligence": [
        "business intelligence",
        "business intelligence tools"
    ],


    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    "machine learning": [
        "machine learning",
        "ml"
    ],

    "scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],

    "supervised learning": [
        "supervised learning"
    ],

    "unsupervised learning": [
        "unsupervised learning"
    ],

    "regression": [
        "regression"
    ],

    "linear regression": [
        "linear regression"
    ],

    "logistic regression": [
        "logistic regression"
    ],

    "polynomial regression": [
        "polynomial regression"
    ],

    "classification": [
        "classification",
        "classifier",
        "classification algorithms"
    ],

    "clustering": [
        "clustering",
        "cluster analysis"
    ],

    "k-means": [
        "k-means",
        "kmeans",
        "k means"
    ],

    "knn": [
        "knn",
        "k-nearest neighbors",
        "k nearest neighbors"
    ],

    "random forest": [
        "random forest",
        "random forest classifier",
        "random forest regression"
    ],

    "decision tree": [
        "decision tree",
        "decision trees"
    ],

    "svm": [
        "svm",
        "support vector machine",
        "support vector machines"
    ],

    "naive bayes": [
        "naive bayes"
    ],

    "predictive modeling": [
        "predictive modeling",
        "predictive analytics"
    ],


    # =====================================================
    # STATISTICS
    # =====================================================

    "statistics": [
        "statistics",
        "statistical analysis"
    ],

    "statistical analysis": [
        "statistical analysis",
        "statistics"
    ],

    "probability": [
        "probability",
        "probability theory"
    ],

    "hypothesis testing": [
        "hypothesis testing"
    ],

    "a/b testing": [
        "a/b testing",
        "ab testing",
        "a-b testing",
        "split testing"
    ],

    "descriptive statistics": [
        "descriptive statistics"
    ],

    "inferential statistics": [
        "inferential statistics"
    ],


    # =====================================================
    # ARTIFICIAL INTELLIGENCE
    # =====================================================

    "artificial intelligence": [
        "artificial intelligence"
    ],

    "deep learning": [
        "deep learning",
        "dl"
    ],

    "tensorflow": [
        "tensorflow"
    ],

    "pytorch": [
        "pytorch"
    ],

    "keras": [
        "keras"
    ],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "natural language processing": [
        "natural language processing",
        "nlp"
    ],

    "generative ai": [
        "generative ai",
        "genai",
        "gen-ai"
    ],

    "llm": [
        "llm",
        "llms",
        "large language model",
        "large language models"
    ],

    "rag": [
        "rag",
        "retrieval augmented generation",
        "retrieval-augmented generation"
    ],

    "transformers": [
        "transformers",
        "transformer"
    ],


    # =====================================================
    # DATA ENGINEERING
    # =====================================================

    "etl": [
        "etl",
        "extract transform load",
        "extract transform and load"
    ],

    "data pipeline": [
        "data pipeline",
        "data pipelines"
    ],

    "apache spark": [
        "apache spark",
        "spark"
    ],

    "hadoop": [
        "hadoop"
    ],

    "airflow": [
        "airflow",
        "apache airflow"
    ],


    # =====================================================
    # CLOUD
    # =====================================================

    "aws": [
        "aws",
        "amazon web services"
    ],

    "azure": [
        "azure",
        "microsoft azure"
    ],

    "google cloud": [
        "google cloud",
        "google cloud platform",
        "gcp"
    ],


    # =====================================================
    # TOOLS
    # =====================================================

    "git": [
        "git"
    ],

    "github": [
        "github"
    ],

    "jupyter": [
        "jupyter",
        "jupyter notebook"
    ],

    "google colab": [
        "google colab",
        "colab"
    ],

    "streamlit": [
        "streamlit"
    ],

    "visual studio code": [
        "visual studio code",
        "vs code"
    ],


    # =====================================================
    # WEB SCRAPING
    # =====================================================

    "web scraping": [
        "web scraping",
        "web scrapping"
    ],

    "data extraction": [
        "data extraction"
    ],

    "beautifulsoup": [
        "beautifulsoup",
        "beautiful soup",
        "bs4"
    ],

    "requests": [
        "requests",
        "python requests"
    ],

    "selenium": [
        "selenium"
    ],


    # =====================================================
    # BUSINESS ANALYSIS
    # =====================================================

    "business analysis": [
        "business analysis",
        "business analytics",
        "business analyst"
    ],

    "business analyst": [
        "business analyst",
        "business analysis",
        "business analytics"
    ],

    "requirements gathering": [
        "requirements gathering",
        "requirement gathering",
        "requirements analysis",
        "requirement analysis"
    ],

    "stakeholder management": [
        "stakeholder management",
        "stakeholder communication"
    ],

    "stakeholder communication": [
        "stakeholder communication",
        "stakeholder management"
    ],


    # =====================================================
    # SOFT SKILLS
    # =====================================================

    "communication": [
        "communication",
        "communication skills",
        "verbal communication",
        "written communication"
    ],

    "problem solving": [
        "problem solving",
        "problem-solving",
        "analytical problem solving"
    ],

    "teamwork": [
        "teamwork",
        "team work",
        "team collaboration"
    ],

    "leadership": [
        "leadership",
        "leadership skills"
    ],

    "analytical thinking": [
        "analytical thinking",
        "analytical skills"
    ],

    "critical thinking": [
        "critical thinking"
    ],

    "time management": [
        "time management"
    ]
}


# =========================================================
# SKILL CATEGORIES
# =========================================================

SKILL_CATEGORIES = {

    "Programming": [
        "python",
        "java",
        "javascript",
        "typescript",
        "c++",
        "r programming"
    ],

    "Data Analysis": [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
        "excel",
        "advanced excel",
        "data analysis",
        "data cleaning",
        "data preprocessing",
        "data validation",
        "data visualization",
        "eda",
        "exploratory data analysis"
    ],

    "Database": [
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "oracle",
        "database",
        "joins",
        "subqueries",
        "aggregations"
    ],

    "Business Intelligence": [
        "power bi",
        "tableau",
        "looker",
        "qlik",
        "dax",
        "power query",
        "business intelligence"
    ],

    "Machine Learning": [
        "machine learning",
        "scikit-learn",
        "supervised learning",
        "unsupervised learning",
        "regression",
        "linear regression",
        "logistic regression",
        "polynomial regression",
        "classification",
        "clustering",
        "k-means",
        "knn",
        "random forest",
        "decision tree",
        "svm",
        "naive bayes",
        "predictive modeling"
    ],

    "Statistics": [
        "statistics",
        "statistical analysis",
        "probability",
        "hypothesis testing",
        "a/b testing",
        "descriptive statistics",
        "inferential statistics"
    ],

    "Artificial Intelligence": [
        "artificial intelligence",
        "deep learning",
        "tensorflow",
        "pytorch",
        "keras",
        "nlp",
        "natural language processing",
        "generative ai",
        "llm",
        "rag",
        "transformers"
    ],

    "Data Engineering": [
        "etl",
        "data pipeline",
        "apache spark",
        "hadoop",
        "airflow"
    ],

    "Cloud": [
        "aws",
        "azure",
        "google cloud"
    ],

    "Tools": [
        "git",
        "github",
        "jupyter",
        "google colab",
        "streamlit",
        "visual studio code"
    ],

    "Web Scraping": [
        "web scraping",
        "data extraction",
        "beautifulsoup",
        "requests",
        "selenium"
    ],

    "Business": [
        "business analysis",
        "business analyst",
        "requirements gathering",
        "stakeholder management",
        "stakeholder communication"
    ],

    "Soft Skills": [
        "communication",
        "problem solving",
        "teamwork",
        "leadership",
        "analytical thinking",
        "critical thinking",
        "time management"
    ]
}


# =========================================================
# TEXT NORMALIZATION
# =========================================================

def normalize_text(text):
    """
    Normalizes text for reliable skill matching.
    """

    if not text:
        return ""

    text = str(text).lower()

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

        "mongo db": "mongodb",

        "java script": "javascript",

        "type script": "typescript",

        "data visualisation": "data visualization",

        "web scrapping": "web scraping"
    }

    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )

    # Normalize whitespace

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# REGEX ESCAPE / BOUNDARY MATCH
# =========================================================

def contains_skill(
    text,
    skill
):
    """
    Checks whether a skill exists in text.

    Uses word boundaries where possible so that
    short skills such as 'r' or 'ai' do not
    create excessive false positives.
    """

    if not text or not skill:
        return False

    text = normalize_text(text)
    skill = normalize_text(skill)

    # Special handling for symbols / phrases

    escaped_skill = re.escape(skill)

    # Phrase or standalone matching

    pattern = rf"(?<![a-zA-Z0-9]){escaped_skill}(?![a-zA-Z0-9])"

    return bool(
        re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )
    )


# =========================================================
# CANONICAL SKILL
# =========================================================

def get_canonical_skill(
    detected_skill
):
    """
    Converts an alias into its canonical skill name.
    """

    detected_skill = normalize_text(
        detected_skill
    )

    for canonical, aliases in SKILL_ALIASES.items():

        if detected_skill == normalize_text(
            canonical
        ):
            return canonical

        for alias in aliases:

            if detected_skill == normalize_text(
                alias
            ):
                return canonical

    return detected_skill


# =========================================================
# EXTRACT SKILLS
# =========================================================

def extract_skills(text):
    """
    Extracts skills from resume text or job description.

    Returns:
        {
            "Programming": [...],
            "Data Analysis": [...],
            ...
        }
    """

    if not text:
        return {}

    normalized_text = normalize_text(
        text
    )

    detected_skills = {}

    for category, skills in SKILL_CATEGORIES.items():

        category_skills = []

        for skill in skills:

            aliases = SKILL_ALIASES.get(
                skill,
                [skill]
            )

            found = False

            # Check canonical skill and aliases

            for alias in aliases:

                if contains_skill(
                    normalized_text,
                    alias
                ):

                    found = True
                    break

            if found:

                if skill not in category_skills:

                    category_skills.append(
                        skill
                    )

        if category_skills:

            detected_skills[
                category
            ] = category_skills

    return detected_skills


# =========================================================
# FLATTEN SKILLS
# =========================================================

def flatten_skills(
    skills_dict
):
    """
    Converts categorized skills into a single list.
    """

    if not skills_dict:
        return []

    result = []

    for skills in skills_dict.values():

        for skill in skills:

            if skill not in result:

                result.append(
                    skill
                )

    return result