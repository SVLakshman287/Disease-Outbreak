import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Prediction of Disease Outbreaks',layout='wide',page_icon='doctor')
diabetes_model=pickle.load(open(r"C:\Users\Ashok\Documents\Project Deseases\Training_models\diabetes_model.sav",'rb'))
hear_disease_model=pickle.load(open(r"C:\Users\Ashok\Documents\Project Deseases\Training_models\diabetes_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"C:\Users\Ashok\Documents\Project Deseases\Training_models\diabetes_model.sav",'rb'))
with st.sidebar:
    selected=option_menu('Prediction of disease outbreak system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    if selected=='Diabetes Prediction':
        st.title('Diabetes Prediction using Ml')
        col1,col2,col3=st.columns(3)
        with col1:
            Pregnancies=st.text_input('Number of Pregnencies')
        with col2:
            Glucose=st.text_input('Glucose level')
        with col3:
            Bloodpressure=st.text_input('Blood pressure value')
        with col1:
            SkinThickness=st.text_input('Skin Thickness value')
        with col2:
            Insulin=st.text_input('Insulin level')
        with col3:
            BMI=st.text_input('BMI Value')
        with col1:
            DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
        with col2:
            Age=st.text_input('Age of the person')
        diab_diagnosis=''
        if st.button('Diabetes Text Result'):
            user_input=[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
            user_input=[float(x) for x in user_input]
            diab_prediction=diabetes_model.predict([user_input])
            if diab_prediction[0]==1:
                diab_diagnosis='The person is diabetic'
            else:
                diab_diagnosis='The person is not diabetic'
    st.success(diab_diagnosis)