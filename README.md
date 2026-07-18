# Customer Retention Intelligence Platform

An end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn. The project follows a modular ML pipeline architecture and provides real-time predictions through a FastAPI backend with a Streamlit frontend.

---

## Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. This project helps identify customers who are likely to leave by analyzing customer demographics, service usage, and billing information.

The application includes:

- Modular Machine Learning Pipeline
- Data Preprocessing & Feature Engineering
- Model Training & Evaluation
- FastAPI REST API
- Streamlit Web Interface
- Logging & Exception Handling

---

## Project Architecture

```
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
               FastAPI Backend
                      │
                      ▼
            Prediction Pipeline
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
  preprocessor.pkl             model.pkl
                      │
                      ▼
            Customer Churn Prediction
```

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| API | FastAPI |
| Frontend | Streamlit |
| Model Serialization | Joblib |
| Version Control | Git |
| Deployment | Docker (Optional) |

---

## Project Structure

```
Customer-Retention-Intelligence-Platform/

│── api/
│   └── app.py

│── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl

│── data/

│── logs/

│── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── config.py
│   ├── logger.py
│   ├── exception.py
│   └── utils.py

│── streamlit_app/
│   └── app.py

│── requirements.txt
│── README.md
```

---

## Machine Learning Workflow

```
Dataset
   │
   ▼
Data Ingestion
   │
   ▼
Data Validation
   │
   ▼
Data Transformation
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Model Serialization
   │
   ▼
Prediction Pipeline
   │
   ▼
FastAPI
   │
   ▼
Streamlit Dashboard
```

---

## Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

The best-performing model is automatically selected and saved for prediction.

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| GET | `/health` | Health Check |
| POST | `/predict` | Predict Customer Churn |

---

## Streamlit Dashboard

The dashboard allows users to:

- Enter customer information
- Predict customer churn
- Display prediction results in real time

---

## Installation

### Clone Repository

```bash
git clone <repository-url>

cd Customer-Retention-Intelligence-Platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Training Pipeline

```bash
python src/pipeline/train_pipeline.py
```

---

## ▶️ Start FastAPI

```bash
uvicorn api.app:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit

```bash
streamlit run streamlit_app/app.py
```

---

## Features

- End-to-End ML Pipeline
- Modular Project Structure
- Feature Engineering
- Model Evaluation
- Real-time Prediction
- REST API
- Interactive UI
- Logging
- Exception Handling

---

## Future Improvements

- Hyperparameter Tuning
- Model Explainability (SHAP)
- Batch Prediction
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment

---

## Author

**Nikhil Jankar**

AI Engineer | Machine Learning | Python | Data Analytics

LinkedIn: *https://www.linkedin.com/in/nikhiljankar/*


---

## ⭐ If you found this project useful, consider giving it a star!
