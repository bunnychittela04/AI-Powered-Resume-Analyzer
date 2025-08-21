# AI-Powered Resume Analyzer (ATS Optimizer)

## 📌 Project Overview
The **AI-Powered Resume Analyzer** is a web-based tool designed to evaluate resumes against job descriptions using **Natural Language Processing (NLP)** techniques.  
It helps job seekers improve their **ATS (Applicant Tracking System)** score by highlighting missing keywords, analyzing skills, and providing an overall match percentage.  

---

## 🚀 Features
- 📄 **Resume Upload**: Upload resumes in `.pdf` or `.docx` format.
- 📝 **Job Description Input**: Paste or upload the target job description.
- 🔍 **ATS Match Score**: Calculates a match percentage between the resume and job description.
- 📊 **Keyword Analysis**: Identifies missing important keywords from the resume.
- 📈 **Skills & Strengths Breakdown**: Shows strengths and improvement areas.
- 🖼 **User-Friendly Dashboard**: Clean, simple, and responsive UI.
- 💡 **AI Suggestions**: Suggests improvements to make the resume ATS-friendly.

---

## 🛠 Tech Stack
| Technology     | Purpose |
|----------------|---------|
| **Python 3.x** | Backend processing |
| **Flask** | Web framework |
| **spaCy / NLTK** | NLP processing |
| **scikit-learn** | Text similarity calculations |
| **PDFMiner / docx2txt** | Resume text extraction |
| **Bootstrap / HTML / CSS** | Frontend styling |
| **JavaScript** | Client-side interactivity |

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
