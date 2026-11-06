# Machine Learning Assignment 2
## Student Dropout and Academic Success Prediction

### 1. Problem Statement
The objective of this project is to implement and compare five machine learning classification algorithms to predict student academic outcomes: Dropout, Enrolled, and Graduate.

### 2. Dataset Description
The project uses the UCI Machine Learning Repository dataset **"Predict Students' Dropout and Academic Success."** It contains 4,424 student records with demographic, academic, and socioeconomic information. The target variable has three classes: Dropout, Enrolled, and Graduate.

Dataset Source: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

### 3. Classification Models
1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbours (KNN)
4. Gaussian Naive Bayes
5. Support Vector Machine (SVM)

### 4. Model Performance Comparison

| Model | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7684 | 0.8779 | 0.7070 | 0.6754 | 0.6826 | 0.6150 |
| Decision Tree | 0.7322 | 0.8398 | 0.6706 | 0.6453 | 0.6530 | 0.5549 |
| KNN | 0.6734 | 0.7883 | 0.5899 | 0.5722 | 0.5751 | 0.4529 |
| Gaussian Naive Bayes | 0.6599 | 0.7908 | 0.5669 | 0.5586 | 0.5581 | 0.4303 |
| SVM | 0.7582 | 0.8664 | 0.7051 | 0.6676 | 0.6785 | 0.5986 |

### 5. Performance Observations
- **Logistic Regression:** Achieved the highest accuracy, AUC, F1-score, and MCC, demonstrating the strongest overall performance.
- **Decision Tree:** Delivered moderate performance across the evaluation metrics.
- **KNN:** Achieved lower accuracy and F1-score compared with Logistic Regression, Decision Tree, and SVM.
- **Gaussian Naive Bayes:** Recorded the lowest accuracy, precision, recall, F1-score, and MCC among the five models.
- **SVM:** Achieved the second-highest accuracy and performed close to Logistic Regression.

### 6. Overall Best Model
Logistic Regression is the best-performing model overall, achieving an accuracy of **0.7684** and an AUC of **0.8779**. It also recorded the highest F1-score and MCC among the five classifiers.

### 7. GitHub Repository
Repository Link: https://github.com/GaaneshKrishnaAI/student_dropout_academic_success-

### 8. Live Streamlit Application
Application Link: https://mqeow2vpq77bbvgtrz29gf.streamlit.app/

### 9. Conclusion
Five machine learning classification algorithms were implemented and evaluated using six performance metrics. Based on the comparison, Logistic Regression demonstrated the strongest overall predictive performance for student academic outcome classification.
