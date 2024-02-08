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
st.title("PMTCT Analysis & Reporting")

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
st.title("PMTCT Dashboard")

# Create a sidebar for the dashboard
st.sidebar.title("PMTCT Reporting Dashboard")

# Next we will create a condition that will check if the multiselect widgets have been used
if len(county) > 0:
  if isinstance(county, str) or not hasattr(county, '__iter__'):
    county = [county]
    data = data[data['county'].isin(county)]

# Create a multiselect widget for the dashboard
county = st.sidebar.multiselect("County", data['county'].unique())

# For sub county, we need to only display the sub counties that are in the selected county
# Create a condition that will check if the county multiselect widget has been used
if len(county) > 0:
  # Filter the data
  data = data[data['county'].isin(county)]
  # Update the sub county multiselect widget to only display the sub counties that are in the selected county
  sub_county = st.sidebar.multiselect("Sub County", data['sub_county'].unique())
  # Create a condition that will check if the sub county multiselect widget has been used
  if len(sub_county) > 0:
    if isinstance(sub_county, str) or not hasattr(sub_county, '__iter__'):
      sub_county = [sub_county]
      data = data[data['sub_county'].isin(sub_county)]
else:
  # Update the sub county multiselect widget to match the data
  sub_county = st.sidebar.multiselect("Sub County", data['sub_county'].unique())

# For the ward, we need to only display the wards that are in the selected sub county
# Create a condition that will check if the sub county multiselect widget has been used
if len(sub_county) > 0:
  # Filter the data
  data = data[data['sub_county'].isin(sub_county)]
  # Update the ward multiselect widget to only display the wards that are in the selected sub county
  ward = st.sidebar.multiselect("Ward", data['ward'].unique())
  # Create a condition that will check if the ward multiselect widget has been used
  if len(ward) > 0:
    if isinstance(ward, str) or not hasattr(ward, '__iter__'):
      ward = [ward]
      data = data[data['ward'].isin(ward)]
else:
  # Update the ward multiselect widget to match the data
  ward = st.sidebar.multiselect("Ward", data['ward'].unique())

# For the facility, we need to only display the facilities that are in the selected ward
# Create a condition that will check if the ward multiselect widget has been used
if len(ward) > 0:
  # Filter the data
  data = data[data['ward'].isin(ward)]
  # Update the facility multiselect widget to only display the facilities that are in the selected ward
  facility = st.sidebar.multiselect("Facility", data['facility'].unique())
  # Create a condition that will check if the facility multiselect widget has been used
  if len(facility) > 0:
    if isinstance(facility, str) or not hasattr(facility, '__iter__'):
      ward = [ward]
      data = data[data['facility'].isin(facility)]
else:
  # Update the facility multiselect widget to match the data
  facility = st.sidebar.multiselect("Facility", data['facility'].unique())

if len(indicators) > 0:
  if isinstance(indicators, str) or not hasattr(indicators, '__iter__'):
    indicators = [indicators]
  # Filter the data
  data = data[data['indicators'].isin(indicators)]
if len(khis_data) > 0:
  if isinstance(khis_data, str) or not hasattr(khis_data, '__iter__'):
    khis_data = [khis_data]
  # Filter the data
  data = data[data['khis_data'].isin(khis_data)]
if len(datim_value) > 0:
  if isinstance(datim_value, str) or not hasattr(datim_value, '__iter__'):
    datim_value = [datim_value]
  # Filter the data
  data = data[data['datim_value'].isin(datim_value)]
if len(period) > 0:
  if isinstance(period, str) or not hasattr(period, '__iter__'):
    period = [period]
  # Filter the data
  data = data[data['period'].isin(period)]
if len(Month) > 0:
  if isinstance(Month, str) or not hasattr(Month, '__iter__'):
    Month = [Month] 
  # Filter the data
  data = data[data['Month'].isin(Month)]

# Create a multiselect widget for the dashboard
#county = st.sidebar.multiselect("County", data['county'].unique())
#sub_county = st.sidebar.multiselect("Sub County", data['sub_county'].unique())
#ward = st.sidebar.multiselect("Ward", data['ward'].unique())
#facility = st.sidebar.multiselect("Facility", data['facility'].unique())
#indicators = st.sidebar.multiselect("Indicators", data['indicators'].unique())
#datim_value = st.sidebar.multiselect("Datim Value", data['datim_value'].unique())
#period = st.sidebar.multiselect("Period", data['period'].unique())
#Month = st.sidebar.multiselect("Month", data['Month'].unique())


# Create a condition that will check if the data is empty
if data.empty:
  # Display a message
  st.write("Please select a value from the sidebar")
else:
  st.write("HIV Positive Patients")

  # Create a bar chart
  fig = px.bar(data, x='facility', y='datim_value', color='county', facet_row='period', height=800)
  # add labels
  fig.update_layout(xaxis_title="Facility", yaxis_title="Number of HIV Positive Patients", xaxis_tickangle=-90, margin=dict(r=150)) 
  # Display the chart
  st.plotly_chart(fig)

# Create a public URL for the web app
public_url = ngrok.connect(8501)
public_url