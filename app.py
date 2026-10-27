
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    confusion_matrix
)

# Configure the Streamlit page
st.set_page_config(
    page_title="Student Academic Success Dashboard",
    layout="wide"
)

st.title("Student Dropout and Academic Success Prediction")
st.write(
    "Evaluate five trained classification models on an uploaded test dataset."
)

# Allow users to upload a CSV file
uploaded_file = st.file_uploader(
    "Upload test_data.csv",
    type=["csv"]
)

# Define the available models and their saved filenames
model_paths = {
    "Logistic Regression": "model/logistic_regression.joblib",
    "Decision Tree": "model/decision_tree.joblib",
    "KNN": "model/knn.joblib",
    "Naive Bayes": "model/naive_bayes.joblib",
    "Support Vector Machine": "model/support_vector_machine.joblib"
}

if uploaded_file is not None:
    try:
        # Read the uploaded dataset
        data = pd.read_csv(uploaded_file)

        # Verify that the target column is present
        if "Target" not in data.columns:
            st.error(
                "The uploaded CSV must contain a 'Target' column "
                "with the actual class labels."
            )
            st.stop()

        # Separate input features and actual labels
        X_uploaded = data.drop(columns=["Target"])
        y_actual = data["Target"]

        # Load the training feature names and preprocessing artifacts
        scaler = joblib.load("model/scaler.joblib")
        class_labels = joblib.load("model/class_labels.joblib")

        # Check the expected input columns
        expected_columns = list(scaler.feature_names_in_)

        if list(X_uploaded.columns) != expected_columns:
            st.error(
                "The uploaded CSV columns do not match the training "
                "features or are in a different order."
            )
            st.stop()

        if X_uploaded.isnull().any().any() or y_actual.isnull().any():
            st.error("The uploaded dataset contains missing values.")
            st.stop()

        # Convert feature values to numeric form
        X_uploaded = X_uploaded.apply(pd.to_numeric, errors="raise")

        # Select a model for evaluation
        model_choice = st.selectbox(
            "Select a classification model",
            list(model_paths.keys())
        )

        # Load the selected trained model without retraining
        model = joblib.load(model_paths[model_choice])

        # Apply the same feature scaling used during training
        if model_choice in [
            "Logistic Regression",
            "KNN",
            "Support Vector Machine"
        ]:
            X_ready = scaler.transform(X_uploaded)
        else:
            X_ready = X_uploaded

        # Predict classes and class probabilities
        predictions = model.predict(X_ready)
        probabilities = model.predict_proba(X_ready)

        # Calculate the six evaluation metrics
        accuracy = accuracy_score(y_actual, predictions)

        auc = roc_auc_score(
            y_actual,
            probabilities,
            labels=model.classes_,
            multi_class="ovr",
            average="macro"
        )

        precision = precision_score(
            y_actual, predictions, average="macro", zero_division=0
        )

        recall = recall_score(
            y_actual, predictions, average="macro", zero_division=0
        )

        f1 = f1_score(
            y_actual, predictions, average="macro", zero_division=0
        )

        mcc = matthews_corrcoef(y_actual, predictions)

        # Display the evaluation metrics
        st.subheader(f"Performance Metrics: {model_choice}")

        columns = st.columns(6)
        metric_values = [
            ("Accuracy", accuracy),
            ("AUC (OvR Macro)", auc),
            ("Precision (Macro)", precision),
            ("Recall (Macro)", recall),
            ("F1 Score (Macro)", f1),
            ("MCC", mcc)
        ]

        for column, (label, value) in zip(columns, metric_values):
            column.metric(label, f"{value:.4f}")

        # Display the confusion matrix
        st.subheader("Confusion Matrix")

        cm = confusion_matrix(
            y_actual,
            predictions,
            labels=class_labels
        )

        fig, ax = plt.subplots(figsize=(7, 5))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=class_labels,
            yticklabels=class_labels,
            ax=ax
        )

        ax.set_xlabel("Predicted Class")
        ax.set_ylabel("Actual Class")
        ax.set_title(f"Confusion Matrix: {model_choice}")

        st.pyplot(fig)
        plt.close(fig)

        # Display a sample of actual and predicted outcomes
        st.subheader("Prediction Preview")

        preview = pd.DataFrame({
            "Actual Outcome": y_actual,
            "Predicted Outcome": predictions
        })

        st.dataframe(preview.head(20), use_container_width=True)

    except Exception as error:
        st.error(f"Unable to evaluate the uploaded dataset: {error}")
