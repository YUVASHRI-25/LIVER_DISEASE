# 🍷 Liver Disease Classification App

This is a web application built using **Streamlit** that predicts the risk of liver disease based on various patient parameters. The model is built using a **Random Forest classifier** trained on a dataset that has been balanced using **SMOTE** (Synthetic Minority Over-sampling Technique). The app provides a user-friendly interface for entering patient details and getting predictions on the risk of liver disease.

**TRY WITH STREAMLIT APP**:https://liverdiabetes.streamlit.app/

## 🛠️ Features

- **Data Input**: Users can input details like age, gender, various blood test parameters, etc.
- **Prediction**: The app predicts whether a patient has a high or low risk of liver disease.
- **Model**: The model is a **Random Forest classifier**, trained with a balanced dataset using **SMOTE**.
- **Interactive UI**: Built with **Streamlit** to provide an interactive experience.
  

## 🧠 Model Training

The model was trained using the **Random Forest classifier** with the **liver dataset**. **SMOTE** was used to balance the classes before training to address the issue of class imbalance.

### Model Hyperparameters:

* **n\_estimators**: Number of trees in the forest \[100, 200, 300].
* **max\_depth**: The maximum depth of the tree \[None, 10, 20, 30].
* **min\_samples\_split**: The minimum number of samples required to split an internal node \[2, 5, 10].
* **min\_samples\_leaf**: The minimum number of samples required to be at a leaf node \[1, 2, 4].
* **bootstrap**: Whether bootstrap samples are used when building trees \[True, False].

## 🔥 App Workflow

1. **User Input**: The app collects data like Age, Gender, Total Bilirubin, Direct Bilirubin, Alkaline Phosphotase, etc.
2. **Feature Scaling**: Input features are scaled using **StandardScaler** to match the scale used during model training.
3. **Prediction**: The app predicts the likelihood of liver disease using the trained **Random Forest model** and displays the result:

   * **High Risk**: If the probability is greater than or equal to **0.55**.
   * **Low Risk**: If the probability is less than **0.55**.


```

## 📊 Results

The model achieves the following evaluation metrics on the test set:

* **Accuracy**: 91.23%
* **Precision**: 89.01%
* **Recall**: 92.45%
* **F1-Score**: 90.78%

```

