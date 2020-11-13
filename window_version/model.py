import numpy as np
import pandas as pd
from pandas import datetime
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from functools import partial
import pymysql
global screen
global canvas
from time import sleep
def model_calll(window, called_item, model_status, passed_value, graph_status):
    global read_data, process_to_do, calling_status, graph_to_print, title_print_first_word, p, d, q, graph_staus
    # db = pymysql.connect("localhost","root","","7th_project" )
    if called_item == "Rice":
        read_data = pd.read_csv("dataset/rice.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Import"
        p = 21
        d = 1
        q = 5

    elif called_item == "Potato":
        read_data = pd.read_csv("dataset/potato.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Import"
        p = 21
        d = 1
        q = 5

    elif called_item == "Apple":
        read_data = pd.read_csv("dataset/apple.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Import"
        p = 27
        d = 1
        q = 2

    elif called_item == "Tea":
        read_data = pd.read_csv("dataset/tea.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Export"
        p = 14
        d = 1
        q = 3

    elif called_item == "Alainchi":
        read_data = pd.read_csv("dataset/alainchi.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Export"
        p = 16
        d = 1
        q = 4
    
    elif called_item == "Herbs":
        read_data = pd.read_csv("dataset/herbs.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Export"
        p = 20
        d = 1
        q = 8


    calling_status = model_status
    graph_type = passed_value

    data= read_data.reset_index()
    data['Month'] = pd.to_datetime(data["Month"])
    data.set_index("Month", inplace = True)
    # data['Quantity'] = data['Quantity'] / 1000
    # print(data['Quantity'])
    training_data = data[:round(len(data)*0.85)]
    test_data = data[round(len(data)*0.85):]
    len_training = len(training_data)
    training_data_logscale = np.log(training_data)

    # training_data_logscale = np.log(training_data)
    movingavg = training_data_logscale.rolling(window=12).mean()
    movingstd = training_data_logscale.rolling(window=12).std()
    datasetlogscalemovingavg = training_data_logscale - movingavg
    datasetlogscalemovingavg.dropna(inplace=True)
    exp_decay_wt_avg = training_data_logscale.ewm(
        halflife=12, min_periods=0, adjust=True).mean()
    data_logscale_minus_moving_exp_decay_avg = training_data_logscale - exp_decay_wt_avg
    datasetlogdiffshifting = training_data_logscale - training_data_logscale.shift()
    datasetlogdiffshifting.dropna(inplace=True)



    def graph_print(called_status, graph_to_print, training_data, test_data, len_training, datasetlogdiffshifting):
        results_ar = ARIMAResults.load("trained_model/"+called_item+".pkl")
        global original_data_plot, predicted_data

        rss = np.log(sum((results_ar.fittedvalues-datasetlogdiffshifting["Quantity"])**2))
        if called_status == 0:

            #making prediction
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
            predicted_data.to_csv("predicted_data/"+called_item+".csv", index = True, header = True)
        fig = plt.figure(figsize=(7, 4), dpi=90)
        plt.title(f'{title_print_first_word} of {called_item} with RSS Error: {rss:.4f}')
        if(graph_to_print == "Line Graph"):
            plt.plot(original_data_plot, color='black', label="Training Data")
            plt.plot(test_data, color='blue', label="Actual Data")
            plt.plot(predicted_data, color='red', label="Predicted Data")
        elif(graph_to_print == "Scatter Graph"):
            plt.scatter(original_data_plot.index.values, original_data_plot['Quantity'], s=10, color='black', label="Training Data")
            plt.scatter(test_data.index.values, test_data['Quantity'], s=10, color='blue', label="Actual Data")
            plt.scatter(predicted_data.index.values, predicted_data['Quantity'], s=10, color='red', label="Predicted Data")
            rolmean = training_data.rolling(window = 12).mean()
            plt.plot(rolmean, color = 'green', label = "mean line")            

        plt.xlabel("Date")
        plt.ylabel("Quantity in Kg")
        plt.legend(loc='best')
        plt.grid()
        # You can make your x axis labels vertical using the rotation

        # specify the window as master
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=30, column=5, columnspan=4,
                                    padx=0, pady=0, ipadx = 27, ipady = 30)
        
        called_status = 1
        return called_status, canvas

    if(passed_value == "Reload Model"):
        graph_type = "Line Graph"
        
        model = ARIMA(training_data_logscale, order=(p, d, q))
        results_ar = model.fit(disp=-1)
        results_ar.save("trained_model/"+called_item+".pkl")


        model_status, canvas= graph_print(calling_status, graph_type, training_data, test_data, len_training, datasetlogdiffshifting)
        graph_staus.append("1")
        return model_status, graph_staus
    else:
        model_status, canvas= graph_print(calling_status, graph_type,training_data, test_data, len_training, datasetlogdiffshifting)
        graph_status.append(canvas)
        return model_status, graph_status
