#!/usr/bin/env python
# coding: utf-8

# In[2]:


#data processing
import pandas as pd
#linear algebra
import numpy as np
#data visualisation
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly.express as px
###import dash
####import dash_core_components as dcc
###import dash_html_components as html
###import squarify
from matplotlib import pyplot as plot


# In[3]:


data =pd.read_csv('globalterrorismdb_0522dist(1).csv', encoding='latin-1')
df = pd.DataFrame(data)
print("Data has imported")
data.head() 


# In[4]:


df.info()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


for i in df.columns:
    print(i,end=", ")


# In[8]:


df=df[["iyear", "imonth","iday", "country_txt","region_txt","provstate","city","latitude","longitude","location","summary","attacktype1_txt","targtype1_txt", "gname", "motive", "weaptype1_txt", "nkill","nwound","addnotes"]]
df.head()


# Cleaning the data

# In[9]:


df=df[["iyear","imonth","iday","country_txt","region_txt","provstate","city",
       "latitude","longitude","location","summary","attacktype1_txt","targtype1_txt",
       "gname","weaptype1_txt","nkill","nwound","addnotes"]]
df.head()


# In[10]:


data.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','provstate':'state','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)


# In[11]:


data=data[['Year','Month','Day','Country','state','Region','city','latitude','longitude','AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]


# In[12]:


data.head()


# In[13]:


data.info()


# In[14]:


data.shape


# In[ ]:





# In[15]:


data.isnull().sum()


# In[16]:


data["Killed"]=data["Killed"].fillna(0)
data["Wounded"]=data["Wounded"].fillna(0)
data["Casualty"]=data["Killed"]+data["Wounded"]


# In[17]:


data.describe()


# In[18]:


data.isnull().sum()


# In[19]:


data.info()


# In[ ]:





# In[20]:


data.hist(figsize=(20,10))  # This represents  the distribution of data  on each series in the DataFrame.


# In[21]:


data.info


# In[22]:


data.describe()


# # Observation
# 

# The data cosisit of terorist activities ranginig from the year : 1970 to 2020
# 

# Maximum number of people killed in an event were :1700
# 

# Maximum number of people wounded in a event were :10878
# 

# Max number of total casualties in a event were:12263

# # Correlation Analysis

# In[23]:


plt.figure(figsize=(15,10))
#This shows how much related is one parameter to the other in the dataset. 
sns.heatmap(np.round(data.corr(),2),annot=True, cmap='BuPu')


# In[24]:


pd.crosstab(data.Year, data.Region).plot(kind='area',figsize=(15,6))
plt.title('Terrorist Activities by Region in each Year')
plt.ylabel('Number of Attacks')
plt.show()


# # Visulaise Data

# Year wise Attack
# 

# **Number of Terrorist Activities each Year**

# In[25]:


Year=data.Year.value_counts().to_dict()
rate=((Year[2020]-Year[1970])/Year[2020])*100
print(Year[1970],'attacks happened in 1970 &',Year[2020],'attacks happened in 2020')
print('So the number of attacks from 1970 has increased by',np.round(rate,0),'% till 2020')


# **Number of attack were there in 1970 & 2020 and Also find percentage the attacks have increased.**

# In[ ]:





# # Total casualties by wounded + killed each year

# In[26]:


yc=data [["Year", "Casualty"]].groupby("Year").sum()
yw=data[["Year","Wounded"]].groupby("Year").sum()
yk=data [["Year", "Killed"]].groupby("Year").sum()
yw.head(),yc.head(),yk.head()


# In[ ]:





# In[27]:


ct=data["Country"].value_counts().head(10)
ct


# In[28]:


ct=data[["Country", "Casualty"]].groupby("Country").sum().sort_values(by="Casualty", ascending=False)
ct = ct[:10]
ct.head(10)


# In[29]:


cnk=data[["Country", "Killed"]].groupby("Country").sum().sort_values(by="Killed", ascending=False)
cnk.head(10)


# In[30]:


cnw=data[["Country", "Wounded"]].groupby("Country").sum().sort_values(by="Wounded", ascending=False)
cnw.head(10)


# In[31]:


yk=data[["Year","Killed"]].groupby("Year").sum()
yk.head()


# In[32]:


attacks=data["Year"].value_counts(dropna=False).sort_index().to_frame().reset_index().rename(columns={"index":"Year","Year":"Attacks"}).set_index("Year")
attacks.head()


# In[ ]:





# In[33]:


yc.plot(kind="bar",color="red",figsize=(17,8))
plt.title("Casualties wise Year",fontsize=18)
plt.xlabel("Year", fontsize=18)
plt.ylabel("Casualties numbers",fontsize=18)
plt.show()


# In[34]:


fig=plt.figure()
ax0=fig.add_subplot(2,1,1)
ax1=fig.add_subplot(2,1,2)

#Killed
yk.plot(kind="bar", color="brown", figsize=(15,15),ax=ax0)
ax0.set_title("Killed each year")
ax0.set_xlabel("Year")
ax0.set_ylabel("Number killed")

#Wonded
yw.plot(kind="bar", color="blue", figsize=(15,15),ax=ax1)
ax1.set_title("Wounded each year")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number wonded")
plt.show()


# In[35]:


ct.plot(kind="bar", color="brown", figsize=(15,15))
plt.title("Attack by Country")
plt.xlabel("Countrys name", fontsize =15)
plt.xticks(fontsize=20)
plt.ylabel("Number Attacks", fontsize=15)
plt.show()


# In[36]:


ct[:10].plot(kind="bar", color="blue",figsize=(15,7))
plt.title("Countries by Casualties", fontsize=13)
plt.xlabel("Countries", fontsize =15)
plt.xticks(fontsize=12)
plt.ylabel("Number of Casualties", fontsize=15)
plt.show()


# In[39]:


fig=plt.figure()
ax0=fig.add_subplot(1,2,1)
ax1=fig.add_subplot(1,2,2)

#Killed
cnk[:10].plot(kind="bar", color="brown", figsize=(15,9),ax=ax0)
ax0.set_title("Killed each Country")
ax0.set_xlabel("Countriesr")
ax0.set_ylabel("Number killed")

#Wonded
cnw[:10].plot(kind="bar", color="blue", figsize=(15,9),ax=ax1)
ax1.set_title("Wounded each Country")
ax1.set_xlabel("Countries")
ax1.set_ylabel("Number wonded")

plt.show()


# In[37]:


px.scatter(data,data.Wounded,data.Killed,hover_name='Country',animation_frame='Year',animation_group='Country',color='AttackType',
           range_color=[0,1],labels={'Killed':'Deaths','Wounded':'Casualities'},
           title='Number of casualities vs Killed people in each country for each year')


# In[38]:


terr=data.groupby(['Country'],as_index=False).count()


# In[39]:


fig=px.choropleth(terr,locations='Country',locationmode='country names',
                  color='Year',hover_name='Country',projection='orthographic',
                  title='Total number of attacks (1970-2020)',labels={'Year':'Attacks'})
fig.show()


# # Sum up the total kills each year and create the count plot

# In[41]:


plt.subplots(figsize=(15,10))
kills = data.groupby('Year')['Killed'].sum().to_frame().reset_index()
kills.columns = ['Year','Killed']
sns.barplot(x=kills['Year'], y=kills['Killed'], palette='bright')
plt.title('Number Of Kills Each Year')
plt.show()


# In[42]:


import squarify
fig, ax = plt.subplots(1, figsize = (20,22))
squarify.plot(sizes=kills['Killed'], 
              label=kills['Year'], 
              alpha=.8 )
plt.axis('off')
plt.title('Number of Kills')
plt.show()


#  **The number of casualities corresponding to the killed people in each country for each year.**

# In[43]:


plt.subplots(figsize=(15,6))
sns.countplot('Year',data=data,palette='RdYlGn_r',edgecolor=sns.color_palette("YlOrBr", 10))
plt.xticks(rotation=90)
plt.title('Number Of Terrorist Activities Each Year')
plt.show()


# In[44]:


Year=data.Year.value_counts().to_dict()
rate=((Year[2020]-Year[1970])/Year[2020])*100
print(Year[1970],'attacks happened in 1970 &',Year[2020],'attacks happened in 2020')
print("Attacks from 1970 has increased each year by",np.round(rate,0),'% till 2020')


# In[45]:


plt.figure(figsize=(13,6))
sns.countplot(data['AttackType'],order=data['AttackType'].value_counts().index,
              palette='hot')
plt.xticks(rotation=90)
plt.xlabel('Method')
plt.title('Method of Attack')
plt.show()


# In[46]:


plt.figure(figsize=(13,6))
sns.countplot(data['Target_type'],order=data['Target_type'].value_counts().index,
              palette='magma')
plt.xticks(rotation=90)
plt.xlabel('Type')
plt.title('Type of Target')
plt.show()


# In[47]:


fig,axes = plt.subplots(figsize=(16,11),nrows=1,ncols=2)
sns.barplot(x = data['Country'].value_counts()[:20].values, y = data['Country'].value_counts()[:20].index, 
            ax=axes[0],palette = 'magma');
axes[0].set_title('Terrorist Attacks per Country')
sns.barplot(x=data['Region'].value_counts().values,y=data['Region'].value_counts().index,
            ax=axes[1])
axes[1].set_title('Terrorist Attacks per Region')
fig.tight_layout()
plt.show()


# In[156]:


max_count=terr['Year'].max()
max_id=terr['Year'].idxmax()
max_name=terr['Country'][max_id]
min_count=terr['Year'].min()
min_id=terr['Year'].idxmin()
min_name=terr['Country'][min_id]


# In[49]:


print(max_name,'has suffered the maximum number of terror attacks of',max_count)
print(min_name,'has suffered the minimum number of terror attacks of',min_count)


# In[50]:


plt.subplots(figsize=(11,10))
sns.barplot(y=data['Group'].value_counts()[1:12].index,x=data['Group'].value_counts()[1:12].values,
           palette='copper')
plt.title('Most Active Terrorist Organizations')
plt.show()


# In[51]:


data_after = data[data['Year']>=2000]
fig,ax = plt.subplots(figsize=(15,10),nrows=2,ncols=1)
ax[0] = pd.crosstab(data.Year,data.Region).plot(ax=ax[0])
ax[0].set_title('Change in Regions per Year')
ax[0].legend(loc='center left',bbox_to_anchor = (1,0.5))
ax[0].vlines(x=2000,ymin=0,ymax=7000,colors='red',linestyles='--')
pd.crosstab(data_after.Year,data_after.Region).plot.bar(stacked=True,ax=ax[1])
ax[1].set_title('After Declaration of War on Terror (2000-2020)')
ax[1].legend(loc='center left',bbox_to_anchor = (1,0.5))
plt.show()


# In[52]:


mean_missing_percent=data.isnull().mean() *100
total_missing = data.isnull().sum().sort_values(ascending = False)

missing_data = pd.concat([total_missing, mean_missing_percent], axis=1, keys=["Total","%"])
missing_data


# In[53]:


missing_data.plot(figsize=(20,10))


# In[54]:


sns.barplot(data['Group'].value_counts()[1:15].values,data['Group'].value_counts()[1:15].index,palette=('viridis'))
plt.xticks(rotation=90)
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.title('Terrorist Groups with Highest Terror Attacks')
plt.show()


# In[55]:


plt.figure(figsize=(9,9))
data['Country'].value_counts()[:11].plot(kind='pie',autopct='%1.1f%%',shadow=True)
plt.title('Number of attacks based on countries')
plt.show()


# In[56]:


df.country_txt


# In[ ]:





# In[ ]:




