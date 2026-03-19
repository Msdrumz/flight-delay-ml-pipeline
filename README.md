# flight-delay-ml-pipeline
# ✈️ Flight Delay Prediction Pipeline with MLflow and FastAPI

## Overview
Developed a machine learning pipeline to predict flight delays based on the origin of incoming flights to a selected airport. The project focused on automating the workflow with MLflow, deploying the trained model through a FastAPI endpoint, and validating the application with unit tests.

---

## Problem
Flight delays create operational challenges for airports, airlines, and passengers. This project explores how machine learning can be used to predict delay outcomes and how a trained model can be packaged into a reproducible, deployment-ready workflow.

---

## Solution
Built an end-to-end machine learning workflow that imports and prepares data, runs model training through an MLflow pipeline, and serves predictions through a REST API. The deployment workflow also included unit testing and Docker-based packaging to support portability and reliability.

---

## Tools & Technologies
- Python
- MLflow
- FastAPI
- pytest
- Docker
- scikit-learn
- JSON
- Jupyter / Python scripts

---

## Process
- Imported and prepared flight delay data
- Cleaned and filtered data for model input
- Coordinated the workflow using an `MLproject` file
- Logged model execution and results through MLflow
- Exported model artifacts for deployment
- Built a FastAPI endpoint for predictions
- Wrote unit tests to validate valid and invalid API requests
- Packaged the application with a Dockerfile

---

## Results
- Created a reproducible machine learning pipeline using MLflow
- Deployed the trained model through a REST API
- Added unit testing to improve reliability and validate behavior
- Structured the project for deployment-ready execution with Docker

---

## Visual Outputs

### Pipeline Workflow
![Pipeline Workflow](images/pipeline-diagram.png)

### API Response Example
![API Response Example](images/api-response.png)

---

## Project Structure
```text
flight-delay-ml-pipeline/
│
├── README.md
├── main.py
├── MLproject
├── requirements.txt
├── Dockerfile
├── api.py
├── tests/
│   └── test_api.py
├── artifacts/
│   ├── model.pkl
│   └── airport_encodings.json
└── images/
    ├── pipeline-diagram.png
    └── api-response.png
