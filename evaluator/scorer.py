"""
evaluator/scorer.py

Scores a candidate's answer against the reference answer using cosine
similarity between their SBERT embeddings.
"""

from sklearn.metrics.pairwise import cosine_similarity
from evaluator.embedder import get_embeddings


def score_answer(user_answer: str, reference_answer: str) -> float:
    """
    Compare a candidate's answer to the reference (ideal) answer.

    Args:
        user_answer: the candidate's typed answer
        reference_answer: the ideal/expected answer for the question

    Returns:
        A similarity score between 0.0 and 1.0, rounded to 3 decimals.
        Returns 0.0 immediately if user_answer is empty/whitespace-only,
        without calling the model (saves compute on empty submissions).
    """
    if not user_answer or not user_answer.strip():
        return 0.0
    if not reference_answer or not reference_answer.strip():
        # No reference to compare against -- can't meaningfully score
        return 0.0

    vectors = get_embeddings([user_answer, reference_answer])
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]

    # Cosine similarity can be slightly outside [0, 1] due to floating
    # point; clamp defensively so downstream code always gets a clean range.
    similarity = max(0.0, min(1.0, float(similarity)))
    return round(similarity, 3)


if __name__ == "__main__":
    ref = "Overfitting happens when a model learns noise instead of the pattern."
    good = "Overfitting is when the model memorizes training noise rather than generalizing."
    bad = "I like using Python for web development."
    print("Good answer score:", score_answer(good, ref))
    print("Bad answer score:", score_answer(bad, ref))
    print("Empty answer score:", score_answer("", ref))
