import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn-v0_8')

import yfinance as yf

tesla = yf.Ticker('TSLA')

stockinfo = tesla.info

for key,value in stockinfo.items():
   print(key, ":", value)

numshares = tesla.info['sharesOutstanding']
print(numshares)

df = tesla.dividends
data = df.resample('Y').sum()
data = data.reset_index()

data['Year'] = data['Date'].dt.year

plt.figure()
plt.bar(data['Year'],data['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title('Tesla Dividend History')
plt.xlim(2003,2023)
plt.show()





