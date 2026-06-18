# TruthRank AI

## Intelligent Candidate Discovery & Ranking Engine

TruthRank AI is an AI-powered recruitment intelligence system developed for the Redrob Data & AI Challenge. The system goes beyond traditional keyword matching by understanding candidate profiles semantically and ranking candidates using a hybrid scoring framework.

The objective is to identify candidates who genuinely fit a role based on experience, skills, career trajectory, behavioral signals, trust indicators, and availability rather than simple keyword overlap.

---

# Problem Statement

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching. This often leads to:

* High-quality candidates being missed
* Irrelevant candidates being ranked highly
* Recruiters spending significant time reviewing unsuitable profiles
* Poor matching between job requirements and candidate capabilities

The Redrob challenge requires building an intelligent ranking engine that can understand both the job description and candidate profiles to generate recruiter-trustworthy recommendations.

---

# Dataset Overview

The solution was built using the Redrob candidate dataset containing:

* 100,000 candidate profiles
* Career history
* Skills and endorsements
* Certifications
* Education records
* Platform behavioral signals
* Recruiter engagement metrics
* Availability indicators

Dataset Characteristics:

* Total Candidates: 100,000
* Filtered Candidates: 1,179
* Final Ranked Candidates: 100

---

# Solution Architecture

Job Description

↓

JD Parsing & Understanding

↓

Semantic Embedding Generation

↓

Fast Candidate Pre-Filtering

↓

Feature Extraction

↓

Hybrid Scoring Engine

├── Semantic Match Score

├── Career Fit Score

├── Product Experience Score

├── Behavioral Score

├── Availability Score

├── Trust Score

└── Honeypot Detection

↓

Hybrid Ranking Engine

↓

Explainability Layer

↓

Top-100 Candidate Recommendations

↓

final_submission.csv

---

# Core Components

## 1. Fast Candidate Pre-Filtering

The first stage reduces the search space by filtering candidates using role relevance and experience signals.

Input:

* 100,000 candidates

Output:

* 1,179 shortlisted candidates

Benefits:

* Faster execution
* Reduced embedding computations
* Lower memory usage

---

## 2. Semantic Matching Engine

TruthRank AI uses:

BAAI/bge-small-en-v1.5

through Sentence Transformers to generate embeddings for:

* Job descriptions
* Candidate profiles

Cosine similarity is used to compute semantic alignment.

This allows the system to identify relevant candidates even when exact keywords do not match.

Example:

A candidate who built recommendation systems may still rank highly even if they never explicitly mention "RAG" or "Pinecone".

---

## 3. Career Fit Scoring

Career Fit evaluates:

* AI Engineering Experience
* Machine Learning Experience
* Search Infrastructure Experience
* Retrieval Systems Experience
* Ranking Systems Experience
* Recommendation Systems Experience

This component captures domain relevance beyond semantic similarity.

---

## 4. Product Experience Scoring

Product Experience rewards candidates who have worked on:

* Production ML systems
* Search systems
* Recommendation engines
* Retrieval pipelines
* Large-scale engineering platforms

The goal is to prioritize engineers who have deployed systems rather than only studying them.

---

## 5. Behavioral Scoring

Behavior signals indicate recruiter readiness.

Signals considered:

* Recruiter response rate
* Interview completion rate
* Profile completeness
* GitHub activity

Behavioral signals help identify candidates who are actively engaged and likely to respond.

---

## 6. Availability Scoring

Availability measures:

* Open-to-work status
* Notice period
* Platform activity

Candidates who are more likely to join quickly receive a higher score.

---

## 7. Trust Score

Trust Score evaluates profile credibility using:

* Verified email
* Verified phone
* Profile completeness
* Recruiter engagement metrics

The objective is to reduce low-quality or suspicious profiles.

---

## 8. Honeypot Detection

The challenge dataset contains intentionally misleading candidates.

TruthRank AI detects suspicious profiles using:

* Unrealistic title-skill combinations
* Keyword stuffing patterns
* Role inconsistency checks

These candidates receive penalties during ranking.

---

## 9. Explainability Layer

Recruiters need to understand why a candidate was recommended.

TruthRank AI generates human-readable explanations such as:

"Senior NLP Engineer shows strong semantic alignment with the role. Direct experience in retrieval, ranking, search or AI systems. Demonstrated production-scale ML experience."

This improves recruiter trust and transparency.

---

# Hybrid Ranking Formula

Final ranking combines:

* Semantic Match Score
* Career Fit Score
* Product Experience Score
* Behavioral Score
* Availability Score
* Trust Score Bonus
* Honeypot Penalty

The ranking engine balances relevance, experience, availability, and credibility.

---

# Results

Dataset Size:

100,000 Candidates

Filtered Candidates:

1,179 Candidates

Top Candidate Categories:

* Senior NLP Engineers
* Senior Machine Learning Engineers
* AI Engineers
* Search Engineers
* Applied ML Engineers
* Data Scientists

Example Top Results:

1. Senior NLP Engineer
2. Senior Machine Learning Engineer
3. Senior AI Engineer
4. Staff Machine Learning Engineer
5. AI Engineer

---

# Runtime Performance

Environment:

* AMD Ryzen 5 5500U
* 8GB RAM
* Windows 11
* Python 3.11

Performance:

* Candidate Pool: 100,000
* Filtered Pool: 1,179
* CPU-only execution
* Memory usage below challenge limits

---

# Output Files

## final_submission.csv

Contains:

* candidate_id
* rank
* score
* reasoning

Submission-ready output.

---

## candidate_explanations.csv

Contains:

* candidate_id
* title
* score
* explanation

Provides recruiter-friendly explanations for rankings.

---

# Repository Structure

TruthRankAI/

├── data/

├── outputs/

├── models/

├── src/

│ ├── loaders/

│ ├── parsers/

│ ├── filters/

│ ├── scoring/

│ ├── ranking/

│ ├── explainability/

│ └── submission/

├── requirements.txt

├── README.md

├── submission_metadata.yaml

├── validate_final_submission.py

└── validate_candidate_ids.py

---

# Installation

Clone Repository

git clone YOUR_GITHUB_REPOSITORY

cd TruthRankAI

Install Dependencies

pip install -r requirements.txt

---

# Reproducing Submission

Generate Rankings

python -m src.ranking.rank_large_dataset_v2

Output:

outputs/final_submission.csv

Validate Submission

python validate_final_submission.py

python validate_candidate_ids.py

---

# AI Tools Used

* ChatGPT

AI tools were used for brainstorming, code assistance, documentation support, and architecture discussions.

All implementation, debugging, testing, and integration work was performed by the project author.

---

# Future Improvements

* Learning-to-Rank Models
* Dynamic Weight Optimization
* FAISS Vector Search
* Real-Time Candidate Ranking API
* SHAP Explainability
* Recruiter Feedback Learning Loop

---

# Author

Vivek Vardhan Vandana

B.Tech Computer Science & Engineering (Data Science)

Maharaj Vijayaram Gajapathi Raj College of Engineering

Redrob Data & AI Challenge Submission

TruthRank AI
