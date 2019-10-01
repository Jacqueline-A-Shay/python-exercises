import pandas as pd
import numpy as np


from pydataset import data
df = data('mpg') # load the dataset and store it in a variable
data('mpg', show_doc=True) # view the documentation for the dataset

# Use the mpg dataset to practice pandas

# How many rows and columns are there?
print(df.shape) # (234,11)

# What are the data types?
df.dtypes

manufacturer     object
model            object
displ           float64
year              int64
cyl               int64
trans            object
drv              object
cty               int64
hwy               int64
fl               object
class            object
dtype: object
df.head()

# Do any cars have better city mileage than highway mileage? NO
df["hwymi_better"] = df.apply(lambda x : x["hwy"] if x["cty"] < x["hwy"] else "", axis=1)
df
df.sort_values(by="hwymi_better", ascending=False)

df["ctymi_better"] = df.apply(lambda x : x["cty"] if x["cty"] > x["hwy"] else "", axis=1)
df
(df['ctymi_better'].values != '').sum()
print("How many cars have better city performance? {}".format(((df['ctymi_better'].values != '').sum())))
print("How many cars perform better on highway than city? {}".format((df['hwymi_better'][df['hwymi_better'] != ''].count())))

# series nonzero method will return an array containing the nonzero items
print("How many cars have better city performance? {}".format(np.count_nonzero(df["ctymi_better"])))# 0 
print("How many cars perform better on highway than city? {}".format(np.count_nonzero(df["hwymi_better"]))) # 234

better_mi = df['cty'] > df['hwy']
df[better_mi]

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
df["mileage_difference"] = df["hwy"] - df["cty"]
df.head()
np.count_nonzero(df["mileage_difference"]) # also 234, validated all hwy mileage better than cty
df.sort_values(by = 'mileage_difference', ascending=False).head(2)

# On average, which manufacturer has the best miles per gallon? # Honda

df.groupby('manufacturer', as_index = True).agg({"cty":"mean", "hwy":"mean"}).sort_values(by = 'hwy',ascending=False).head(1)

print(df[df['class']=='compact'].sort_values(by = 'hwy', ascending = True).head(1))

# How many different manufacturers are there? # 15
df['manufacturer'].unique() # list all the unique manufacturer
df['manufacturer'].nunique() # list the number of unique ones

# How many different models are there? # 38
df.groupby('manufacturer')['model'].nunique()
# Do automatic or manual cars have better miles per gallon? # not really

# pivot 
# first df.groupby(['col1', 'col2'...])
# .size() > return count of each subset
# .mean() or others (ex:.max(), .min()) follow by['the col you want to calc with']
# .sort_values(seems like sorting will auto based on the calc, ascending = True/False)

# group by manufacturer, trans > take the average of highway mpg
group_trans = df.groupby(["manufacturer", "trans"]).mean()['hwy'].sort_values(ascending=False) 
group_trans
group_trans.plot(kind='barh', stacked=True, figsize=[32,12], colormap='winter')

# group by manufacturer, trans > take the average of highway mpg
group_trans2 = df.groupby("trans").mean()['hwy'].sort_values(ascending=False)
group_trans2
group_trans2.plot(kind='barh', stacked=True, figsize=[16,6], colormap='winter')


fig, ax = plt.bar(x = 'trans', y = 'hwy',figsize=(15,7))
df.groupby(['manufacturer','trans']).mean()['hwy'].plot(ax=ax)

from pydataset import data

mam = data('Mammals')
mam.shape # (107, 4)
mam.dtypes

# weight      float64
# speed       float64
# hoppers        bool
# specials       bool
# dtype: object

mam.describe()

#             weight       speed
# count   107.000000  107.000000
# mean    278.688178   46.208411
# std     839.608269   26.716778
# min       0.016000    1.600000
# 25%       1.700000   22.500000
# 50%      34.000000   48.000000
# 75%     142.500000   65.000000
# max    6000.000000  110.000000

mam.info()

# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 107 entries, 1 to 107
# Data columns (total 4 columns):
# weight      107 non-null float64
# speed       107 non-null float64
# hoppers     107 non-null bool
# specials    107 non-null bool
# dtypes: bool(2), float64(2)
# memory usage: 2.7 KB

#the specie that runs the fastes has weight of 55
mam.sort_values(by='speed',ascending=False) 
mam[['weight','speed']].sort_values(by='speed',ascending=False).head(1)
# overal percentage of specials
mam['specials'].value_counts(normalize=True) * 100
(mam.specials==True).mean()*100
# How many animals are hoppers that are above the median speed? What percentage is this?
is_hopper = mam[mam['hoppers'] == True]
is_hopper
median = mam['speed'].median()
total = mam.count()
total
hs = is_hopper[is_hopper["speed"] > median]
hs
percentage = round((hs.shape[0]/mam.shape[0] *100),2)
print('percentage of hoppers running faster than median speed is: ', percentage)

num_animals = sum((mam.hoppers == True) & (mam.speed > mam.speed.median()))
print(round(num_animals/len(mam)*100,2))

# Getting data from SQL databases
create_engine function 
from sqlalchemy module 
to create an engine that pandas can use to execute a query and construct a dataframe.

