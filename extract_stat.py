import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from timeseries import convert_data_to_timeseries

input_file = 'data_timeseries.txt'


data1 = convert_data_to_timeseries(input_file, 2)
data2 = convert_data_to_timeseries(input_file, 3)

dataframe = pd.DataFrame({'first': data1, 'second': data2})


print ('\nMaximum:\n', dataframe.max())
print ('\nMinimum:\n', dataframe.min())

print ('\nMean:\n', dataframe.mean())
print ('\nMean row-wise:\n', dataframe.mean(1)[:10])


pd.rolling_mean(dataframe, window=24).plot()


print ('\nCorrelation coefficients:\n', dataframe.corr())


plt.figure()
pd.rolling_corr(dataframe['first'], dataframe['second'], window=60).plot()

plt.show()
