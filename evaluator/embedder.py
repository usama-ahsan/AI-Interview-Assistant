"""
evaluator/embedder.py

Wraps a Sentence-BERT model to turn text into embeddings (vectors that
capture semantic meaning, not just word overlap). This is the real
model -- 'all-MiniLM-L6-v2' is small, fast on CPU, and a standard
starting point for semantic similarity tasks.

The model is loaded once, lazily, on first use (not at import time),
so importing this module stays fast, and app startup isn't blocked
until scoring is actually needed.
"""

from functools import lru_cache

MODEL_NAME = "all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def _get_model():
    """Load and cache the SBERT model. lru_cache ensures it's loaded
    only once even if this function is called many times."""
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(MODEL_NAME)


def get_embeddings(texts: list[str]):
    """
    Convert a list of texts into SBERT embeddings.

    Args:
        texts: list of strings to embed

    Returns:
        A numpy array of shape (len(texts), embedding_dim)
    """
    model = _get_model()
    return model.encode(texts, convert_to_numpy=True)


if __name__ == "__main__":
    vectors = get_embeddings(["hello world", "hi there"])
    print("Shape:", vectors.shape)
