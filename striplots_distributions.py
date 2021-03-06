
"""Part II"""

import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px


#open file the energy file
energy=pd.read_csv('energy.csv')
print(energy.columns)
df=DataFrame(energy.head(500))
print(df.head(500))

startup=pd.read_csv('energy_startup.csv')
print(startup.columns)
sdf=DataFrame(startup.head(700))
print(sdf.head(700))

December=df[df.Month=='Dec']
plt.scatter(df.Kwh, df.Active_kwh_month)
#interest=sales_rev and kwh


#taking info from both datasets into one df. #merge 

startup_df=sdf[['Year','Month','Sales_rev','Season','Month_Profit','Client_Region']].copy()
print(startup_df)
endf=df[['Year','Month','Active_kwh_month','Kwh', 'Room_household']].copy()
z_merge=pd.merge(startup_df,endf)
print(z_merge)


#x=sns.relplot('Sales_rev','Month_Profit',data=z_merge,hue='Season', size='Year')
#plt.show()

December=z_merge[z_merge.Month=='Dec']
Decemberd=df[df.Month=='Dec']
#p=sns.stripplot(z_merge.Sales_rev,z_merge.Season, size=3.5, alpha=0.4);
#plt.show()

#sp=sns.stripplot(z_merge.Sales_rev,z_merge.Client_Region, size=3.5, alpha=0.4);
#plt.show()

"""sp=sns.stripplot(z_merge.Room_household, z_merge.Sales_rev, jitter=True,  size=3.5, alpha=0.4)


sns.stripplot(x='Room_household', y='Sales_rev', jitter=0.30, size=10, alpha=0.7, split=True, palette='Blues', marker='.', linewidth=1, edgecolor='white', data=z_merge)
plt.show()"""

energy=pd.read_csv('energy.csv')
print(energy.columns)
df=DataFrame(energy.head(500))
print(df.head(500))

"""
sns.stripplot(x='Season', y='Active_kwh_month', jitter=0.30, size=10, alpha=0.7, hue='Room_household', palette='OrRd', marker='.', linewidth=1, edgecolor='white', data=z_merge)


sns.stripplot(x='Client_Region', y='Room_household', jitter=0.30, size=15, alpha=0.7, hue='Kwh', palette='husl', marker='*', linewidth=1, edgecolor='white', data=z_merge)



sns.stripplot(x='Client_Region', y='Kwh', jitter=0.30, size=15, alpha=0.7, hue='Year', palette='husl', marker='*', linewidth=1, edgecolor='white', data=z_merge)


sns.stripplot(x='Room_household', y='Sales_rev', jitter=0.30, size=15, alpha=0.7, hue='Year', palette='Blues', marker='*', linewidth=1, edgecolor='white', data=z_merge)


sns.stripplot(x='Client_Region', y='Sales_rev', jitter=0.30, size=15, alpha=0.7, hue='Kwh',  palette='husl', marker='*', linewidth=1, edgecolor='white', data=z_merge)"""


startup_df=sdf[['Year','Month','Sales_rev','Season','Month_Profit','Client_Region']].copy()
print(startup_df)
endf=df[['Year','Month','Active_kwh_month','Kwh', 'Room_household']].copy()
z_merge=pd.merge(startup_df,endf)
print(z_merge)

# Sales

#what were top sales revenue generating products? top room household and region
#geeration by revenue generation


startup=pd.read_csv('energy_startup.csv')
print(startup.columns)
sdf=DataFrame(startup.head(700))
print(sdf.head(700))

toprev=sdf.groupby(['Client_Room_household','Client_Region']).sum().round(2).sort_values(['Sales_rev'], ascending=False)
print(toprev.head(10))














