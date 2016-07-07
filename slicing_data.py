import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from timeseries import convert_data_to_timeseries

input_file='data_timeseries.txt'


column_num=2

data_timeseries=convert_data_to_timeseries(input_file,column_num)


start='2008'
end='2015'


plt.figure()
data_timeseries[start:end].plot()

plt.title('Data from '+start+'to'+end)

start='2007-2'

end='2007-11'

plt.figure()

data_timeseries[start:end].plot()

plt.title('data from'+start+'to'+end)

plt.show()