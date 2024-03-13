import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn-v0_8')

import yfinance as yf

GameStop = yf.Ticker('GME')

stockinfo = GameStop.info

for key,value in stockinfo.items():
   print(key, ":", value)

numshares = GameStop.info['sharesOutstanding']
print(numshares)

df = GameStop.dividends
data = df.resample('Y').sum()
data = data.reset_index()

data['Year'] = data['Date'].dt.year

plt.figure()
plt.bar(data['Year'],data['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title('GameStop Dividend History')
plt.xlim(2003,2023)
plt.show()





