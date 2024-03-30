import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mp
import seaborn as sb
stocks=input("enter yahoo finance code for the stock:")
data=yf.download(stocks, "2020-3-1", "2021-1-26", auto_adjust=True)
data.head()
