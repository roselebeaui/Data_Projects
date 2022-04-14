#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import seaborn as sns


# In[214]:


data_1 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_January_2019.csv')
data_2 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_February_2019.csv')
data_3 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_March_2019.csv')
data_4 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_April_2019.csv')
data_5 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_May_2019.csv')
data_6 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_June_2019.csv')
data_7 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_July_2019.csv')
data_8 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_August_2019.csv')
data_9 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_September_2019.csv')
data_10 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_October_2019.csv')
data_11 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_November_2019.csv')
data_12 = pd.read_csv(r'C:\Users\alexa\Desktop\Alexa\Sales_Product\Sales_December_2019.csv')

data = pd.concat([data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10,data_12,data_12],axis=0)
data.head(5)


# In[215]:


data.info


# In[216]:


#Checking for NULL values

sns.heatmap(data=pd.isnull(data))


# In[185]:


#Drop NULL Values

data = data.dropna()


# In[186]:


#Check data structure

data.info()


# In[187]:


data['Quantity Ordered'].unique()


# In[188]:


filter_repeated_values = data['Quantity Ordered'] != 'Quantity Ordered'

data = data[filter_repeated_values]


# In[189]:


data['Quantity Ordered'].unique()
data.size


# In[190]:


#Creating Month/Year/Time Column

data['month'] = data['Order Date'].str[0:2]
data['year'] = data['Order Date'].str[6:8]
data['time'] = data['Order Date'].str[-5:-3]
data


# In[191]:


#Change Column Types - numerical

data['Quantity Ordered'] = pd.to_numeric(data['Quantity Ordered'])
data['Price Each'] = pd.to_numeric(data['Price Each'])


# In[192]:


#Check Data Types

data.info()


# In[193]:


data


# In[194]:


#Extract city from Address

city = data['Purchase Address'].str.split(", ",expand=True)[1]
city


# In[195]:


#Join city column to data

data = pd.concat([data,city],axis=1)
data


# In[196]:


#Rename Column

data = data.rename({1:'City'},axis=1)


# In[197]:


data['Sales'] = data['Quantity Ordered']*data['Price Each']


# In[198]:


data


# In[199]:


#Calculation for Total Sales

data_q1 = data[['year','Sales']]


# In[200]:


data_q1.groupby(['year']).sum()


# In[201]:


#Calculation for Sales by Month

data_q2 = data[['month','Sales']]
data_q2.groupby(['month']).sum().sort_values(by=['Sales'],ascending=False)['Sales']


# In[202]:


#SNS Bar Plot

plot_q2 = data_q2.groupby(['month']).sum().sort_values(by=['Sales'],ascending=False)['Sales']

sns.barplot(x=plot_q2.index ,y= plot_q2)


# In[203]:


#Total Sales by City

data_q3 = data[['City','Sales']]
data_q3.groupby(['City']).sum().sort_values(['Sales'],ascending=False)['Sales']


# In[204]:


#SNS Bar Plot

plot_q3 = data_q3.groupby(['City']).sum().sort_values(['Sales'],ascending=False)['Sales']

plt_1 = sns.barplot(x=plot_q3.index, y=plot_q3)

for item in plt_1.get_xticklabels():
    item.set_rotation(90)


# In[205]:


#Calculation Total Sales by Time of Day

data_q4 = data[['time','Sales']]
data_q4.groupby(['time']).sum().sort_values(['time'],ascending=True)['Sales']


# In[206]:


#Use SNS Line Plot to Estimate Potential Ad Periods

plot_q4 = data_q4.groupby(['time']).sum().sort_values(['time'],ascending=True)['Sales']

sns.lineplot(x=plot_q4.index , y=plot_q4)


# In[207]:


#Analysis of Products Most Likely to be Sold Together

data_q5 = data[['Order ID','Product']]
data_q5 = data_q5[data_q5['Order ID'].duplicated(keep=False)].sort_values(['Product'])
data_q5


# In[208]:


data_q5.groupby('Order ID').sum()['Product']


# In[209]:


data_q5_groups = pd.DataFrame(data_q5.groupby('Order ID').sum()['Product'])
data_q5_groups['number'] = data_q5_groups.index
data_q5_groups.groupby(['Product']).count().sort_values(['number'],ascending=False).head(20)


# In[210]:


#Calculation of Product Units Sold by Rank

data_q6 = data[['Product','Quantity Ordered']]
data_q6.groupby(['Product']).sum().sort_values(['Quantity Ordered'],ascending=False)['Quantity Ordered']


# In[211]:


#NS Products Bar Plot

plot_q6 = data_q6.groupby(['Product']).sum().sort_values(['Quantity Ordered'],ascending=False)['Quantity Ordered']

plt = sns.barplot(x=plot_q6.index, y=plot_q6)

for item in plt.get_xticklabels():
    item.set_rotation(90)


# In[ ]:




