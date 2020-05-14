#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:50:04 2020

@author: redeye
"""
from tkinter import * 
import sys
import numpy as np
import pandas as pd
from pandas import datetime
import matplotlib.pyplot as plt
from sql import *
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from model_call_1 import *
from functools import partial
#from statsmodels.graphics.tsaplots import plot_acf