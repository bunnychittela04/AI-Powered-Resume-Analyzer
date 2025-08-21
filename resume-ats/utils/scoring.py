from __future__ import annotations
from typing import Dict, Set

def coverage_metrics(resume_terms: Set[str], jd_terms: Set[str]) -> Dict[str, float]:
    if not jd_terms:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0, "overlap": 0}
    overlap = len(resume_terms & jd_terms)
    precision = overlap / max(len(resume_terms), 1)
    recall = overlap / len(jd_terms)
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
    return {"precision": precision, "recall": recall, "f1": f1, "overlap": overlap}

def combined_score(semantic_sim: float, f1: float, w_sem: float = 0.6, w_kw: float = 0.4) -> float:
    # Weighted sum of semantic similarity and keyword F1
    score = w_sem * semantic_sim + w_kw * f1
    # Convert to percentage
    return max(0.0, min(100.0, score * 100.0))
