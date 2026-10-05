# 🤖 AI Resume & ATS Analyzer

An AI-powered **Resume & ATS Analyzer** built with Python and Streamlit that helps job seekers evaluate their resumes against a specific job description.

The application analyzes the resume, extracts relevant information, compares it with the job requirements, and generates an **ATS compatibility score** along with useful insights for improving the resume.

## 🚀 Live Demo

👉 [AI Resume & ATS Analyzer](https://ai-resume-ats-analyzer-jgyqbsojjvmgccfcjaw9eb.streamlit.app/)

---

## 📌 Project Overview

Applicant Tracking Systems (ATS) are commonly used by companies to filter and rank resumes before they reach recruiters.

This project helps candidates understand how well their resume matches a particular job description by analyzing:

* Skills
* Keywords
* Resume structure
* Education
* Experience
* Job-description similarity
* Missing skills and keywords

The goal is to provide a simple and automated way to identify areas where a resume can be improved before applying for a job.

---

## ✨ Features

### 📄 Resume Upload

* Upload your resume in **PDF format**
* Extract text automatically from the uploaded document

### 🧹 Text Processing

* Clean and preprocess resume text
* Remove unnecessary formatting/noise
* Normalize text for analysis

### 🧠 Resume Parsing

Extracts important resume information such as:

* Skills
* Education
* Experience
* Keywords
* Relevant sections

### 📋 Job Description Analysis

Enter or paste a job description to identify:

* Required skills
* Important keywords
* Job-related terms
* Relevant requirements

### 📊 ATS Scoring

The application calculates an overall ATS score using multiple components:

| Component         | Weight |
| ----------------- | -----: |
| Skill Match       |    40% |
| Keyword Match     |    20% |
| TF-IDF Similarity |    20% |
| Resume Structure  |    10% |
| Education         |     5% |
| Experience        |     5% |

### 🔍 Skill Matching

Compares the skills mentioned in the resume with the skills required by the job description.

### 🔑 Keyword Matching

Identifies important keywords from the job description and checks whether they are present in the resume.

### 📐 TF-IDF Similarity

Uses **TF-IDF (Term Frequency–Inverse Document Frequency)** to measure the textual similarity between the resume and job description.

### 📑 Resume Structure Analysis

Checks whether important resume sections are present and properly structured.

### 🎓 Education & Experience Analysis

Evaluates education and experience information against the requirements mentioned in the job description.

### 💡 Improvement Insights

Provides useful feedback based on the analysis, helping candidates identify missing skills, keywords, and resume improvements.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Framework

* Streamlit

### Natural Language Processing

* spaCy
* Scikit-learn
* TF-IDF

### PDF Processing

* PyMuPDF (`fitz`)

### Data Processing

* Python
* Regular Expressions

### Deployment

* Streamlit Community Cloud

---

## 📂 Project Structure

```text
AI Resume & ATS Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
└── Modules/
    ├── pdf_parser.py
    ├── text_cleaner.py
    ├── resume_parser.py
    ├── skill_extractor.py
    └── jd_parser.py
```

---

## ⚙️ How It Works

```text
        Resume PDF
             │
             ▼
      PDF Text Extraction
             │
             ▼
       Text Cleaning
             │
             ▼
       Resume Parsing
             │
             ▼
      Skill Extraction
             │
             │
             ▼
      Job Description
             │
             ▼
      JD Skill Extraction
             │
             ▼
      Resume vs JD Analysis
             │
      ┌──────┼─────────┐
      ▼      ▼         ▼
   Skills Keywords  TF-IDF
   Match   Match   Similarity
      │      │         │
      └──────┼─────────┘
             ▼
        ATS Score
             │
             ▼
      Improvement Tips
```

---

## 🧮 ATS Score Calculation

The overall ATS score is calculated using a weighted scoring approach:

```text
ATS Score =
    Skill Match × 40%
  + Keyword Match × 20%
  + TF-IDF Similarity × 20%
  + Structure × 10%
  + Education × 5%
  + Experience × 5%
```

This approach combines both **keyword-based analysis** and **text similarity analysis** rather than relying on a single metric.

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Resume-ATS-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd "AI Resume & ATS Analyzer"
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the environment

**Windows:**

```bash
env\Scripts\activate
```

**Linux / macOS:**

```bash
source env/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install the spaCy model

```bash
python -m spacy download en_core_web_sm
```

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

The project uses libraries including:

```text
streamlit
pandas
scikit-learn
spacy
PyMuPDF
```

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Example Use Case

Suppose a candidate wants to apply for a **Data Analyst** position.

The candidate can:

1. Upload their resume.
2. Paste the Data Analyst job description.
3. Run the analysis.
4. View the ATS score.
5. Check matched skills.
6. Identify missing skills and keywords.
7. Improve the resume accordingly.

For example, if the job description requires:

```text
Python
SQL
Power BI
Excel
Pandas
Data Analysis
```

and the resume contains:

```text
Python
SQL
Excel
Pandas
```

the analyzer can identify **Power BI** and **Data Analysis** as potentially missing or insufficiently represented skills.

---

## 🔐 Privacy

The application is designed to analyze the resume and job description provided by the user for generating the analysis.

Users should avoid uploading documents containing unnecessary sensitive personal information.

---

## 🚧 Future Improvements

Planned improvements include:

* [ ] Better resume section detection
* [ ] More advanced skill extraction
* [ ] Improved keyword matching
* [ ] Resume formatting analysis
* [ ] Job-role-specific recommendations
* [ ] Resume improvement suggestions
* [ ] Downloadable ATS analysis report
* [ ] Support for additional document formats
* [ ] Improved handling of different resume layouts
* [ ] More advanced NLP-ba
