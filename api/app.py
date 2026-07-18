from fastapi import FastAPI
from pydantic import BaseModel

from src.pipeline.predict_pipeline import (
    PredictPipeline,
    CustomData
)

app = FastAPI(
    title="Customer Retention Intelligence Platform",
    version="1.0",
    description="Customer Churn Prediction API"
)


class CustomerRequest(BaseModel):

    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():

    return {
        "message": "Customer Retention Intelligence Platform API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(data: CustomerRequest):

    custom_data = CustomData(
        gender=data.gender,
        SeniorCitizen=data.SeniorCitizen,
        Partner=data.Partner,
        Dependents=data.Dependents,
        tenure=data.tenure,
        PhoneService=data.PhoneService,
        MultipleLines=data.MultipleLines,
        InternetService=data.InternetService,
        OnlineSecurity=data.OnlineSecurity,
        OnlineBackup=data.OnlineBackup,
        DeviceProtection=data.DeviceProtection,
        TechSupport=data.TechSupport,
        StreamingTV=data.StreamingTV,
        StreamingMovies=data.StreamingMovies,
        Contract=data.Contract,
        PaperlessBilling=data.PaperlessBilling,
        PaymentMethod=data.PaymentMethod,
        MonthlyCharges=data.MonthlyCharges,
        TotalCharges=data.TotalCharges
    )

    df = custom_data.get_data_as_dataframe()

    predictor = PredictPipeline()

    prediction = predictor.predict(df)

    result = "Yes" if prediction[0] == "Yes" else "No"

    return {
        "prediction": result
    }