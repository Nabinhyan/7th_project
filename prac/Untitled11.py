import numpy as np
import pandas as pd
from pandas import datetime
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
#import Untitled11
def parser(x):
    return datetime.strptime(x,'%Y-%m')


data=pd.read_csv('importofrice.csv', index_col=0 ,parse_dates = [0], date_parser = parser)
training_data = data[:round(len(data)*0.85)]
test_data = data[round(len(data)*0.85):]
len_training = len(training_data)
training_data_logscale = np.log(training_data)




datasetlogdiffshifting = training_data_logscale - training_data_logscale.shift()
datasetlogdiffshifting.dropna(inplace=True)
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
model = ARIMA(training_data_logscale,order=(1,1,4))
results_ar = model.fit(disp=-1)
rss = np.log(sum((results_ar.fittedvalues-datasetlogdiffshifting["Quantity"])**2))
print('RSS: %.4f'% rss)







#pred is prediction
pred=results_ar.forecast(steps = 60)[0]
pred_list = pred.tolist() #typing casting array type to list
pred_series = pd.Series(pred_list, copy = False) #typecasting list to series
pred_series=np.exp(pred_series)
training_data_copy = training_data
training_data_copy=training_data_copy.reset_index()
for x in range(len(pred_series)):
    if(training_data_copy.Month[len(training_data_copy)-1].month < 12):
        pred_month = training_data_copy.Month[len(training_data_copy)-1].month + 1
        pred_year = training_data_copy.Month[len(training_data_copy)-1].year
    else:
        pred_year = training_data_copy.Month[len(training_data_copy)-1].year + 1 
        pred_month = 1
    pred_date = '{}-{}'.format(pred_year,pred_month)
    pred_date = datetime.strptime(pred_date, '%Y-%m')
    training_data_copy = training_data_copy.append({'Month': pred_date, 'Quantity': pred_series[x]}, ignore_index=True)

training_data_copy.set_index("Month", inplace = True)
original_data_plot = training_data_copy[:len_training]
predicted_data = training_data_copy[len_training:]
plt.figure(figsize=(6,4), dpi=100)
plt.xlabel("Date")
plt.ylabel("Quantity in kg")
plt.plot(original_data_plot,color = 'black', label='training')
plt.plot(test_data, color = 'blue', label='Actual Test Data')
plt.plot(predicted_data, color = 'red',label='Prediction')
plt.grid()
plt.legend(loc='best')




