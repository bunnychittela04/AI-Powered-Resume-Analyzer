AI-Powered Resume Analyzer (ATS Optimizer)

A web application that analyzes resumes against job descriptions (similar to an Applicant Tracking System).
It uses Natural Language Processing (NLP) and TF-IDF to extract skills, match them against the job description, and calculate a match score with suggestions to improve.

🚀 Features

ATS-style Match Score — Percentage showing how closely a resume matches a job description.

Resume Skills Extraction — Detects relevant technical & soft skills from the uploaded resume.

JD Keywords Extraction — Extracts important keywords from the provided job description.

Missing Keywords Suggestions — Highlights terms from the JD missing in the resume.

Semantic Similarity Analysis — Uses NLP & TF-IDF to compare text meaning, not just exact matches.

📌 Tech Stack

Backend: Python, Flask

NLP Libraries: spaCy, scikit-learn (TF-IDF)

File Parsing: PyPDF2, docx2txt

Frontend: HTML, CSS, JavaScript

Deployment (optional): Heroku / Render

📂 How It Works

Upload Resume (.pdf / .docx / .txt)

Paste Job Description (JD)

The system:

Extracts text from the resume.

Cleans & tokenizes both texts.

Extracts relevant keywords & skills.

Calculates match score.

Identifies missing keywords.

Displays results with detailed skill comparison.

Output
<img width="1894" height="913" alt="Screenshot 2025-08-21 150144" src="https://github.com/user-attachments/assets/96e3b296-eb19-4e69-b802-569e87a432a2" />


Analysis Results

Example Results:

Match Score: 9.6%

Semantic Similarity: 10.3%

Keyword F1: 8.7%

Overlap: 2 terms

Detected Resume Skills:

data science, django, flask, git, javascript, linux, machine learning, mysql, nosql, numpy, oop, python, sqlite


Extracted JD Keywords:

academic, actively, activities, apply, aws, begin, better, campus, career, certifications, challenges, college, coming, completed, computer, consider, contribute, css, currently, design, developed, development, html, java, knowledge, new, opportunity, project, python, servicenow, sql, technical


Missing Keywords (Suggestions to Add):

academic, actively, apply, aws, challenges, college, css, html, java, servicenow, sql, technical, etc.

🛠 Installation & Setup
# Clone repository
git clone https://github.com/yourusername/resume-ats-optimizer.git
cd resume-ats-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py


The app will run on:

http://127.0.0.1:5000

📈 Future Enhancements

Add BERT embeddings for better semantic similarity.

Include charts & graphs for skill comparison.

Store user history in a database.

Multi-language resume support.
