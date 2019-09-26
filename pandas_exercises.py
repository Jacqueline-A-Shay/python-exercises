utilize API or open source data to compplement the currently available dataset
ex: get google map or weather etc to assist labeling feature engineering etc

from pydataset import data
mpg = data('mpg')
mpg.head()

# On average, which manufacturer has the best miles per gallon?
extract = mpg.groupby(mpg.manufacturer)[['hwy']].mean().sort_values(by='hwy', ascending = False)
extract.idxmax()
extract == extract.idxmax()

count_val.max() # 13 (y)
count_val[count_val == count_val.max()] #mask

print("The manufacturer producing the best mpg car is: {}".format(extract.idxmax()))

# How many different manufacturers are there?
print("There are {} manufacturers in the dataset".format(mpg.manufacturer.nunique()))

