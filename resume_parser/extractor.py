"""
resume_parser/extractor.py

Extracts name, email, and phone number from raw resume text.
"""

import re

EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

# Matches phone numbers with optional country code, spaces, dashes, dots,
# parentheses. Requires at least 9 digits total to avoid matching random
# short number sequences (e.g. a graduation year).
PHONE_PATTERN = re.compile(
    r"(\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}"
)

# Lines that are clearly section headers, not names -- used to skip past
# them when guessing the candidate's name from the top of the resume.
SECTION_HEADERS = {
    "resume", "cv", "curriculum vitae", "profile", "summary",
    "contact", "contact information", "personal information",
}


def extract_email(text: str) -> str | None:
    """Return the first email address found in the text, or None."""
    match = EMAIL_PATTERN.search(text)
    return match.group(0) if match else None


def extract_phone(text: str) -> str | None:
    """Return the first plausible phone number found in the text, or None."""
    for match in PHONE_PATTERN.finditer(text):
        candidate = match.group(0)
        digit_count = sum(c.isdigit() for c in candidate)
        if digit_count >= 9:
            return candidate.strip()
    return None


def extract_name(text: str) -> str | None:
    """
    Best-effort guess at the candidate's name: the first non-empty line
    that isn't an email, phone number, URL, or common section header.
    Works for the common "name at the very top" resume layout; may fail
    on heavily designed/columnar resume templates.
    """
    for raw_line in text.strip().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.lower() in SECTION_HEADERS:
            continue
        if EMAIL_PATTERN.search(line):
            continue
        if "http" in line.lower() or "www." in line.lower():
            continue
        if sum(c.isdigit() for c in line) >= 4:
            continue
        # A name is short, a few words, mostly alphabetic
        word_count = len(line.split())
        if 1 <= word_count <= 5 and len(line) <= 60:
            return line
    return None


def extract_contact_info(text: str) -> dict:
    """
    Extract name, email, and phone from resume text.

    Returns (matches the project's data contract):
        {"name": str | None, "email": str | None, "phone": str | None}
    """
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
    }


if __name__ == "__main__":
    sample = """Usama Ahsan
    abc@gmail.com | +92 300 1234567
    """
    print(extract_contact_info(sample))
