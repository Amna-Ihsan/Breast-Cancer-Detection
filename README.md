## Breast Cancer Detection Model

This project is a machine learning web application that predicts whether a breast cancer tumor is **Benign** or **Malignant** using diagnostic data. The model is trained using **Logistic Regression** and deployed with a simple **Streamlit user interface**.

### Project Overview

The dataset is loaded from `breast_cancer.csv`. The unnecessary `Sample code number` column is removed, and the remaining diagnostic features are used to train the model.

The target column is:

* `Class`

In this dataset:

* `2` = Benign
* `4` = Malignant

### Technologies Used

* Python
* Pandas
* Scikit-learn
* Logistic Regression
* Joblib
* Streamlit
* k-Fold Cross Validation

### Model Workflow

1. Import the dataset.
2. Remove the `Sample code number` column.
3. Check for missing values and duplicates.
4. Split the dataset into training and testing sets.
5. Train a Logistic Regression model.
6. Predict results on the test data.
7. Evaluate the model using accuracy score and confusion matrix.
8. Validate the model using 10-fold Cross Validation.
9. Save the trained model and feature names using Joblib.
10. Load the model in Streamlit for user prediction.

### User Interface

A simple web interface is created using **Streamlit**. Users can enter diagnostic feature values using sliders. After clicking the **Predict** button, the app predicts whether the tumor is **Benign** or **Malignant**.

### How to Run the Project

Install the required libraries:

```bash
pip install pandas scikit-learn joblib streamlit
```

Run the Streamlit app:

```bash
streamlit run app.py
```

### Model Evaluation

The model is evaluated using:

* Accuracy Score
* Confusion Matrix
* 10-Fold Cross Validation
* Standard Deviation of accuracy scores

### Project Link

[View Project](https://breast-cancer-detection-myysnypmquibmywqxrq2ww.streamlit.app/)

