# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:19:18 2023

@author: Bishwadeep
"""



import numpy as np
import pickle
import streamlit as st

#loading the asved model
loaded_model=pickle.load(open('C:/Users/Dell/Desktop/import/diabetes_model.sav','rb'))

#creating a function for prediction

def diabetes_prediction(input_data):

	#changing the to the numpy array
	numpy_input = np.asarray(input_data)
	#have to reshape the numpy input because we are predicting for only one entry of the complete dataset
	numpy_reshaped = numpy_input.reshape(1,-1)

	prediction = loaded_model.predict(numpy_reshaped)
	print(prediction)

	if(prediction[0]==0):
		return'Patient is non-diabetic'
	else:
		return'Patient is diabetic'


def main():
	#giving a title
	st.title('Diabetes Prediction Web app')
	
	#getting the input data from user
	
	Pregnancies=st.number_input('Number of Pregnancies')
	Glucose=st.number_input('Glucose level')
	BloodPressure=st.number_input('BloodPressure value')
	SkinThickness=st.number_input('SkinThickness value')
	Insulin=st.number_input('Insulin value')
	BMI=st.number_input('BMI value')
	DiabetesPedigreeFunction=st.number_input('DiabetesPedigreeFunction value')
	Age=st.number_input('Age of the patient')

	#code for prediction
	diagnosis= ''
 
	#creating a button for prediction
	if st.button('Diabetes Test Result'):
		diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])


	st.success(diagnosis)


if __name__ == '__main__':
	main()
