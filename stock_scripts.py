# annual returns
from pandas_datareader import data as web
spy = web.DataReader('^GSPC', 'yahoo', start='01/01/1968', end='12/01/2016')['Adj Close']
annual_returns = spy.resample('AS', how=lambda x: x[-1])
annual_returns.pct_change()

import numpy as np
from pandas import DataFrame
import pandas.io.data as web


all_data = {}
for ticker in ['MCD', 'GPC', 'TGNA', 'DIS', 'TGT', 'VFC', 'MAT', 'SNA', 'SWK', 'LB', 'LOW', 'PHM', 'HAS', 'TJX', 'JCI', 'GPS', 'JWN', 'HD', 'NKE', 'NWL', 'IPG', 'CBS', 'AMZN', 'RL', 'EXPE', 'SNI', 'WYNN', 'ORLY', 'PCLN', 'ROST', 'URBN', 'DISCA', 'KMX', 'CMG', 'BWA', 'DLTR', 'TRIP', 'DG', 'GRMN', 'DLPH', 'PVH', 'GM', 'FOXA', 'FOX', 'NWSA', 'NWS', 'KORS', 'MHK', 'TSCO', 'UA', 'DISCK', 'RCL', 'HBI', 'AAP', 'SIG', 'FL', 'ULTA', 'LKQ', 'AN', 'AZO', 'BBBY', 'BBY', 'CCL', 'COH', 'CMCSA', 'DHI', 'DRI', 'F', 'GT', 'HOG', 'HAR', 'KSS', 'LEN', 'M', 'MAR', 'OMC', 'SPLS', 'SBUX', 'HOT', 'TIF', 'TWX', 'VIAB', 'WHR', 'WYN', 'YUM']:
all_data[ticker]= web.DataReader(ticker, 'yahoo', start='01/01/2012', end='01/01/2016')
price = DataFrame({tic: data['Adj Close']
    for tic, data in all_data.items()})
annual_returns = price.resample('AS', how=lambda x: x[-1])
df = annual_returns.pct_change()
df.to_csv('stock_returns_b.csv')


import pandas.io.data as web
import pandas as pd

tics = ['SPY', 'ABBV', 'WMT', 'PEP', 'INTU', 'CRM', 'INTC', 'ADP', 'GE', 'BIIB', 'CVS', 'OXY', 'TJX', 'HSY', 'SJM']
data = {}
df = pd.DataFrame(data)
for t in tics:
    J = web.DataReader(t, 'yahoo', start='01/01/2009', end='01/01/2016')['Adj Close']
    annual_returns = J.resample('AS').apply(lambda x: x[-1])
    df[t] = annual_returns.pct_change()
df['portfolio']= df.mean(axis=1)   
df



import datetime
from pandas_datareader.data import DataReader
import numpy as np
from decimal import Decimal, InvalidOperation, DivisionByZero
from pandas_datareader._utils import RemoteDataError
import pandas as pd
from pandas_datareader import data, wb
import pandas as pd
tics = ['XOM','GE','WMT','V']
data = {}
df = pd.DataFrame(data)
for t in tics:
    try:
        s = web.DataReader(t, 'yahoo', start='01/01/2009', end='01/01/2016')['Adj Close']
        annual_returns = s.resample('AS').apply(lambda x: x[-1])
        annual = annual_returns.pct_change()
        today = 0.134577576
        data= {'stock':t, 'today':today, 'max':annual.max(), 'min':annual.min(), 'diff':today-annual.min()}
        s = pd.Series(data)
        result = []
        if s['diff'] <= .60:
            result.append({t:s.values})
    except(OSError, RemoteDataError, InvalidOperation, DivisionByZero) as e:
        print('{0} {1}'.format(t, 'something went wrong'))
        
for v in result:
    print(v)
		
# helper functions
tic = ['PSX']
values = [67.45, 34.23]

def func(stk, alist):
    returns=[]
    for a, b in zip(alist[::1], alist[1::1]):
        returns.append((b - a) / a)

    result = dict(zip(stk, returns))
    r = pd.Series(result).transpose()
    return pd.DataFrame(r).T
    return r
func(tic, values)

def addweighted(a, b):
    return (a*.8) + (b*.2)

x = -.2
y = .01
addweighted(x, y )

tic = ['PSX']
values = [67.45, 34.23]
data = {}
# data[tic[0]] = values
def func(stk, alist):
    returns=[]
    for a, b in zip(alist[::1], alist[1::1]):
        returns.append((b - a) / a)

    result = dict(zip(stk, returns))
    r = pd.Series(result).transpose()
    return pd.DataFrame(r).T
    return r
func(tic, values)

import numpy as np
import pandas.io.data as web


tic = 'BSX'
s = web.DataReader(tic, 'yahoo', start='01/01/1996', end='10/10/2016')['Adj Close']
annual_returns = s.resample('AS').apply(lambda x: x[-1])
annual = annual_returns.pct_change()
today = 0.134577576
# print('today: {}'.format(today))
# print('max:   {}'.format(annual.max()))
# print('min:   {}'.format(annual.min()))
# print('diff:  {}'.format(today - annual.min())) # .20 of less
data= {'stk':tic, 'today':today, 'max':annual.max(), 'min':annual.min(), 'diff':today-annual.min()}
df = pd.DataFrame(data, index=[0])
df

prices = [30.4, 32.5]
for a, b in zip(prices[::1], prices[1::1]):
    print((b - a) / a)
#Edit: If you want this as a list, you could do this:
print([(b - a) / a for a, b in zip(prices[::1], prices[1::1])])
#0.0690789473684211
#[0.0690789473684211]