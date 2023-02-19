# PMTCT-tests-automation
A classification model that assists in the identification of PMTCT sites that do not report tests.
Introduction
The HealthIT project continues to support the implementation of various Information Systems on the Ministry of Health. One of the overarching goals of the continued development and deployment of health information systems is to support data driven decision making in the healthcare sector. In this regard a lot of efforts have gone into the development of mechanisms to collect accurate data, to ensure its quality and to develop reports and visualizations. 
Our project focused on the development of a classification model app that would check and see which sites did not report their  PMTCT - Prevention-Of-Mother-To-Child-Hiv-Transmission. Reprting of HIV testing indicators is inconstistend across facilities some tests include tests from some testing locations and exclude PMTCT tests 

*Objectives of the project*

1.To create a model that will predict accurately facilities that have not submitted their PMTCT data

2.Identify other missing variables 

3.Be able to flag facilities whose data is inconsistent where both datim_values and dhis_values are never aligned 

4.To able able to classify and render data in app 

Value of the data to client 

The data for HIV tested in facilities across the countries and the PMTCT data are crucial in both acquisition of drugs and testing kits. Also the amount of HIV positive is important for further policy making. So being able to classify the data and see inconsistency and to be able to flag facilities that are not able to take, store and report the data is important.It will also help them to be able to use data for other various things. We have also created an UI where it will be easy to access the data and to even download a well classified report.

Data Acquisition

The data was provided by the Health It team from there systems

EDA(Exploratory Data Analysis)

During the EDA process we explored descriptive statistics and multicoliniarity

Insight -
Most features have a high and direct correlation
