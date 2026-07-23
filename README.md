# AI-Interview-Assistant
## Overview
AI Interview Assistant is a deep learning-based web application that analyzes a candidate's resume, generates personalized interview questions, evaluates answers using a fine-tuned Sentence-BERT model, and provides detailed feedback and a final interview report.

---

## Features

- Resume Upload (PDF)
- Resume Parsing
- Skill Extraction
- Interview Question Generation
- Answer Evaluation
- Semantic Similarity Scoring (SBERT)
- AI Feedback
- Final Interview Report

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI

### Deep Learning
- PyTorch
- Sentence Transformers

### Resume Parsing
- PyMuPDF

### Database
- SQLite

---

## Project Structure

```text
AI-Interview-Assistant/

backend/
frontend/
resume_parser/
training/
models/
datasets/
reports/
utils/
tests/

README.md
requirements.txt
app.py
```

---

## Installation

```bash
git clone <repository-url>
cd AI-Interview-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

## Run

```bash
streamlit run app.py
```

---

## Future Work

- Voice Interview
- LLM Feedback
- Adaptive Interview Difficulty
- Multi-language Support
- Cloud Deployment

---

## Contributors

- Usama Ahsan
- Amna Noor

---

## License

MIT License
