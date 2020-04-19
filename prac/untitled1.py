import numpy as np
import pandas as pd
from pandas import datetime
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import Untitled11
def parser(x):
    return datetime.strptime(x,'%Y-%m')


data=pd.read_csv('importofrice.csv', index_col=0 ,parse_dates = [0], date_parser = parser)
training_data = data[:round(len(data)*0.85)]
test_data = data[round(len(data)*0.85):]
len_training = len(training_data)
training_data_logscale = np.log(training_data)
results_ar = Untitled11.model_arima_define(training_data_logscale)