import streamlit as st
import pandas as pd
import joblib

# load model
model = joblib.load('titanic_model.pkl')

# page title
st.set_page_config(page_title='Titanic Survival Predictor')
st.title('Titanic Survival Predictor')
st.write("Enter passenger details and predict survival: ")

# User inputs
pclass = st.selectbox(
    "PassengerClass",[1,2,3]
)

sex = st.selectbox(
    "Gender",["Male","Female"]
)

age = st.number_input(
    "Age",
    min_value=0,
    max_value=100,
    value=25
)

sibsp = st.number_input(
    "Number of siblings/Spouses",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "Number of Parents/Children",
     min_value=0,
    max_value=10,
    value=0
)

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=50.0
)

embark_town = st.selectbox(
    "Embarked Port",
    ["C","Q","S"]
)

alone = st.selectbox(
    "Alone",
    ['yes','no']
)

# encoding
sex =1 if sex=='Male' else 0
alone=1 if alone=='yes' else 0
embark_town_map={
    "C":0,
    "Q":1,
    "S":2
}

embark_town = embark_town_map[embark_town]

# 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embark_town', 'alone'
# prediction button
if st.button("Predict Survival"):
    input_data = data = pd.DataFrame({
        'pclass':[pclass],
        'sex':[sex],
        'age':[age],
        'sibsp':[sibsp],
        'parch':[parch],
        'fare':[fare],
        'embark_town':[embark_town],
        'alone':[alone]
    })

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    st.subheader("Result")

    if(prediction[0]==1):
        st.success("Passenger Survived")
    else:
        st.error("Passenger Not Survived")

