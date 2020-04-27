import numpy as np
import pandas as pd
from pandas import datetime
#import matplotlib.pylab as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA



import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from functools import partial
global screen
global canvas




def model_calll(window, model_status, called_item, graph_type):
    print(model_status)
    global called_csv, graph_to_print, original_data_plot, test_data, predicted_data
    if called_item == "Rice":
        called_csv = "rice.csv"
    elif called_item == "Potato":
        called_csv = "potato.csv"
    elif called_item == "Apple":
        called_csv = "apple.csv"
    
    graph_to_print = graph_type
    
    def graph_print():
        fig = plt.figure(figsize=(3.7, 3), dpi = 100)
        plt.title("Import of ...... ")
        if(graph_to_print == "Line Graph"):
            plt.plot(original_data_plot,color = 'black', label = "Training Data")
            plt.plot(test_data, color = 'blue', label = "Actual Data")
            plt.plot(predicted_data, color = 'red', label = "Predicted Data")
        elif(graph_to_print == "Scatter Graph"):
            plt.scatter(original_data_plot.index.values, original_data_plot['Quantity'], s = 10, color = 'black', label = "Training Data")
            plt.scatter(test_data.index.values, test_data['Quantity'], s = 10, color = 'blue', label = "Actual Data")
            plt.scatter(predicted_data.index.values, predicted_data['Quantity'], s = 10, color = 'red', label = "Predicted Data")
#            plt.show()
        plt.xlabel("Date")
        plt.ylabel("Quantity in Kg")
        plt.legend(loc='best')
        # You can make your x axis labels vertical using the rotation
        
        # specify the window as master
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0,columnspan = 3, padx=6, pady=3, ipadx = 20, ipady = 11)
        model_status = 1
        return model_status
    
    
    if(model_status == 0):
        def parser(x):
            return datetime.strptime(x, '%Y-%m')
        data = pd.read_csv(called_csv, index_col=0,parse_dates=[0], date_parser=parser)
        training_data = data[:round(len(data)*0.85)]
        test_data = data[round(len(data)*0.85):]
        len_training = len(training_data)
        training_data_logscale = np.log(training_data)
        movingavg = training_data_logscale.rolling(window=12).mean()
        movingstd = training_data_logscale.rolling(window=12).std()
        datasetlogscalemovingavg = training_data_logscale - movingavg
        datasetlogscalemovingavg.dropna(inplace=True)
        def test_stationarity(timeseries):
            movingavg = timeseries.rolling(window=12).mean()
            movingstd = timeseries.rolling(window=12).std()
            print('Result of Dickey-Fuller Test:')
            dftest = adfuller(training_data['Quantity'], autolag='AIC')
            dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        exp_decay_wt_avg = training_data_logscale.ewm(
            halflife=12, min_periods=0, adjust=True).mean()
        data_logscale_minus_moving_exp_decay_avg = training_data_logscale - exp_decay_wt_avg
        datasetlogdiffshifting = training_data_logscale - training_data_logscale.shift()
        datasetlogdiffshifting.dropna(inplace=True)
        model = ARIMA(training_data_logscale, order=(21, 1, 4))
        results_ar = model.fit(disp=-1)
        rss = np.log(
            sum((results_ar.fittedvalues-datasetlogdiffshifting["Quantity"])**2))
        print('RSS: %.4f' % rss)
        predic_arima_diff = pd.Series(results_ar.fittedvalues, copy=False)
        predic_arima_diff_cumsum = predic_arima_diff.cumsum()
        predic_arima_log = pd.Series(training_data_logscale['Quantity'], index=training_data_logscale.index)
        predic_arima_log = predic_arima_log.add(predic_arima_diff_cumsum, fill_value=0)
        pred = results_ar.forecast(steps=60)[0]
        y = pred.tolist()
        s = pd.Series(y, copy=False)
        s = np.exp(s)
        training_data = training_data.reset_index()
        for x in range(len(s)):
            if(training_data.Month[len(training_data)-1].month < 12):
                m = training_data.Month[len(training_data)-1].month + 1
                y = training_data.Month[len(training_data)-1].year
            else:
                y = training_data.Month[len(training_data)-1].year + 1
                m = 1
            d = '{}-{}'.format(y, m)
            d = datetime.strptime(d, '%Y-%m')
            training_data = training_data.append(
                {'Month': d, 'Quantity': s[x]}, ignore_index=True)
        training_data.set_index("Month", inplace=True)
        original_data_plot = training_data[:len_training]
        predicted_data = training_data[len_training:]
        graph_print()
    
    else:
        graph_print()