Create engine object
- specify a connection url. 

a specially formatted url that describes how to connect to a database. 
general - 
protocol://[user[:password]@]hostname/[database_name] 

from sqlalchemy import create_engine

from env import user, password, host

url = 'mysql+pymysql://{}:{}@{}/fruits_db'.format(user, password, host)

dbc = create_engine(url)

df = pd.read_sql('SELECT * FROM fruits', dbc)


# Create a function named get_db_url. 
def get_db_url(username, hostname, password, database):
    url = 'mysql+pymysql://{}:{}@{}/fruits_db'.format(user, password, host)
    return url

""" 2)Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
2a)How many rows and columns are there?
2b)What are the data types of each column?
2c)Summarize the dataframe with .info and .describe
2d)Rename the cty column to city.
2e)Rename the hwy column to highway.
2f)Do any cars have better city mileage than highway mileage?
2g)Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
2h)Which car (or cars) has the highest mileage difference?
2i)Which compact class car has the lowest highway mileage? The best?
2j)Create a column named average_mileage that is the mean of the city and highway mileage.
2k)Which dodge car has the best average mileage? The worst? """

from pydataset import data
mpg = data('mpg')
#2a)
mpg.shape
#2b,c)
mpg.info()
mpg.describe()
#2d,e)
mpg.rename(columns = {'cty':'city','hwy':'highway'},inplace = True)
#2f)
better_mileage = mpg['city']>mpg['highway']
mpg[better_mileage]
#2g)
mpg['mileage_difference'] = mpg.highway-mpg.city
#2h)
mpg.sort_values(by = 'mileage_difference',ascending=False).head(1)
#2i)
print(mpg[mpg['class'] == 'compact'].sort_values(by='highway',ascending=True).head(1))
print(mpg[mpg['class'] == 'compact'].sort_values(by='highway',ascending=True).tail(1))
#2i)
mpg['average_mileage']=mpg[['highway','city']].apply(np.mean,axis=1)
#2k)
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage',ascending=False).head(1)
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage',ascending=False).tail(1)



""" 3)Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
3a)How many rows and columns are there?
3b)What are the data types?
3c)Summarize the dataframe with .info and .describe
3d)What is the the weight of the fastest animal?
3e)What is the overall percentage of specials? 
3f)How many animals are hoppers that are above the median speed? What percentage is this? """

mammals=data('Mammals')
mammals.head()
#3a)
mammals.shape
#3b)
mammals.dtypes
#3c)
mammals.info()
mammals.describe()
#3d)
mammals[['weight','speed']].sort_values(by='speed',ascending=False).head(1)
#3e)
sum(mammals.specials==True)/len(mammals)*100
#3f
num_animals=sum((mammals.hoppers == True) & (mammals.speed > mammals.speed.median()))
print(num_animals)
print(round(num_animals/len(mammals)*100,2))

""" 2)Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
2a)How many rows and columns are there?
2b)What are the data types of each column?
2c)Summarize the dataframe with .info and .describe
2d)Rename the cty column to city.
2e)Rename the hwy column to highway.
2f)Do any cars have better city mileage than highway mileage?
2g)Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
2h)Which car (or cars) has the highest mileage difference?
2i)Which compact class car has the lowest highway mileage? The best?
2j)Create a column named average_mileage that is the mean of the city and highway mileage.
2k)Which dodge car has the best average mileage? The worst? """

from pydataset import data
mpg = data('mpg')
#2a)
mpg.shape
#2b,c)
mpg.info()
mpg.describe()
#2d,e)
mpg.rename(columns = {'cty':'city','hwy':'highway'},inplace = True)
#2f)
better_mileage = mpg['city']>mpg['highway']
mpg[better_mileage]
#2g)
mpg['mileage_difference'] = mpg.highway-mpg.city
#2h)
mpg.sort_values(by = 'mileage_difference',ascending=False).head(1)
#2i)
print(mpg[mpg['class'] == 'compact'].sort_values(by='highway',ascending=True).head(1))
print(mpg[mpg['class'] == 'compact'].sort_values(by='highway',ascending=True).tail(1))
#2i)
mpg['average_mileage']=mpg[['highway','city']].apply(np.mean,axis=1)
#2k)
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage',ascending=False).head(1)
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage',ascending=False).tail(1)



""" 3)Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
3a)How many rows and columns are there?
3b)What are the data types?
3c)Summarize the dataframe with .info and .describe
3d)What is the the weight of the fastest animal?
3e)What is the overall percentage of specials? 
3f)How many animals are hoppers that are above the median speed? What percentage is this? """

mammals=data('Mammals')
mammals.head()
#3a)
mammals.shape
#3b)
mammals.dtypes
#3c)
mammals.info()
mammals.describe()
#3d)
mammals[['weight','speed']].sort_values(by='speed',ascending=False).head(1)
#3e)
sum(mammals.specials==True)/len(mammals)*100
#3f
num_animals=sum((mammals.hoppers == True) & (mammals.speed > mammals.speed.median()))
print(num_animals)
print(round(num_animals/len(mammals)*100,2))