CONFIG = {
    "data_path": "data/candidates.json",
    "jd_path": "data/job_description.txt",
    "output_path": "outputs/submission.csv",

    "top_k": 100,

    "weights": {
        "semantic": 0.40,
        "career": 0.20,
        "experience": 0.10,
        "behavioral": 0.10,
        "technical": 0.10,
        "availability": 0.05,
        "location": 0.05
    }
}