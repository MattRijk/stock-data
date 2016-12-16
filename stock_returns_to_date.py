from pandas_datareader import data, wb

tickers = ['A', 'BAC', 'F', 'GE', 'IBM']
pdata = pd.Panel(dict((stk, data.get_data_yahoo(stk, '1/1/2013', '5/7/2016'))
                     for stk in tickers))
pdata = pdata.swapaxes('items', 'minor')

x = pdata.ix['Adj Close', '5/1/2013']
y = pdata.ix['Adj Close', '5/2/2016']

print(x); print; print(y)

def three_year_returns(a,b):
    return (b-a)/a

three_year_returns(x, y)


import pandas.io.data as web
tickers = ['SPY','XOM','GE','WMT','MCD']
pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2014', '5/7/2016'))
                     for stk in tickers))

pdata = pdata.swapaxes('items', 'minor')
x = pdata.ix['Adj Close', '5/1/2014']
y = pdata.ix['Adj Close', '5/2/2016']


def three_year_returns(a,b):
    return (b-a)/a

three_year_returns(x, y)


# CORRELATION
import numpy as np
from pandas import DataFrame
import pandas.io.data as web

all_data = {}
for ticker in ['GE','JNJ','AMZN','XOM','MSFT','SPY']:
    all_data[ticker]= web.get_data_yahoo(ticker, '1/02/2013', '05/15/2015')
price = DataFrame({tic: data['Adj Close']
                    for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume']
                    for tic, data in all_data.iteritems()})
returns = price.pct_change()
x = returns.corr()
print(x)

# GRAPHS AND PLOTS
def get(tickers, start, end):
    def data(ticker):
        return pd.io.data.DataReader(ticker, 'yahoo', start, end)
    datas = map(data, tickers)
    return pd.concat(datas, keys=tickers, names=['Ticker','Date'])  

tickers = ['AAPL','MSFT','GE','IBM','AA','DAL','UAL', 'PEP', 'KO']
all_data = get(tickers, start, end)
all_data[:5]

just_closing_prices = all_data[['Adj Close']].reset_index()
just_closing_prices[:5]

just_closing_prices['Return'].hist(bins=50,figsize=(12,8));

v = np.random.normal(size=100)

from scipy.stats import norm  
df = pd.DataFrame({'A': data})

df.A.plot(kind='hist', normed=True)

range = np.arange(-5, 5, 1)
plt.plot(range, norm.pdf(range,-100,100))