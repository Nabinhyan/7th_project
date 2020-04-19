import numpy as np
import pandas as pd
from pandas import datetime
from datetime import datetime
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA

c=15
global test_data
global results_ar

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
        
    
    
def parser(x):
    return datetime.strptime(x,'%Y-%m')

data=pd.read_csv('importofrice.csv', index_col=0 ,parse_dates = [0], date_parser = parser)
training_data = data[:round(len(data)*0.85)]
test_data = data[round(len(data)*0.85):]

training_data_logscale = np.log(training_data)
movingavg = training_data_logscale.rolling(window=12).mean()
movingstd = training_data_logscale.rolling(window=12).std()
datasetlogscalemovingavg = training_data_logscale - movingavg
datasetlogscalemovingavg.dropna(inplace=True)

def test_stationarity(timeseries):
    movingavg = timeseries.rolling(window=12).mean()
    movingstd = timeseries.rolling(window=12).std()
    
datasetlogdiffshifting = training_data_logscale - training_data_logscale.shift()
datasetlogdiffshifting.dropna(inplace=True)

def give():
    return c
    return results_ar

model = ARIMA(training_data_logscale,order=(2,1,3))
results_ar = model.fit(disp=-1)
rss = np.log(sum((results_ar.fittedvalues-datasetlogdiffshifting["Quantity"])**2))
print('Resudial Sum of Square: %.4f'% rss)

predction_period = int(input('Enter the time peroid to prediction::'))
prediction_my(results_ar, training_data, test_data, predction_period)
