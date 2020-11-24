import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ochl
import pandas as pd
import os
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 11, 23)
symbol = input("Please insert a VALID Stock symbol")
df = web.DataReader('{}'.format(symbol), 'yahoo', start, end)


df = pd.read_csv('{}.csv'.format(str(symbol)), parse_dates=True, index_col=0)
#df['100ma'] = df['Adj Close'].rolling(window=100).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
print(df_ohlc.tail())

#Graphs
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()
candlestick_ochl(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()
