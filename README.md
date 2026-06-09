# 🚢 Titanic Survival Prediction

## 📌 Overview

The **Titanic Survival Prediction** project uses Machine Learning to predict whether a passenger survived the Titanic disaster based on features such as age, gender, passenger class, fare, and family information.

The project involves data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and prediction. Multiple machine learning algorithms were tested, and the best-performing model was selected for final predictions.

---

## 🎯 Objective

The goal of this project is to build a predictive model that can determine whether a passenger survived the Titanic disaster using historical passenger data.

---

## 🚀 Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Model Training
* Model Evaluation and Comparison
* Survival Prediction for New Passengers
* Visualization of Insights and Trends

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Streamlit
* Joblib

---

## 📊 Dataset

The dataset contains passenger information from the Titanic disaster.

### Features

| Feature     | Description                       |
| ----------- | --------------------------------- |
| PassengerId | Unique passenger identifier       |
| Pclass      | Ticket class (1st, 2nd, 3rd)      |
| Name        | Passenger name                    |
| Sex         | Gender                            |
| Age         | Passenger age                     |
| SibSp       | Number of siblings/spouses aboard |
| Parch       | Number of parents/children aboard |
| Ticket      | Ticket number                     |
| Fare        | Passenger fare                    |
| Cabin       | Cabin number                      |
| Embarked    | Port of embarkation               |

### Target Variable

| Value | Meaning         |
| ----- | --------------- |
| 0     | Did Not Survive |
| 1     | Survived        |

---

## 📈 Exploratory Data Analysis

Key insights obtained from the dataset:

* Female passengers had a significantly higher survival rate.
* First-class passengers were more likely to survive.
* Younger passengers showed better survival chances.
* Passenger fare correlated positively with survival.
* Family size influenced survival probability.

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Handling Missing Values
4. Feature Encoding
5. Feature Scaling
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Survival Prediction

---

## 📊 Models Evaluated

| Model                  | Accuracy |
| ---------------------- | -------- |
| Logistic Regression    | 80%      |
| Decision Tree          | 63%      |
| Random Forest          | 81%      |
| K-Nearest Neighbors    | 82%      |
| Support Vector Machine | 81%      |
| Naive Bayes            | 77%      |
| XGBClassifier          | 83%      |

 ---
## 📉 Evaluation Metrics

The model performance was evaluated using:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🔮 Future Improvements

* Hyperparameter Tuning
* Advanced Feature Engineering
* Ensemble Learning Methods
* Web Application Deployment
* Real-Time Prediction Interface

---

## 🏆 Results

The final model achieved strong predictive performance and successfully identified survival patterns from passenger characteristics.
