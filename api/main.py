from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model/churn_predictor.pkl")

class Customer(BaseModel):
    Recency: int
    Frequency: int
    Monetary: float

@app.get("/")
def read_root():
    return {"msg": "Churn Prediction API is up!"}

@app.post("/predict")
def predict_churn(customer: Customer):
    data = pd.DataFrame([customer.dict()])
    prediction = model.predict(data)[0]
    return {"churn_prediction": int(prediction)}
