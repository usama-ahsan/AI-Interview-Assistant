"""
question_generator/generator.py

Takes structured resume data (contract output of resume_parser) and
produces a list of interview questions (contract input for backend/frontend).
"""

from question_generator.templates import (
    SKILL_TEMPLATES,
    PROJECT_TEMPLATE,
    GENERIC_SKILL_TEMPLATE,
)

MAX_QUESTIONS = 15  # keep interviews from becoming unreasonably long


def generate_questions(resume_data: dict, max_questions: int = MAX_QUESTIONS) -> dict:
    """
    Generate interview questions from structured resume data.

    Args:
        resume_data: {
            "name": str, "email": str, "phone": str,
            "skills": [str, ...],
            "projects": [{"title": str, "description": str}, ...]
        }
        max_questions: cap on the total number of questions returned

    Returns:
        {"questions": [
            {"id": int, "question": str, "type": "skill"|"project",
             "reference_answer": str}
        ]}
        Returns {"questions": []} if resume_data has no skills or projects.
    """
    questions = []
    qid = 1

    for skill in resume_data.get("skills", []):
        template = SKILL_TEMPLATES.get(skill)
        if template is None:
            template = {
                "question": GENERIC_SKILL_TEMPLATE["question"].format(skill=skill),
                "reference_answer": GENERIC_SKILL_TEMPLATE["reference_answer"].format(skill=skill),
            }
        questions.append({
            "id": qid,
            "question": template["question"],
            "type": "skill",
            "reference_answer": template["reference_answer"],
        })
        qid += 1

    for project in resume_data.get("projects", []):
        title = project.get("title", "").strip()
        if not title:
            continue
        questions.append({
            "id": qid,
            "question": PROJECT_TEMPLATE.format(title=title),
            "type": "project",
            "reference_answer": project.get("description", ""),
        })
        qid += 1

    return {"questions": questions[:max_questions]}


if __name__ == "__main__":
    sample_resume_data = {
        "name": "Ali Raza",
        "email": "ali.raza@email.com",
        "phone": "+92 300 1234567",
        "skills": ["python", "sql", "kubernetes"],  # kubernetes has no template -> generic fallback
        "projects": [{"title": "AI Resume Screener", "description": "Built with Python and scikit-learn"}],
    }
    import json
    print(json.dumps(generate_questions(sample_resume_data), indent=2))
