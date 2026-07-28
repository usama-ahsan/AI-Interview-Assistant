"""
resume_parser/skills.py
PERSON A OWNS THIS FILE

Matches known skill keywords against resume text. This is a keyword
matcher, not an ML model -- simple, fast, and predictable, which is
appropriate for an MVP. It can be swapped for an NER model later
without changing its function signature.
"""

import re

# Grouped for maintainability; extraction itself treats them as one flat list.
PROGRAMMING_LANGUAGES = [
    "python", "java", "javascript", "typescript", "c++", "c#", "c",
    "go", "golang", "rust", "ruby", "php", "swift", "kotlin", "r", "scala",
]

WEB_FRAMEWORKS = [
    "react", "angular", "vue", "django", "flask", "fastapi", "express",
    "next.js", "node.js", "streamlit", "spring", "spring boot", ".net",
]

DATA_ML = [
    "machine learning", "deep learning", "nlp", "natural language processing",
    "computer vision", "pytorch", "tensorflow", "keras", "scikit-learn",
    "sklearn", "pandas", "numpy", "matplotlib", "sbert", "bert",
    "hugging face", "huggingface", "opencv", "xgboost",
]

DATABASES = [
    "sql", "mysql", "postgresql", "postgres", "mongodb", "sqlite",
    "redis", "oracle", "firebase", "dynamodb",
]

DEVOPS_CLOUD = [
    "docker", "kubernetes", "aws", "azure", "gcp", "google cloud",
    "ci/cd", "jenkins", "terraform", "linux", "git", "github", "gitlab",
]

OTHER = [
    "html", "css", "rest api", "graphql", "agile", "scrum", "tableau",
    "power bi", "excel", "jira",
]

KNOWN_SKILLS = sorted(
    set(PROGRAMMING_LANGUAGES + WEB_FRAMEWORKS + DATA_ML + DATABASES + DEVOPS_CLOUD + OTHER),
    key=len,
    reverse=True,  # match longer phrases first (e.g. "machine learning" before "machine")
)


def extract_skills(text: str) -> list[str]:
    """
    Find known skills mentioned in resume text.

    Args:
        text: raw resume text

    Returns:
        Sorted, de-duplicated list of matched skill names (lowercase).
        Matching is word-boundary aware so "r" doesn't match inside "art",
        and "c" doesn't match inside "science".
    """
    text_lower = text.lower()
    found = set()

    for skill in KNOWN_SKILLS:
        # Escape special regex chars (e.g. "c++", ".net") then use word
        # boundaries so short skills like "r", "c", "go" don't false-match
        # inside unrelated words.
        pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"
        if re.search(pattern, text_lower):
            found.add(skill)

    return sorted(found)


if __name__ == "__main__":
    sample = "Skilled in Python, SQL, React, and Machine Learning. Familiar with Docker and AWS."
    print(extract_skills(sample))
