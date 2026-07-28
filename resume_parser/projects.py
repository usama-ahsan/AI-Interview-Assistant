"""
resume_parser/projects.py

Extracts a "Projects" section from resume text and splits it into
individual project entries (title + description).
"""

import re

# Headings that commonly follow a Projects section on a resume -- used
# as stop points so we don't grab content from later sections.
NEXT_SECTION_HEADINGS = [
    "education", "experience", "work experience", "employment",
    "skills", "certifications", "achievements", "publications",
    "references", "languages", "interests", "extracurricular",
    "awards", "volunteer", "volunteering",
]

SECTION_PATTERN = re.compile(
    r"(?im)^\s*projects?\s*:?\s*$"
)


def extract_projects(text: str) -> list[dict]:
    """
    Find a "Projects" section and split it into individual entries.

    Args:
        text: raw resume text

    Returns:
        List of {"title": str, "description": str} dicts, in the order
        they appear. Returns an empty list if no Projects section is found.
    """
    lines = text.splitlines()
    start_idx = None

    for i, line in enumerate(lines):
        if SECTION_PATTERN.match(line.strip()):
            start_idx = i + 1
            break
        # Also catch "Projects" as an inline heading like "PROJECTS" with
        # trailing content stripped by strip().
        if line.strip().lower() in ("projects", "project", "projects:", "key projects"):
            start_idx = i + 1
            break

    if start_idx is None:
        return []

    end_idx = len(lines)
    for i in range(start_idx, len(lines)):
        stripped = lines[i].strip().lower().rstrip(":")
        if stripped in NEXT_SECTION_HEADINGS:
            end_idx = i
            break

    block_lines = [l for l in lines[start_idx:end_idx] if l.strip()]
    return _parse_project_entries(block_lines)


def _parse_project_entries(block_lines: list[str]) -> list[dict]:
    """Turn raw lines from a Projects section into structured entries."""
    projects = []
    for raw_line in block_lines:
        entry = raw_line.strip("-•*\t ").strip()
        if not entry:
            continue

        title, description = _split_title_description(entry)
        projects.append({"title": title.strip(), "description": description.strip()})

    return projects


def _split_title_description(entry: str) -> tuple[str, str]:
    """Split a single project line into (title, description) using the
    first colon or em-dash/hyphen separator; falls back to the whole
    line as the title if no separator is found."""
    for separator in (":", " – ", " - ", "-"):
        if separator in entry:
            title, _, description = entry.partition(separator)
            if title.strip():
                return title, description
    return entry, ""


if __name__ == "__main__":
    sample = """
    Projects:
    AI Resume Screener: Built a tool using Python and scikit-learn to rank resumes
    Portfolio Website - Personal site built with React and CSS

    Education
    BS Computer Science
    """
    print(extract_projects(sample))
