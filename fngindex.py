import requests, csv, json, urllib
import pandas as pd
import time
from fake_useragent import UserAgent
from datetime import datetime

BASE_URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata/"
START_DATE = '2020-09-19'
END_DATE = '2022-06-02'
ua = UserAgent()

headers = {
   'User-Agent': ua.random,
   }

r = requests.get(BASE_URL + START_DATE, headers = headers)
data = r.json()

fng_data = pd.read_csv('fear-greed.csv', usecols=['Date', 'Fear Greed'])
fng_data['Date'] = pd.to_datetime(fng_data['Date'], format='%Y-%m-%d')  

fng_data.set_index('Date', inplace=True)
missing_dates = []
all_dates = (pd.date_range(fng_data.index[0], END_DATE, freq='D'))
for date in all_dates:
	if date not in fng_data.index:
		missing_dates.append(date)
		#print(date)
		fng_data.loc[date] = [0]
fng_data.sort_index(inplace=True)


for data in ((data['fear_and_greed_historical']['data'])):
	x = int(data['x'])
	x = datetime.fromtimestamp(x / 1000).strftime('%Y-%m-%d')
	y = int(data['y'])
	fng_data.at[x, 'Fear Greed'] = y
#currently any days that do not have data points from cnn are filled with zeros, uncomment the following line to backfill
#fng_data['Fear Greed'].replace(to_replace=0, method='bfill')

fng_data.to_pickle('all_fng.pkl')
fng_data.to_csv('all_fng_csv.csv')

