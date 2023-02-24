
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
import pandas as pd
import os
import streamlit as st

# Load the data
df = pd.read_csv('/home/ashioyajotham/Downloads/PMTCT-Data-Behavior-Identification-and-Clean-Up-Automation/Data/data.csv')

# Preprocess the data
target = "PMTCT"
features = ['facility', 'ward', 'sub_county', 'county', 'indicators', 
            'khis_data', 'datim_value', 'period', 'Month']

if st.checkbox('Show dataframe'):
    st.write(df)

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

lr_model = make_pipeline(
    OneHotEncoder(handle_unknown = "ignore"),
    LogisticRegression()
)
lr_model.fit(X_train, y_train)


# Encode the data
encoder = OneHotEncoder(handle_unknown = "ignore")
X_train_encoded = encoder.fit_transform(X_train)
X_test_encoded = encoder.transform(X_test)

# Fit the RF model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_encoded, y_train)


st.title("HIV Testing")

st.write("This is a simple HIV Testing prediction web app to predict whether a facility reports PMTCT or not.")

st.write("Please fill in the required details.")

st.balloons() # Adds a balloon animation

# style 
st.markdown(""" <style> .reportview-container { background: #F5F5F5; } </style> """, unsafe_allow_html=True)



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = pd.read_csv('/home/ashioyajotham/Downloads/PMTCT-Data-Behavior-Identification-and-Clean-Up-Automation/Data/data.csv')
# Notify the reader that the data was successfully loaded.
data_load_state.text("Loading data...done!")

# Classify the data
st.subheader('Classify the data')

# Create a selectbox for the classification model
classifier = st.selectbox('Select the classifier', ('Logistic Regression', 'Random Forest'))

# Variables for the user input features
facility = st.text_input("facility", "Enter facility")
ward = st.text_input("ward", "Enter ward")

# Create a button which when clicked predicts the class
if st.button("Predict"):
    input = pd.DataFrame([[facility, ward]], columns=['facility', 'ward'])

    # Encode the input
    input_encoded = encoder.transform(input)

    if classifier == 'Logistic Regression':
        prediction = lr_model.predict(input_encoded)
        prediction_proba = lr_model.predict_proba(input_encoded)

    elif classifier == 'Random Forest':
        prediction = rf_model.predict(input_encoded)
        prediction_proba = rf_model.predict_proba(input_encoded)

    st.subheader('Prediction')
    st.write(prediction)


