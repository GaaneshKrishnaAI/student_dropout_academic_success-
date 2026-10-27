
# Machine Learning Assignment 2
## Student Dropout and Academic Success Prediction

### 1. Problem Statement
The objective of this project is to implement and compare five machine learning classification algorithms to predict student academic outcomes: Dropout, Enrolled, and Graduate.

### 2. Dataset Description
The dataset contains student demographic, academic, and socioeconomic information. The target variable has three classes: Dropout, Enrolled, and Graduate.

### 3. Classification Models
1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbours (KNN)
4. Gaussian Naive Baye's
5. Support Vector Machine (SVM)

### 4. Model Performance Comparison

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7684 | 0.8779 | 0.7070 | 0.6754 | 0.6826 | 0.6150 |
| Decision Tree | 0.7322 | 0.8398 | 0.6706 | 0.6453 | 0.6530 | 0.5549 |
| KNN | 0.6734 | 0.7883 | 0.5899 | 0.5722 | 0.5751 | 0.4529 |
| Gaussian Naive Bayes | 0.6599 | 0.7908 | 0.5669 | 0.5586 | 0.5581 | 0.4303 |
| Support Vector Machine | 0.7582 | 0.8664 | 0.7051 | 0.6676 | 0.6785 | 0.5986 |

### 5. Performance Observations
- **Logistic Regression:** Achieved the highest accuracy, AUC, F1 score, and MCC.
- **Decision Tree:** Achieved moderate performance across the evaluation metrics.
- **KNN:** Had lower accuracy and F1 score than Logistic Regression, Decision Tree, and SVM.
- **Gaussian Naive Bayes:** Had the lowest accuracy, precision, recall, F1 score, and MCC.
- **Support Vector Machine:** Achieved the second-highest accuracy and performed closely to Logistic Regression.

### 6. Overall Best Model
Logistic Regression was the best-performing model based on the observed results, with an accuracy of 0.7684 and an AUC of 0.8779.

### 7. GitHub Repository
Repository URL: To be added after creating the GitHub repository.

### 8. Conclusion
The five classification algorithms were evaluated using accuracy, AUC, precision, recall, F1 score, and Matthews Correlation Coefficient. Logistic Regression demonstrated the strongest overall performance among the evaluated models.

