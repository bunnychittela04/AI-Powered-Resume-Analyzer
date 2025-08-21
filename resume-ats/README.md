# AI-Powered Resume Analyzer (ATS Optimizer)

A minimal Flask app that compares a candidate's resume to a Job Description (JD) using NLP + TF-IDF semantic similarity and keyword coverage, producing an ATS-like match score and suggestions for missing keywords.

## Quickstart (VS Code)

1. **Download / Open**
   - Open this folder in VS Code.

2. **Create a virtual environment**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux (bash/zsh):**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. **Run the app**
   ```bash
   python app.py
   ```
   Then open http://127.0.0.1:5000/

5. **Use it**
   - Upload a resume file (`.pdf` / `.docx` / `.txt`)
   - Paste a Job Description (JD) into the text area
   - Get: match score, extracted skills, and missing keywords

## Project Structure

```
resume-ats/
├── app.py
├── requirements.txt
├── README.md
├── utils/
│   ├── __init__.py
│   ├── extract_text.py
│   ├── nlp_utils.py
│   ├── scoring.py
│   └── skills.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
└── static/
    └── style.css
```

## Notes
- The scoring uses a blend of **semantic similarity** (TF-IDF cosine) and **keyword coverage** (overlap with a curated skills list).
- You can extend the skills list in `utils/skills.py` or hook up a database.
- For a more advanced version, swap TF-IDF with sentence embeddings (e.g., `sentence-transformers`) and add authentication + history storage.
