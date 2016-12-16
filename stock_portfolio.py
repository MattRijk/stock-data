from pandas.io.data as web

class Portfolio:
	""" """
	def __init__(self, tickers, start, end=None): 
		""" """
		self.tickers = tickers
		self.start = start
		if end is None:
			self.end = datetime.today()
		self.end = end
		data = pd.Panel(dict((stk, web.get_data_yahoo(stk, start, end))
								   for stk in tickers)) 
		data = data.swapaxes('items', 'minor')
		data = data['Adj Close', '1/14/16']
		data.to_dict()
		self.data = data
		
		
	def __getitem__(self, ticker):
		item = self.data[ticker]
		return item

	def __setitem__(self):pass

	def append(self, ticker):pass
	
	def __delitem__(self):pass
# interface
	
p1 = Portfolio(['XOM','T','GE','MCD','WMT'], '1/14/16')
	
p1

