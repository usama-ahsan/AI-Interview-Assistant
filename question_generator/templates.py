"""
question_generator/templates.py

Question + reference-answer templates, keyed by skill name (must match
the skill names produced by resume_parser/skills.py exactly).
"""

SKILL_TEMPLATES = {
    "python": {
        "question": "Can you explain the difference between a list and a tuple in Python?",
        "reference_answer": (
            "Lists are mutable and defined with square brackets, while tuples "
            "are immutable and defined with parentheses. Tuples are generally "
            "faster and used for fixed collections of data."
        ),
    },
    "java": {
        "question": "What is the difference between an interface and an abstract class in Java?",
        "reference_answer": (
            "An interface only declares method signatures (no implementation, "
            "prior to Java 8 default methods) and supports multiple inheritance. "
            "An abstract class can have both implemented and unimplemented "
            "methods and a class can only extend one abstract class."
        ),
    },
    "javascript": {
        "question": "What is the difference between '==' and '===' in JavaScript?",
        "reference_answer": (
            "'==' compares values after type coercion, while '===' compares "
            "both value and type without coercion, making it stricter and "
            "generally safer to use."
        ),
    },
    "sql": {
        "question": "What is the difference between INNER JOIN and LEFT JOIN in SQL?",
        "reference_answer": (
            "INNER JOIN returns only rows with matching values in both tables, "
            "while LEFT JOIN returns all rows from the left table and matched "
            "rows from the right table, with NULLs where there is no match."
        ),
    },
    "machine learning": {
        "question": "What is overfitting and how can you prevent it?",
        "reference_answer": (
            "Overfitting happens when a model learns noise in the training "
            "data instead of the underlying pattern, hurting generalization "
            "to new data. It can be prevented with regularization, "
            "cross-validation, more training data, or simpler models."
        ),
    },
    "deep learning": {
        "question": "What is the vanishing gradient problem?",
        "reference_answer": (
            "It occurs when gradients become extremely small during "
            "backpropagation through many layers, causing early layers to "
            "learn very slowly or stop learning. Techniques like ReLU "
            "activations, batch normalization, and residual connections help."
        ),
    },
    "react": {
        "question": "What is the purpose of the useEffect hook in React?",
        "reference_answer": (
            "useEffect lets you run side effects like data fetching, "
            "subscriptions, or manual DOM updates after render, and can clean "
            "up after itself using a returned cleanup function."
        ),
    },
    "django": {
        "question": "What is the difference between Django's ORM and raw SQL queries?",
        "reference_answer": (
            "Django's ORM lets you interact with the database using Python "
            "objects and methods instead of writing raw SQL, providing "
            "database abstraction, security against SQL injection, and "
            "portability across database backends."
        ),
    },
    "docker": {
        "question": "What is the difference between a Docker image and a Docker container?",
        "reference_answer": (
            "An image is a read-only template with the application code and "
            "dependencies. A container is a running instance of that image, "
            "with its own writable layer."
        ),
    },
    "git": {
        "question": "What is the difference between 'git merge' and 'git rebase'?",
        "reference_answer": (
            "Merge combines branches by creating a new merge commit and "
            "preserves full history, while rebase replays commits on top of "
            "another branch, producing a linear history but rewriting commit "
            "hashes."
        ),
    },
    "aws": {
        "question": "What is the difference between EC2 and Lambda on AWS?",
        "reference_answer": (
            "EC2 provides virtual servers you manage and pay for continuously, "
            "suited for long-running applications. Lambda is serverless, runs "
            "code in response to events, and you only pay for actual execution "
            "time."
        ),
    },
    "nlp": {
        "question": "What is the difference between stemming and lemmatization?",
        "reference_answer": (
            "Stemming crudely chops word endings using rules, which can "
            "produce non-words. Lemmatization uses vocabulary and grammar "
            "rules to return the proper base (dictionary) form of a word."
        ),
    },
}

PROJECT_TEMPLATE = (
    "Tell me more about your project '{title}'. What was your specific "
    "contribution, and what challenges did you face?"
)

# Fallback question used when a matched skill has no dedicated template yet,
# so the pipeline never silently drops a skill.
GENERIC_SKILL_TEMPLATE = {
    "question": "Can you describe your experience working with {skill}?",
    "reference_answer": (
        "A strong answer should mention specific projects or tasks where "
        "{skill} was used, the problem it solved, and the outcome."
    ),
}
