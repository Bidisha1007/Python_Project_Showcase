# -*- coding: utf-8 -*-
"""Covid-19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZNli25IGoHQ1_uHbsNXJDGy8uVnhEZFl
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot  as plt
import matplotlib.dates as mdates

# %matplotlib inline
plt.style.use('fivethirtyeight')

df=pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv',parse_dates=['Date'])
df['Total Cases']=df[['Confirmed','Recovered','Deaths']].sum(axis=1)

#Worldwide Cases

worldwide_df = df.groupby(['Date']).sum()
w= worldwide_df.plot(figsize=(8,10))
w.set_xlabel('Date')
w.set_ylabel('# of cases worldwide')
w.title.set_text('Worldwide COVID Insights')

plt.show()

us_df = df[df['Country']=='US'].groupby(['Date']).sum()
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)

ax.plot(worldwide_df[['Total Cases']],label='Worldwide')
ax.plot(us_df[['Total Cases']],label='United States')
ax.set_xlabel('Date')
ax.set_ylabel('# of total cases ')
ax.title.set_text('Worldwide vs. United States total cases')
plt.legend(loc='upper left')
plt.show()

India_df = df[df['Country']=='India'].groupby(['Date']).sum()
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)

ax.plot(worldwide_df[['Total Cases']],label='Worldwide')
ax.plot(us_df[['Total Cases']],label='India')
ax.set_xlabel('Date')
ax.set_ylabel('# of total cases ')
ax.title.set_text('Worldwide vs.India total cases')
plt.legend(loc='upper left')
plt.show()

#India daily cases and death
India_df = India_df.reset_index()
India_df ['Daily Confirmed'] = India_df ['Confirmed'].sub(India_df ['Confirmed'].shift())
India_df ['Daily Deaths'] = India_df ['Deaths'].sub(India_df ['Deaths'].shift())
India_df

fig = plt.figure(figsize=(20,12))
ax= fig.add_subplot(111)

ax.bar(India_df ['Date'],India_df['Daily Confirmed'],color='b',label='India daily confirm cases')
ax.bar(India_df ['Date'],India_df['Daily Deaths'],color='r',label='India daily Deaths')
ax.set_xlabel('Date')
ax.set_ylabel('# of people affected ')
ax.title.set_text('India daily cases and death')
plt.legend(loc='upper left')

plt.show()

from datetime import date, timedelta
last_recorded_date= "2022-04-16"
#yesterday = date.today() - timedelta(days=1)
#yesterday.strftime('%Y-%m-%d')

today_df = df[df['Date'] ==last_recorded_date]
top_10 = today_df.sort_values(['Confirmed'],ascending=False)[:10]
top_10.loc['rest-of-world'] = today_df.sort_values(['Confirmed'],ascending=False)[10:].sum()
top_10.loc['rest-of-world','Country']='Rest Of World'
top_10

fig = plt.figure(figsize=(10,10))
ax= fig.add_subplot(111)
ax.pie(top_10['Confirmed'],labels=top_10['Country'],autopct='%1.1f%%')
ax.title.set_text('Hardest Hit Countries Worldwide')

plt.legend(loc='upper left',fontsize='7')
plt.show()
