import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modelTraining = st.beta_container()

with header:
    st.title('Welcome! to a Scratch Score Application!')

with dataset:
    st.header('Dataset')
    st.text('My dataset')

    scratch_data = pd.read_excel("Scratch_Project_Data_01_11_4321_Pair04.xlsx")
    st.write(scratch_data.head())

    grade_dist = pd.DataFrame(scratch_data['Grade'].value_counts())
    st.bar_chart(grade_dist)

with features:
    st.header('Features')
    st.text('My features')

with modelTraining:
    st.header('Model')
    st.text('My model')
