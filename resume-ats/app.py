from __future__ import annotations
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from utils.extract_text import extract_text_from_upload, allowed_file
from utils.nlp_utils import extract_skills, tfidf_semantic_similarity, jd_keywords, normalize_text
from utils.scoring import coverage_metrics, combined_score

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")
app.config["MAX_CONTENT_LENGTH"] = 4 * 1024 * 1024  # 4 MB

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # Validate inputs
    if "resume" not in request.files:
        flash("Please upload a resume file.")
        return redirect(url_for("index"))
    file = request.files["resume"]
    jd_text = request.form.get("jd", "").strip()
    if not file or file.filename == "":
        flash("Please choose a resume file.")
        return redirect(url_for("index"))
    if not jd_text:
        flash("Please paste a Job Description (JD).")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash("Unsupported file type. Upload .pdf, .docx or .txt.")
        return redirect(url_for("index"))
    # Extract resume text
    text, err = extract_text_from_upload(file, file.filename)
    if err:
        flash(err)
        return redirect(url_for("index"))

    resume_text = normalize_text(text)
    jd_text_norm = normalize_text(jd_text)

    # Skills & keywords
    resume_skills = sorted(extract_skills(resume_text))
    jd_terms = jd_keywords(jd_text_norm)

    # Coverage metrics
    cov = coverage_metrics(set(resume_skills), jd_terms)
    kw_f1 = cov["f1"]

    # Semantic similarity
    semantic_sim = tfidf_semantic_similarity(resume_text, jd_text_norm)

    # Combined score (0-100)
    score = combined_score(semantic_sim, kw_f1, w_sem=0.6, w_kw=0.4)

    # Missing terms
    missing = sorted(list(jd_terms - set(resume_skills)))

    return render_template(
        "result.html",
        score=score,
        semantic_sim=semantic_sim,
        kw_f1=kw_f1,
        overlap=cov["overlap"],
        resume_skills=resume_skills,
        jd_terms=sorted(jd_terms),
        missing=missing,
    )

if __name__ == "__main__":
    app.run(debug=True)
