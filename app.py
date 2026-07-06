import streamlit as st
import pandas as pd
import numpy as np
import pickle

model=pickle.load(open("model.pkl","rb"))
sc=pickle.load(open("sc.pkl","rb"))

st.title("Diabetic Patient Prediction ")

col1,col2=st.columns(2)

with col1:
    pregnacies=st.slider("pregnacies",0,17,1)
    BloodPressure=st.slider("BloodPressure",40,140,72)
    Insulin=st.slider("Insulin",15,300,80)
    DiabeticPedigreeFunction=st.number_input(
        "Diabetic Pedigree Function",
        min_value=0.05,
        max_value=3.0,
        value=0.47,
        step=0.001,
        format="%.3f"

    )
with col2:
    Glucose=st.slider("Glucose",50,200,120)    
    SkinThickness=st.slider("SkinThickness",7,99,20)
    BMI=st.slider("BMI",18.0,50.0,32.0,step=0.1)
    Age=st.slider("Age",21,81,33)

if st.button("predict"):
    columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age' ]
    myinput=[pregnacies,BloodPressure,Insulin,DiabeticPedigreeFunction,Glucose,SkinThickness,BMI,Age]
    myinput = pd.DataFrame([[1, 72, 80, 0.47, 120, 20, 32, 33]], columns=columns)


    result=model.predict(myinput)
    if result[0] == 0:
        st.error("NO, patient is not Diabetic")
    else:
        st.success("yes,patient is Diabetic")    