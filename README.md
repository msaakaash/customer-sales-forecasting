# 🧠 Customer Sales Forecasting & Churn Prediction

A full-stack data science project that forecasts customer sales and predicts churn using machine learning, visual analytics, and interactive dashboards. This project is containerized with Docker and production-ready with a REST API built using FastAPI.


## 🚀 Features

- 🧼 Data Cleaning & Preprocessing
- 📊 Exploratory Data Analysis (EDA)
- 🧠 Feature Engineering & Customer Segmentation
- 🔍 Predictive Modeling (Sales Forecasting & Churn Prediction)
- 🧪 Model Evaluation & Selection
- 🖼️ Interactive Dashboard using Streamlit
- 🌐 REST API using FastAPI for model serving
- 🐳 Dockerized for easy deployment


## 🔀 Project Phases

### ✅ Phase 1: Data Cleaning & Preprocessing
- Handled missing values, outliers, and feature encoding
- Scaled features for modeling

### ✅ Phase 2: Exploratory Data Analysis
- Visualized sales trends, customer segments, and patterns
- Grouped insights by product, region, and customer

### ✅ Phase 3: Feature Engineering & Clustering
- Created new insightful features
- Applied KMeans clustering for segmentation
- Visualized clusters using heatmaps and elbow curves

### ✅ Phase 4: Predictive Modeling
- Built and compared multiple models (RandomForest, XGBoost, etc.)
- Selected best model based on performance metrics
- Saved model with `joblib`

### ✅ Phase 5: Streamlit Dashboard
- Built an interactive dashboard to visualize insights and make predictions
- Integrated trained model with Streamlit interface

### ✅ Phase 6: API & Dockerization
- Created a FastAPI backend for real-time prediction
- Dockerized the API for scalable deployment


## 🛠️ Tech Stack

| Category           | Tools/Technologies                             |
|-------------------|-------------------------------------------------|
| Data Processing    | Pandas, NumPy                                  |
| Visualization      | Matplotlib, Seaborn, Plotly                    |
| Machine Learning   | Scikit-learn, XGBoost, KMeans                  |
| Dashboard          | Streamlit                                      |
| Backend API        | FastAPI, Uvicorn                               |
| Model Serving      | joblib                                         |
| Containerization   | Docker                                         |
| Version Control    | Git + GitHub                                   |



## ⚙️ Installation & Usage

### Requirements

- Python 3.10+
- Docker installed and running


### Clone the Repository

Navigate to your desired folder and run:

`git clone https://github.com/msaakaash/customer-sales-forecasting.git`  
`cd customer-sales-forecasting`


### Optional: Create a Virtual Environment

- Windows:  
  `python -m venv venv && venv\Scripts\activate`

- macOS/Linux:  
  `python3 -m venv venv && source venv/bin/activate`


### Install Dependencies (Development)

Install all required Python packages:

`pip install -r api/requirements.txt`


### Run the Streamlit Dashboard

Launch the interactive dashboard:

`streamlit run streamlit_app.py`

Visit [http://localhost:8501](http://localhost:8501)


### 🌐 Run the FastAPI Backend with Docker
`cd api`

`docker build -t churn-api .`

`docker run -p 8000:8000 churn-api`

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger docs.


## 🤝 Contributors Welcome!

We welcome contributors to improve data pipelines, dashboard UI, and deployment strategies.

Feel free to fork this project and open a pull request.


## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software.

---

## 🙌 Acknowledgement

Built by [**Aakaash M S**](https://github.com/msaakaash)

