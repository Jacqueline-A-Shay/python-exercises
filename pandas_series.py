import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
type(fruits)

fruits.describe()

count       17
unique      13
top       kiwi
freq         4
dtype: object

# only the unique fruit names
fruits.unique()
fruits.nunique() # total 13 different unique fruits

# how many are each fruit?
index = pd.Index(fruits)
index.value_counts()

kiwi                4
mango               2
gala apple          1
blueberry           1
tomato              1
watermelon          1
blackberry          1
strawberry          1
honeycrisp apple    1
honeydew            1
gooseberry          1
papaya              1
pineapple           1
dtype: int64

# most freq occuring fruit
kiwi

# least freq occuring fruit
anything other than kiwi or mango

# get the longest string from the fruits series
fruits.map(len).max() # 16

# Find the fruit(s) with 5 or more letters in the name.
fruits.apply(lambda x: len(x) >= 5).sum()

# Capitalize all the fruit strings in the series.
fruits.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization) # 10
fruits.str.contains('a').sum()

# Output the number of vowels in each and every fruit.
import re
fruits.str.extractall('(?i)(?P<vowels>[aeiou])').groupby(level=0).count()

# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
fruits.apply(lambda x:'o'in x)