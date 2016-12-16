from datetime import datetime, timedelta
from pandas_datareader import data, wb

class Portfolio:
    
    """
    Accumulates stock tickers, retrieves price data from Yahoo Finance
    and returns a porfolio of stock returns.
    """
    
    def __init__(self, tickers, start, end=None):
        self.tickers = tickers
        self.start = start
        if end == None:
            end = str((datetime.today() - timedelta(days=1)).strftime("%m/%d/%Y"))
        self.end = end
        self.pdata = pd.Panel(dict((stk, data.get_data_yahoo\
                                   (stk, self.start, self.end))
                                    for stk in self.tickers))
        
    def append(self, ticker):
        self.tickers.append(ticker)
    
    def extend(self, *tickers):
        self.tickers.extend(tickers)
    
    def remove(self, ticker):
        self.tickers.remove(ticker)
        
    def _calc_return(self, x, y):
        return (y-x) / x
        
    def _api_data(self):
        """Returns pandas Panel of percentages for period."""
        pdata = self.pdata.swapaxes('items', 'minor')
        a = pdata.ix['Adj Close', self.start]
        b = pdata.ix['Adj Close', self.end]         
        stocks = self._calc_return(a, b)
        return stocks
    
    def mean(self):
        """Return the mean of all the values in the portfolio."""
        portfolio = self._api_data()
        return portfolio.mean()
        
    def __repr__(self):
        return str(self._api_data())