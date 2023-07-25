# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:00:41 2023

@author: Bishwadeep
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/Dell/Desktop/import/parkinsons_model.sav','rb'))

#creating a function for prediction

def parkinsons_prediction(input_data):

	#changing the to the numpy array
	numpy_input = np.asarray(input_data)
	#have to reshape the numpy input because we are predicting for only one entry of the complete dataset
	numpy_reshaped = numpy_input.reshape(1,-1)

	prediction = loaded_model.predict(numpy_reshaped)
	print(prediction)

	if(prediction[0]==0):
		return'Patient has no Parkinsons Disease'
	else:
		return'Patient has Parkinsons Disease'


def main():
	#giving a title
	st.title('Parkinsons Disease Prediction Web app')
	
	#getting the input data from user

	MDVP:Fo(Hz)=st.number_input('MDVP:Fo(Hz) value')
	MDVP:Fhi(Hz)=st.number_input('MDVP:Fhi(Hz) value')
	MDVP:Flo(Hz)=st.number_input('MDVP:Flo(Hz) value')
	MDVP:Jitter()=st.number_input('MDVP:Jitter(%) value')
	MDVP:Jitter(Abs)=st.number_input('MDVP:Jitter(Abs) value')
	MDVP:RAP=st.number_input('MDVP:RAP value')
	MDVP:PPQ=st.number_input('MDVP:PPQ value')
	Jitter:DDP=st.number_input('Jitter:DDP value')
	MDVP:Shimmer=st.number_input('MDVP:Shimmer value')
	MDVP:Shimmer(dB)=st.number_input('MDVP:Shimmer(dB) value')
	Shimmer:APQ3=st.number_input('Shimmer:APQ3 value')
	Shimmer:APQ5=st.number_input('Shimmer:APQ5 value')
	MDVP:APQ=st.number_input('MDVP:APQ value')
	Shimmer:DDA=st.number_input('Shimmer:DDA value')
	NHR=st.number_input('NHR value')
	HNR=st.number_input('HNR value')
	RPDE=st.number_input('RPDE value')
	DFA=st.number_input('DFA value')
	spread1=st.number_input('spread1 value')
	spread2=st.number_input('spread2e value')
	D2=st.number_input('D2 value')
	PPE=st.number_input('PPE value')


	#code for prediction
	diagnosis=''
 
	#creating a button for prediction
	if st.button('Heart Test Result'):
		diagnosis=parkinsons_prediction([MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])


	st.success(diagnosis)


if __name__ == '__main__':
	main()
