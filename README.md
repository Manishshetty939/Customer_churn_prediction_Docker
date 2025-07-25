# 🧠 Customer Churn Prediction with Streamlit, FastAPI & Docker

This project is a complete **Customer Churn Prediction system** that includes:

- 💡 Machine Learning models for predicting customer churn
- 🌐 FastAPI backend serving the model as an API
- 🎨 Streamlit frontend to interact with the model
- 🐳 Docker container for easy deployment

- 🚀 How to Run

### 1. Clone the Repository

git clone https://github.com/Manishshetty939/Customer_churn_prediction_Docker.git
cd Customer_churn_prediction_Docker


🐳 Build and Run with Docker

# Navigate to API folder
cd api

# Build Docker image
docker build -t churn-api .

# Run the container
docker run -p 8000:8000 churn-api
The FastAPI backend will be available at:
http://localhost:8000/docs

 ▶️ Run Streamlit Frontend
In another terminal:

streamlit run app.py
Visit: http://localhost:8501
