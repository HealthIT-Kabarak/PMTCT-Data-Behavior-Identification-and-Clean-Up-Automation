import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os
import streamlit as st

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config (page_title="PMTCT Reporting", page_icon=":heart:", layout="centered", initial_sidebar_state="expanded")

st.title("HIV Testing")

st.write("This is a simple HIV Testing prediction web app to predict whether a facility reports PMTCT or not.")

st.write("Please fill in the required details.")

st.balloons() # Adds a balloon animation

# style 
st.markdown(""" <style> .reportview-container { background: #F5F5F5; } </style> """, unsafe_allow_html=True)



st.write('---') # Adds a horizontal line
def user_input_features():
    county = st.text_input("Facility")
    period = st.text_input("Period")

    cols = [i for i in range(0, 5489)]

    data = {
            'county': county,

            'period': period}

    features = pd.DataFrame.from_dict([data])

    # One hot encode the data using pandas get_dummies
    features = pd.get_dummies(features)

    # Align the data's columns with the model's columns
    features = features.reindex(columns=cols, fill_value=0)

    return features

df = user_input_features() # Store the user input features into a variable  df = pd.DataFrame(features) # Create a Pandas DataFrame

st.write('---')

prediction = model.predict_proba(df)

st.write('---')

if st.button('Predict'):
    if df.isnull().values.any():
        st.error("Please fill in all the required details.")
    else:
        output = model.predict(df)[0]

        if output == 1:
            st.success('The facility reports PMTCT')
        else:
            st.success('The facility did not report PMTCT')

st.write('---')