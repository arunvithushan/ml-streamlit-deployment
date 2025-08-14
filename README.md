# 🍷 Wine Quality Prediction - Streamlit ML Deployment

## 📌 Overview
This project is a complete **Machine Learning pipeline** for predicting the quality of wine based on various chemical properties.  
It includes:
- Data analysis
- Model training
- Streamlit app development
- Deployment to **Streamlit Cloud**

Dataset used: **Wine Quality Dataset** (Kaggle)

---

## 📊 Dataset Description
The dataset contains various physicochemical tests (like acidity, sugar, pH, etc.) and a target variable: **quality** (score between 0 and 10).

**Features include:**
- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol

**Target:**
- Quality score (0–10)

---

## 🛠 Steps in the Project

### 1. Data Preprocessing & EDA
- Checked for missing values and outliers
- Visualized distributions using **Matplotlib** & **Seaborn**
- Correlation analysis
- Feature scaling

### 2. Model Training
- Algorithms used:
  - Random Forest Classifier
  - Logistic Regression
- Evaluation with accuracy, confusion matrix, and classification report
- Best model selected and saved as `model.pkl` using **pickle**

### 3. Streamlit App Features
- **Dataset Overview** – shape, columns, data types
- **Data Visualization** – interactive plots using Plotly & Matplotlib
- **Model Prediction** – user inputs chemical properties → predict wine quality
- **Model Performance** – metrics and comparison results

### 4. Deployment
- Project pushed to **GitHub**
- Deployed using **Streamlit Cloud**

---
