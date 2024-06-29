#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:39:56 2024

@author: sunny-gupta
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models



diabetese_model = pickle.load(open('diabetese_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_disease_model.sav','rb'))
breast_cancer_model=pickle.load(open('finalized_cancer_model.sav','rb'))
heart_disease_model=pickle.load(open('heart_model.sav','rb'))
# sidebar

with st.sidebar:
    selected =option_menu("Multiple Disease Prediction System", 
                          
                          ['Diabetese Prediction','Heart Disease Prediction','Breast Cancer Prediction','Parkinson Disease Prediction'],
                          
                          icons = ['clipboard2-pulse','heart-pulse','virus2','file-person'],
                          
                           default_index=0,
                          
                          )
    
# diabetes prediction page
if (selected=='Diabetese Prediction'):
    #page title
    st.title('Diabetese Prediction using ML')
    
    # column for input fields
    
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
      Glucose=st.text_input('Glucose level')
        
    with col3:
        BloodPressure=st.text_input('BloodPressure level')
    
    with col1:
        SkinThickness=st.text_input('SkinThickness')
        
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    with col2:
        Age=st.text_input('Age')
        
    
    
    diab_diagnosis = ''
    #creating a button for prediction 
    if st.button('Diabetes Test Result'):
        diabetes_predict=diabetese_model.predict([[Pregnancies,Glucose,
        BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
         
        
        if (diabetes_predict[0]==1):
            diab_diagnosis='The Person is Diabetic'
            
        else :
            diab_diagnosis='The Person is not Diabetic'
            
    st.success(diab_diagnosis)
       






# Breast Cancer Prediction Page

def cancer_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = breast_cancer_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]=='M'):
       return "The Breast Cancer is Malingnant !!"
    else:
       return "The Breast Cancer is Benign !!"
    
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    

    def to_numeric(value):
        try:
            return float(value)
        except ValueError:
            return None
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = to_numeric(st.text_input('Radius Mean'))
        
    with col2:
        texture_mean = to_numeric(st.text_input('Texture Mean'))
        
    with col3:
        perimeter_mean = to_numeric(st.text_input('Perimeter Mean'))
    
    with col1:
        area_mean = to_numeric(st.text_input('Area Mean'))
        
    with col2:
        smoothness_mean = to_numeric(st.text_input('Smoothness Mean'))
        
    with col3:
        compactness_mean = to_numeric(st.text_input('Compactness Mean'))
    
    with col1:
        concavity_mean = to_numeric(st.text_input('Concavity Mean'))
        
    with col2:
        concave_points_mean = to_numeric(st.text_input('Concave Points Mean'))
        
    with col3:
        symmetry_mean = to_numeric(st.text_input('Symmetry Mean'))
    
    with col1:
        fractal_dimension_mean = to_numeric(st.text_input('Fractal Dimension Mean'))
    
    with col2:
        radius_se = to_numeric(st.text_input('Radius SE'))
        
    with col3:
        texture_se = to_numeric(st.text_input('Texture SE'))
    
    with col1:
        perimeter_se = to_numeric(st.text_input('Perimeter SE'))
        
    with col2:
        area_se = to_numeric(st.text_input('Area SE'))
        
    with col3:
        smoothness_se = to_numeric(st.text_input('Smoothness SE'))
    
    with col1:
        compactness_se = to_numeric(st.text_input('Compactness SE'))
        
    with col2:
        concavity_se = to_numeric(st.text_input('Concavity SE'))
        
    with col3:
        concave_points_se = to_numeric(st.text_input('Concave Points SE'))
    
    with col1:
        symmetry_se = to_numeric(st.text_input('Symmetry SE'))
        
    with col2:
        fractal_dimension_se = to_numeric(st.text_input('Fractal Dimension SE'))
        
    with col3:
        radius_worst = to_numeric(st.text_input('Radius Worst'))
    
    with col1:
        texture_worst = to_numeric(st.text_input('Texture Worst'))
        
    with col2:
        perimeter_worst = to_numeric(st.text_input('Perimeter Worst'))
        
    with col3:
        area_worst = to_numeric(st.text_input('Area Worst'))
    
    with col1:
        smoothness_worst = to_numeric(st.text_input('Smoothness Worst'))
        
    with col2:
        compactness_worst = to_numeric(st.text_input('Compactness Worst'))
        
    with col3:
        concavity_worst = to_numeric(st.text_input('Concavity Worst'))
    
    with col1:
        concave_points_worst = to_numeric(st.text_input('Concave Points Worst'))
        
    with col2:
        symmetry_worst = to_numeric(st.text_input('Symmetry Worst'))
        
    with col3:
        fractal_dimension_worst = to_numeric(st.text_input('Fractal Dimension Worst'))     
        

            
    # code for Prediction
    cancer_diagnosis=''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        cancer_diagnosis =cancer_prediction([radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst])                          
        

        
    st.success(cancer_diagnosis)
    
# Heart Disease Prediction


# Define the heart disease prediction function
def heart_disease_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = heart_disease_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 1:
        return "The patient is likely to have heart disease."
    else:
        return "The patient is unlikely to have heart disease."

# Check if the selected option is Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    
    # Page title
    st.title('Heart Disease Prediction using ML')

    # Function to convert input to numeric values
    def to_numeric(value):
        try:
            return float(value)
        except ValueError:
            return None
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = to_numeric(st.text_input('Age'))
        
    with col2:
        sex = to_numeric(st.text_input('Sex'))
        
    with col3:
        cp = to_numeric(st.text_input('Chest Pain Type (CP)'))
    
    with col1:
        trestbps = to_numeric(st.text_input('Resting Blood Pressure (trestbps)'))
        
    with col2:
        chol = to_numeric(st.text_input('Cholesterol (chol)'))
        
    with col3:
        fbs = to_numeric(st.text_input('Fasting Blood Sugar (fbs)'))
    
    with col1:
        restecg = to_numeric(st.text_input('Resting Electrocardiographic Results (restecg)'))
        
    with col2:
        thalach = to_numeric(st.text_input('Maximum Heart Rate Achieved (thalach)'))
        
    with col3:
        exang = to_numeric(st.text_input('Exercise Induced Angina (exang)'))
    
    with col1:
        oldpeak = to_numeric(st.text_input('Oldpeak'))
    
    with col2:
        slope = to_numeric(st.text_input('Slope of the Peak Exercise ST Segment (slope)'))
        
    with col3:
        ca = to_numeric(st.text_input('Number of Major Vessels (ca)'))
    
    with col1:
        thal = to_numeric(st.text_input('Thalassemia (thal)'))
    
    # Code for Prediction
    heart_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button("Heart Disease Test Result"):
        heart_diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.success(heart_diagnosis)
    
  
        


# Parkinson's Prediction Page
if (selected=='Parkinson Disease Prediction'):
    
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

