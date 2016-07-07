import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from timeseries import convert_data_to_timeseries 


input_file='data_timeseries.txt'

data1 = convert_data_to_timeseries(input_file,2)

data2 = convert_data_to_timeseries(input_file,3)

dataframe=pd.DataFrame({'first':data1,'second':data2})


dataframe['1952':'1955'].plot()

plt.title('data overlapped on top of each other')


plt.figure()

difference=dataframe['1952':'1955']['first']-dataframe['1952':'1955']['second']


difference.plot()
plt.title('Difference(first-second)')

dataframe[(dataframe['first'] > 60) & (dataframe['second'] < 20)].plot()
plt.title('first > 60 and second < 20')

plt.show()