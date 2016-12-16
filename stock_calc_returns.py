import pandas as pd
import numpy as np
from pandas_datareader import data, wb
from datetime import datetime
import scipy as sp
import scipy.optimize as scopt
import scipy.stats as spstats
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
%matplotlib inline

def get_historical_closes(ticker, start_date, end_date):
    p = data.DataReader(ticker, "yahoo", start_date, end_date)
    d = p.to_frame()['Adj Close'].reset_index()
    d.rename(columns={'minor': 'Ticker',
        'Adj Close': 'Close'}, inplace=True)
    pivoted = d.pivot(index='Date', columns='Ticker')
    pivoted.columns = pivoted.columns.droplevel(0)
    return pivoted
	
closes = get_historical_closes(['MSFT', 'AAPL', 'KO'],
'2010-01-01', '2014-12-31')
closes[:5]

def calc_daily_returns(closes):
    return np.log(closes/closes.shift(1))
		
daily_returns = calc_daily_returns(closes)
daily_returns[:5]

def calc_annual_returns(daily_returns):
    grouped = np.exp(daily_returns.groupby(
    lambda date: date.year).sum())-1
    return grouped

annual_returns = calc_annual_returns(daily_returns)
annual_returns

price = data.get_data_yahoo('AAPL', '2011-01-01')['Adj Close']
price[-5:]

annual_ret = (price['2015-12-31']  - price['2011-03-01'])  / price['2011-03-01']
annual_ret
# 1.2654126017673533

