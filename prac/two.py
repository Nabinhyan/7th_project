import numpy as np
import pandas as pd
from pandas import datetime
from datetime import datetime
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA

def prediction_my(results_ar, training_data, test_data, predction_period):
    pred=results_ar.forecast(steps = predction_period)[0]
    y = pred.tolist()
    s = pd.Series(y, copy = False)
    s=np.exp(s)
    training_data=training_data.reset_index()
    
    for x in range(len(s)):
        if(training_data.Month[len(training_data)-1].month < 12):
            m = training_data.Month[len(training_data)-1].month + 1
            y = training_data.Month[len(training_data)-1].year
        else:
            y = training_data.Month[len(training_data)-1].year + 1 
            m = 1
        d = '{}-{}'.format(y,m)
        d = datetime.strptime(d, '%Y-%m')
        training_data = training_data.append({'Month': d, 'Quantity': s[x]}, ignore_index=True)
    
    training_data.set_index("Month", inplace = True)
    original_data_plot = training_data[:len(training_data)]
    predicted_data = training_data[len(training_data):]
    plt.figure(figsize=(6,4), dpi=100)
    plt.xlabel("Date")
    plt.ylabel("Quantity in kg")
    plt.plot(original_data_plot,color = 'black', label='training')
    plt.plot(test_data, color = 'blue', label='Actual Test Data')
    plt.plot(predicted_data, color = 'red', label='Prediction')
    plt.grid()
    plt.legend(loc='best')
        