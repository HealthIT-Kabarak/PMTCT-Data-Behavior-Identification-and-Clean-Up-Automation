# The next task is to build a simple web app that will allow users to input data and get a prediction
# We will use streamlit to build the web app
# We will use ngrok to expose the web app to the internet
# We will use the following commands to install streamlit and ngrok
#!pip install streamlit
#!pip install pyngrok

# Import streamlit
import streamlit as st

# Import ngrok
from pyngrok import ngrok
import pandas as pd

# Create a function that will take in the user input and make a prediction
def make_prediction(facility, ward, sub_county, county, indicators, khis_data, datim_value, period, Month):
  # Create a dataframe that will hold the user input
  user_input = pd.DataFrame({
      'facility': [facility],
      'ward': [ward],
      'sub_county': [sub_county],
      'county': [county],
      'indicators': [indicators],
      'khis_data': [khis_data],
      'datim_value': [datim_value],
      'period': [period],
      'Month': [Month]
  })

  # Encode the user input
  import pickle
  encoder = pickle.load(open('encoder.pkl', 'rb'))
  user_input_encoded = encoder.transform(user_input)

  # Make a prediction
  model = pickle.load(open('model.pkl', 'rb'))
  prediction = model.predict(user_input_encoded)[0]
  if prediction == 0:
    return "No"
  else:
    return "Yes"
  

# Create a title for the web app
st.title("HIV Prediction App")

# Create a form for the user to input data
with st.form(key='hiv-form'):
  facility = st.text_input(label='Facility')
  ward = st.text_input(label='Ward')
  sub_county = st.text_input(label='Sub County')
  county = st.text_input(label='County')
  indicators = st.text_input(label='Indicators')
  khis_data = st.text_input(label='Khis Data')
  datim_value = st.text_input(label='Datim Value')
  period = st.text_input(label='Period')
  Month = st.text_input(label='Month')
  submit_button = st.form_submit_button(label='Submit')

# Create a condition that will check if the submit button has been clicked
if submit_button:
  # Call the make_prediction function
  prediction = make_prediction(facility, ward, sub_county, county, indicators, khis_data, datim_value, period, Month)
  # Display the prediction
  st.write(f"Prediction: {prediction}")

# We want it to display a dashbboard that can be used to check the number of HIV positive patients in a facility at a given time
# We will use the following commands to install plotly
#!pip install plotly
  
# Import plotly
import plotly.express as px


# Load the data
data = pd.read_csv('data.csv')

# Create a title for the dashboard
st.title("HIV Dashboard")

# Create a sidebar for the dashboard
st.sidebar.title("HIV Dashboard")

# Create a multiselect widget for the dashboard
facility = st.sidebar.multiselect("Facility", data['facility'].unique())

# Create a condition that will check if the facility multiselect widget has been used
if len(facility) > 0:
  # Filter the data
  data = data[data['facility'].isin(facility)]

# Create a multiselect widget for the dashboard
county = st.sidebar.multiselect("County", data['county'].unique())
sub_county = st.sidebar.multiselect("Sub County", data['sub_county'].unique())
ward = st.sidebar.multiselect("Ward", data['ward'].unique())
indicators = st.sidebar.multiselect("Indicators", data['indicators'].unique())
khis_data = st.sidebar.multiselect("Khis Data", data['khis_data'].unique())
datim_value = st.sidebar.multiselect("Datim Value", data['datim_value'].unique())
period = st.sidebar.multiselect("Period", data['period'].unique())
Month = st.sidebar.multiselect("Month", data['Month'].unique())

# Next we will create a condition that will check if the multiselect widgets have been used
if len(county) > 0:
  # Filter the data
  data = data[data['county'].isin(county)]
if len(sub_county) > 0:
  # Filter the data
  data = data[data['sub-county'].isin(sub_county)]
if len(ward) > 0:
  # Filter the data
  data = data[data['ward'].isin(ward)]
if len(indicators) > 0:
  # Filter the data
  data = data[data['indicators'].isin(indicators)]
if len(khis_data) > 0:
  # Filter the data
  data = data[data['khis_data'].isin(khis_data)]
if len(datim_value) > 0:
  # Filter the data
  data = data[data['datim_value'].isin(datim_value)]
if len(period) > 0:
  # Filter the data
  data = data[data['period'].isin(period)]
if len(Month) > 0:  
  # Filter the data
  data = data[data['Month'].isin(Month)]

# Create a condition that will check if the data is empty
if data.empty:
  # Display a message
  st.write("Please select a value from the sidebar")
else:
  st.write("HIV Positive Patients")


  # Create a bar chart
  fig = px.bar(data, x='facility', y='datim_value', color='county', height=500)
  # add labels
  fig.update_layout(xaxis_title="Facility", yaxis_title="Number of HIV Positive Patients")
  # Display the chart
  st.plotly_chart(fig)

# Create a public URL for the web app
public_url = ngrok.connect(8501)
public_url