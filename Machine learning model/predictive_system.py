# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pickle

#loading the asved model
loaded_model=pickle.load(open('C:/Users/Dell/Desktop/import/diabetes_model.sav','rb'))

input = (1,122,90,51,220,49.7,0.325,31)
#changing the to the numpy array
numpy_input = np.asarray(input)
#have to reshape the numpy input because we are predicting for only one entry of the complete dataset
numpy_reshaped = numpy_input.reshape(1,-1)

prediction = loaded_model.predict(numpy_reshaped)
print(prediction)

if(prediction[0]==0):
	print('Patient is non-diabetic')
else:
	print('Patient is diabetic')











