import datetime
import ystockquote

from pandas_datareader.data import DataReader
import numpy as np
from decimal import Decimal, InvalidOperation, DivisionByZero
import urllib2
from pandas_datareader._utils import RemoteDataError
import pandas as pd

path = r'C:\Users\matt\Desktop\stocks\products.txt'
 
with open(path,'r') as f:
    stk_tickers = f.readlines()
       
  
stk = [t.strip('\n').strip('\r') for t in stk_tickers]
tickers = list(set(stk))

ticker_list = tickers
    
#print('{0}    {1}    {2}    {3}   {4}    {5}    {6}'.format('Ticker', 'EPS', 'Yield', 'Dividend', 'Price', 'Book', 'MCap'))



def get_data(ticker):

        try:
            eps = ystockquote.get_earnings_per_share(ticker) 
            
            _yield = ystockquote.get_dividend_yield(ticker)
            
            div = ystockquote.get_dividend_per_share(ticker)
               
            book = ystockquote.get_book_value(ticker)
            
            mcap = ystockquote.get_market_cap(ticker)
            mcap = mcap[:-1]
            
            price = ystockquote.get_price(ticker)
            
            values = [ticker, eps, _yield, div, price, book, mcap]

            return values

            #return '{0}  {1}  {2}  {3}  {4}  {5}  {6}'.format(ticker, eps, _yield, div, price, book, mcap)
    
    
        except(RemoteDataError, urllib2.HTTPError, InvalidOperation, DivisionByZero) as e:
            print('{0} {1}'.format(ticker, 'something went wrong'))
    
            return None
"""
a1 = ['a','b','c','d','e','f','g']
a2 = ['i','j','k','l','m','n','o']
a3 = ['t','u','v','w','x','y','z']

a = pd.Series(data=a1)
b = pd.Series(data=a2)
c = pd.Series(data=a3)

aa = a.to_frame()
bb = b.to_frame()
cc = c.to_frame()

frames = [aa.T,bb.T,cc.T]

result = pd.concat(frames)

print(result)
"""
alist = []
for t in ticker_list:
    a1 = get_data(t)
    
    a = pd.Series(data=a1, index=['ticker', 'eps', '_yield', 'div', 'price', 'book', 'mcap'])
    
    aa = a.to_frame()
    
    alist.append(aa.T)
    
    result = pd.concat(alist)

# print(result)
result.to_excel(r'G:\DOCUMENTS\Securities Analysis\ystockquote_data\yahoo_stock_11_21_16.xlsx')

print('finished')