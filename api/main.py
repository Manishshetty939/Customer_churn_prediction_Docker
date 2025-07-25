from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("churn_predictor.pkl")


# Create FastAPI app
app = FastAPI(title="Churn Prediction API")

# Define input schema
class CustomerData(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Churn Prediction API"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    input_data = np.array([[data.Recency, data.Frequency, data.Monetary]])
    prediction = model.predict(input_data)[0]
    result = "Churn" if prediction == 1 else "Not Churn"
    return {"prediction": result}
