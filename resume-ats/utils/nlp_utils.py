from __future__ import annotations
import re
from typing import List, Set, Dict, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    import spacy
    _NLP = spacy.load("en_core_web_sm")
except Exception:
    # Fallback tokenizer if spaCy model not present yet.
    import spacy
    _NLP = spacy.blank("en")
    if "sentencizer" not in _NLP.pipe_names:
        _NLP.add_pipe("sentencizer")

from .skills import SINGLE_WORD_SKILLS, PHRASE_SKILLS

_WORD_RE = re.compile(r"[a-zA-Z][a-zA-Z\+\-\./#]*")

def normalize_text(text: str) -> str:
    return (text or "").lower()

def tokenize_lemmas(text: str) -> List[str]:
    doc = _NLP(text)
    tokens = []
    for t in doc:
        if t.is_space or t.is_punct:
            continue
        # Use lemma if available, else text
        lemma = (t.lemma_ if t.lemma_ != "-PRON-" else t.text).lower()
        if _WORD_RE.fullmatch(lemma):
            tokens.append(lemma)
    return tokens

def extract_skills(text: str) -> Set[str]:
    """Extract both single-word and phrase skills from text."""
    txt = normalize_text(text)
    found: Set[str] = set()

    # Phrase match (simple substring search)
    for phrase in PHRASE_SKILLS:
        if phrase in txt:
            found.add(phrase)

    # Token-based single-word match
    tokens = set(tokenize_lemmas(txt))
    for s in SINGLE_WORD_SKILLS:
        if s in tokens:
            found.add(s)
    return found

def tfidf_semantic_similarity(a: str, b: str) -> float:
    """Return cosine similarity between two strings using TF-IDF ngrams."""
    vect = TfidfVectorizer(ngram_range=(1,2), stop_words="english", min_df=1)
    X = vect.fit_transform([a, b])
    sim = cosine_similarity(X[0:1], X[1:2])[0,0]
    return float(sim)

def jd_keywords(text: str) -> Set[str]:
    """Heuristic JD keyword extraction: return skills + top unigrams that look like tech terms."""
    # Start with curated skills
    base = set(extract_skills(text))

    # Add TF-IDF top terms by training on JD alone (hack: split into sentences as docs)
    sents = [s.text for s in _NLP(text).sents] or [text]
    vect = TfidfVectorizer(ngram_range=(1,2), stop_words="english", min_df=1, max_features=50)
    X = vect.fit_transform(sents)
    terms = vect.get_feature_names_out().tolist()

    # Keep only token-like words, drop very short terms
    for t in terms:
        tt = t.strip().lower()
        if len(tt) >= 3 and _WORD_RE.fullmatch(tt):
            base.add(tt)
    return base
