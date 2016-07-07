import datetime

import numpy as np 

import matplotlib.pyplot as plt 

from matplotlib.finance import quotes_historical_yahoo_ochl

from hmmlearn.hmm import GaussianHMM

quotes = quotes_historical_yahoo_ochl("INTC",datetime.date(1994,4,5),datetime.date(2015,7,3))


dates = np.array([quote[0] for quote in quotes],dtype=np.int)

closing_values=np.array([quote[2] for quote in quotes])
volume_of_shares=np.array([quote[5] for quote in quotes])[1:]


diff_percentage = 100.0*np.diff(closing_values)/closing_values[:-1]

dates=dates[1:]


X=np.column_stack([diff_percentage,volume_of_shares])

print("\nTraining HMM")

model = GaussianHMM(n_components=5,covariance_type="diag",n_iter=10000)

model.fit(X)

num_samples=500
samples,_=model.sample(num_samples)
plt.plot(np.arange(num_samples),samples[:,0],c='black')

plt.show()