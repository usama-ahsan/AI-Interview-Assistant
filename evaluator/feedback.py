"""
evaluator/feedback.py

Turns a numeric similarity score into human-readable feedback text.
"""

STRONG_THRESHOLD = 0.70
PARTIAL_THRESHOLD = 0.45


def generate_feedback(score: float) -> str:
    """
    Args:
        score: similarity score between 0.0 and 1.0

    Returns:
        A short, honest, encouraging feedback message.
    """
    if score >= STRONG_THRESHOLD:
        return "Strong answer — covers the key concepts well."
    elif score >= PARTIAL_THRESHOLD:
        return "Partial answer — you're on the right track but missed some key points."
    elif score > 0:
        return "Weak answer — consider reviewing this topic and comparing with the reference answer."
    else:
        return "No answer detected — please provide a response to this question."


if __name__ == "__main__":
    for s in (0.9, 0.5, 0.2, 0.0):
        print(s, "->", generate_feedback(s))
