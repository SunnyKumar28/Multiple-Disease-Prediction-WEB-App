# Multiple Disease Prediction System

This project is a web application for predicting various diseases using machine learning models. The app supports predictions for Diabetes, Heart Disease, Breast Cancer, and Parkinson's Disease.



## Live Demo

You can view the live demo of the app here: [Streamlit App]([https://multiple-disease-prediction-web-app-tudfk3zpoycmmfccpnxj2s.streamlit.app/](https://multiple-disease-prediction-web-app-yhwy.onrender.com))

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/multiple-disease-prediction.git
    cd multiple-disease-prediction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the necessary models saved in the same directory:
    - `diabetese_model.sav`
    - `heart_model.sav`
    - `finalized_cancer_model.sav`
    - `parkinsons_disease_model.sav`

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

After running the Streamlit app, a web interface will be displayed with a sidebar menu for selecting different disease predictions:

1. **Diabetes Prediction**: Enter the required parameters such as Pregnancies, Glucose level, Blood Pressure, etc., and click "Diabetes Test Result" to get the prediction.

2. **Heart Disease Prediction**: Enter parameters such as Age, Sex, Chest Pain Type, etc., and click "Heart Disease Test Result" to get the prediction.

3. **Breast Cancer Prediction**: Enter parameters like Radius Mean, Texture Mean, Perimeter Mean, etc., and click "Breast Cancer Test Result" to get the prediction.

4. **Parkinson's Disease Prediction**: Enter parameters like MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz), etc., and click "Parkinson's Test Result" to get the prediction.

## Models

The application uses pre-trained machine learning models for predictions. The models are loaded from `.sav` files:
- `diabetese_model.sav`: Model for Diabetes prediction.
- `heart_model.sav`: Model for Heart Disease prediction.
- `finalized_cancer_model.sav`: Model for Breast Cancer prediction.
- `parkinsons_disease_model.sav`: Model for Parkinson's Disease prediction.






