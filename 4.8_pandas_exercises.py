import pandas as pd
import numpy as np


from pydataset import data
df = data('mpg') # load the dataset and store it in a variable
data('mpg', show_doc=True) # view the documentation for the dataset

# Use pandas to convert the following list to a numeric series:
['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
series = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
print(type(series))


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
df["ctymi_better"] = np.where( df["cty"] > df["hwy"] )
print(df_ctymi_better)
df["hwymi_better"] = df.apply(lambda x : x["hwy"] if x["cty"] < x["hwy"] else "", axis=1)
df
df.sort_values(by="hwymi_better", ascending=False)

# series nonzero method will return an array containing the nonzero items
np.count_nonzero(df["ctymi_better"]) # 0 
np.count_nonzero(df["hwymi_better"]) # 234
df["hwymi_better"].nonzero()

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
df["mileage_difference"] = df["hwy"] - df["cty"]
df.head()
np.count_nonzero(df["mileage_difference"]) # also 234, validated all hwy mileage better than cty

# On average, which manufacturer has the best miles per gallon? # Honda

df.groupby('manufacturer', as_index = True).agg({"cty":"mean", "hwy":"mean"}).sort_values(by = 'hwy',ascending=False)


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