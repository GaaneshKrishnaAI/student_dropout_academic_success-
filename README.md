# Machine Learning Assignment 2

# Student Dropout and Academic Success Prediction

A Machine Learning project that implements and compares five classification algorithms to predict student academic outcomes: **Dropout, Enrolled, and Graduate**.

## 1. Project Overview

The objective of this project is to develop and evaluate machine learning classification models that predict student academic outcomes using demographic, academic, and socioeconomic information.

The project compares five classification algorithms and evaluates their performance using multiple classification metrics. A Streamlit web application is also developed to allow users to upload test data, select a trained model, and view its evaluation results.

## 2. Dataset Description

The project uses the Predict Students' Dropout and Academic Success dataset from the UCI Machine Learning Repository.

Dataset Source: UCI Machine Learning Repository

Total Instances: 4,424

Input Features: 36

Target Variable: Student academic outcome

Classification Classes:

Dropout

Enrolled

Graduate

The dataset contains demographic, academic, and socioeconomic information about students. It is used to train and evaluate the five classification models.

Dataset Link:
https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success



## 3. Machine Learning Models

Five classification algorithms are implemented and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes
5. Support Vector Machine (SVM)

## 4. Project Workflow

The project follows these main stages:

1. **Data Loading:** Load the dataset and examine its structure.
2. **Exploratory Data Analysis:** Analyze the dataset and understand the distribution of student academic outcomes.
3. **Data Preprocessing:** Prepare the input features and target variable for model training.
4. **Train-Test Split:** Divide the dataset into training and testing sets.
5. **Model Training:** Train the five classification algorithms.
6. **Model Evaluation:** Evaluate each model using multiple performance metrics.
7. **Model Comparison:** Compare the results to identify the best-performing classifier.
8. **Model Serialization:** Save the trained models, scaler, and class labels using Joblib.
9. **Deployment:** Develop and deploy an interactive Streamlit application.

## 5. Evaluation Metrics

The models are evaluated using the following metrics:

- **Accuracy:** Overall proportion of correctly classified observations.
- **AUC (OvR Macro):** Measures the ability to distinguish between the three classes using a One-vs-Rest approach.
- **Precision (Macro):** Measures the average precision across the classes.
- **Recall (Macro):** Measures the average recall across the classes.
- **F1 Score (Macro):** Harmonic mean of precision and recall, averaged across classes.
- **Matthews Correlation Coefficient (MCC):** Measures the overall quality of classification predictions.

## 6. Model Performance Comparison

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7684 | 0.8779 | 0.7070 | 0.6754 | 0.6826 | 0.6150 |
| Decision Tree | 0.7322 | 0.8398 | 0.6706 | 0.6453 | 0.6530 | 0.5549 |
| KNN | 0.6734 | 0.7883 | 0.5899 | 0.5722 | 0.5751 | 0.4529 |
| Gaussian Naive Bayes | 0.6599 | 0.7908 | 0.5669 | 0.5586 | 0.5581 | 0.4303 |
| Support Vector Machine | 0.7582 | 0.8664 | 0.7051 | 0.6676 | 0.6785 | 0.5986 |

## 7. Performance Observations

- **Logistic Regression:** Achieved the highest accuracy, AUC, F1 score, and MCC among the five models.
- **Decision Tree:** Demonstrated moderate classification performance across the evaluation metrics.
- **KNN:** Recorded lower accuracy and F1 score compared with Logistic Regression, Decision Tree, and SVM.
- **Gaussian Naive Bayes:** Recorded the lowest accuracy, precision, recall, F1 score, and MCC.
- **Support Vector Machine:** Achieved the second-highest accuracy and performed closely to Logistic Regression.

## 8. Overall Best-Performing Model

Based on the evaluation results, **Logistic Regression** demonstrated the strongest overall performance.

- **Accuracy:** 0.7684
- **AUC (OvR Macro):** 0.8779
- **F1 Score (Macro):** 0.6826
- **MCC:** 0.6150

It achieved the highest accuracy and AUC among the five evaluated classification algorithms.

## 9. Streamlit Web Application
An interactive web application was developed using Streamlit and deployed on Streamlit Community Cloud.
Application features:
Upload a test dataset (test_data.csv).
Select an available trained classification model.
Evaluate the uploaded dataset using the saved model.
Display classification performance metrics.
Visualize the confusion matrix for the selected model.
The application loads saved trained models and evaluates the uploaded test dataset without retraining.
Deployment note: All five classification models are implemented and evaluated in the project. Due to a scikit-learn model compatibility issue on Streamlit Community Cloud, the Decision Tree model is currently unavailable in the deployed application. The remaining four models are available for interactive evaluation.
Live Application: https://mqeow2vpq77bbvgtrz29gf.streamlit.app/


## 10. Technologies and Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## 11. Repository Structure

```text
student_dropout_academic_success-/
│
├── model/
│   ├── class_labels.joblib
│   ├── decision_tree.joblib
│   ├── knn.joblib
│   ├── logistic_regression.joblib
│   ├── naive_bayes.joblib
│   ├── scaler.joblib
│   └── support_vector_machine.joblib
│
├── ML .ipynb
├── app.py
├── data.csv
├── test_data.csv
├── model_comparison.csv
├── requirements.txt
├── runtime.txt
└── README.md
```

## 12. How to Run the Project Locally

**Step 1: Clone the repository**

```bash
git clone https://github.com/GaaneshKrishnaAI/student_dropout_academic_success-.git
```

**Step 2: Navigate to the project directory**

```bash
cd student_dropout_academic_success-
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Streamlit application**

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

## 13. GitHub Repository

**Source Code:**  
https://github.com/GaaneshKrishnaAI/student_dropout_academic_success-

## 14. Conclusion

This project demonstrates the implementation and comparison of five machine learning classification algorithms for predicting student academic outcomes.

The models were evaluated using multiple performance metrics, including Accuracy, AUC, Precision, Recall, F1 Score, and Matthews Correlation Coefficient.

Among the evaluated algorithms, Logistic Regression achieved the strongest overall performance. The project also demonstrates the practical deployment of trained machine learning models through an interactive Streamlit application.

---

**Project:** Machine Learning Assignment 2  
**Title:** Student Dropout and Academic Success Prediction
