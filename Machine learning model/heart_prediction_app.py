# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:52:40 2023

@author: Bishwadeep
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/Dell/Desktop/import/heart_model.sav','rb'))

#creating a function for prediction

def heart_prediction(input_data):

	#changing the to the numpy array
	numpy_input = np.asarray(input_data)
	#have to reshape the numpy input because we are predicting for only one entry of the complete dataset
	numpy_reshaped = numpy_input.reshape(1,-1)

	prediction = loaded_model.predict(numpy_reshaped)
	print(prediction)

	if(prediction[0]==0):
		return'Patient has no heart disease'
	else:
		return'Patient has heart disease'


def main():
	#giving a title
	st.title('Heart Disease Prediction Web app')
	
	#getting the input data from user

	age=st.number_input('Enter age')
	sex=st.number_input('Enter sex(0 for female & 1 for male)')
	cp=st.number_input('Enter CP value')
	trestbps=st.number_input('Enter Trestbps value')
	chol=st.number_input('Enter  value')
	fbs=st.number_input('BMI Chol value')
	restecg=st.number_input('Enter Restecg value')
	thalach=st.number_input('Enter Thalach value')
	exang=st.number_input('Enter Exang value')
	oldpeak=st.number_input('Enter Oldpeak value')
	slope=st.number_input('Enter Slope value')
	ca=st.number_input('Enter CA value')
	thal=st.number_input('Enter Thal value')

	#code for prediction
	diagnosis=''
 
	#creating a button for prediction
	if st.button('Heart Test Result'):
		diagnosis=heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])


	st.success(diagnosis)


if __name__ == '__main__':
	main()

