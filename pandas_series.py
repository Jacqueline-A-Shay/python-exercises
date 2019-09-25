https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mask.html
study index/ subsetting 


import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
type(fruits)

fruits.describe() # overview of total dataset

count       17
unique      13
top       kiwi
freq         4
dtype: object

# only the unique fruit names
fruits.unique()
fruits.nunique() # total 13 different unique fruits

# determine how many times each value occurs in the series
freq = fruits.value_counts()
freq

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

# most freq occuring fruit # kiwi
fruits.mode()

most_freq = freq.max()
most_freq

freq = fruits.value_counts()
freq
freq.idxmax() 

# least freq occuring fruit # anything other than kiwi or mango
lowest_freq = fruits.value_counts().min()
lowest_freq # this will only list the lowest number, not even the name of the fruit

frequencies = fruits.value_counts()
frequencies[frequencies == lowest_freq] # this will provide all the ones having least count

# get the longest string from the fruits series
fruits[fruits.map(len).idxmax()] # 16

fruit_names = fruits.unique()
fruit_names = pd.Series(fruit_names)
fruit_names #list of names

len_of_longest = fruit_names.str.len().max()
len_of_longest #length of longest name

id_of_longest = fruit_names.str.len().idxmax()
id_of_longest 
longest_string = fruit_names[id_of_longest]
longest_string


# Find the fruit(s) with 5 or more letters in the name.
more_than_five = fruits.apply(lambda x: len(x) >= 5)
fruits[more_than_five]

# Capitalize all the fruit strings in the series.
fruits.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization) # 10
counts_of_a = fruit_names.str.count("a")
list(zip(fruit_names, counts_of_a))



# Output the number of vowels in each and every fruit.
import re
df = fruits.str.extractall('(?i)(?P<vowels_count>[aeiou])').groupby(level=0).count()
df['fruit'] = fruits
df.drop_duplicates()
# df.drop(['fruit_names'], axis = 1)

def count_vowels(fruits):
    count = 0
    vowels = 'aeiou'
    for i in fruits:
        if vowels in i:
            count += 1
        return count

list(zip(fruits.uniqe()),pd.Series(fruits.unique()).apply(count_vowels)))

# this works
print(fruits[fruits.apply(lambda x: sum([1 for xc in x if xc.lower() in 'aeiou'])).idxmax()])

# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
fruits[fruits.apply(lambda x: x.count('o') >= 2)]

# Write the code to get only the fruits containing "berry" in the name
fruits[fruits.apply(lambda x: 'berry' in x)]
fruits[fruits.str.contains("berry")]
# Write the code to get only the fruits containing "apple" in the name
fruits[fruits.apply(lambda x: 'apple' in x)]
# Which fruit has the highest amount of vowels?
fruits[fruits.apply(count_vowels).idxmax()]

mon = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
mon = mon.str.strip('$')
mon = mon.str.replace(',','') # strip(",") doesn't work...
mon
mon_f = pd.to_numeric(mon,errors='coerce')
mon_f
mon_f.max() # 4789988.17
mon_f.min() # 278.6
pd.cut(mon_f,4) # Bin the data into 4 equally sized intervals and show how many values fall into each bin.

0        (-4511.11, 1197705.993]
1        (-4511.11, 1197705.993]
2        (-4511.11, 1197705.993]
3      (3592560.778, 4789988.17]
4     (1197705.993, 2395133.385]
5     (1197705.993, 2395133.385]
6        (-4511.11, 1197705.993]
7     (1197705.993, 2395133.385]
8      (3592560.778, 4789988.17]
9     (2395133.385, 3592560.778]
10       (-4511.11, 1197705.993]
11     (3592560.778, 4789988.17]
12     (3592560.778, 4789988.17]
13    (2395133.385, 3592560.778]
14    (1197705.993, 2395133.385]
15     (3592560.778, 4789988.17]
16     (3592560.778, 4789988.17]
17    (2395133.385, 3592560.778]
18       (-4511.11, 1197705.993]
19       (-4511.11, 1197705.993]
dtype: category
Categories (4, interval[float64]): [(-4511.11, 1197705.993] < (1197705.993, 2395133.385] <
                                    (2395133.385, 3592560.778] < (3592560.778, 4789988.17]]



pd.cut(mon_f,4).value_counts() 
(-4511.11, 1197705.993]       7
(3592560.778, 4789988.17]     6
(1197705.993, 2395133.385]    4
(2395133.385, 3592560.778]    3
dtype: int64
import matplotlib.pyplot as plt

pd.cut(mon_f,4).value_counts().plot(kind = 'barh', figsize = (5,5), title = 'Series Histogram Plot')


exam = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
exam
# Find min, max, mean, median of exam score
exam.min() # 60
exam.max() # 96
exam.mean() # 78.15
exam.median()  # 79

# histogram
import numpy as np
exam, exam_bin = np.histogram(exam)
plt.hist(bins[:-1], bins, weights=counts)

exam.hist(gird = False)

# convert to letter grade
import matplotlib.pyplot as plt
letter = pd.cut(exam, bins = [0, 60, 70, 80, 90,100], labels=["F", "D", "C","B","A"])
letter
bin = pd.cut(exam, [0, 60, 70, 80, 90,100])
bin

h = exam.value_counts(sort = False, bins= [0, 60, 70, 80, 90,100])
h

label = ["F", "D", "C","B","A"]
h.plot(kind = 'barh', figsize = (5,5), yticks = ('F','D','C','B','A'))


# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, 
# and that many points should be given to every other score as well.        
dif = 100 - exam.max()
dif
exam
curve = exam + 4
curve

# string handle


hand ='hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
hand
nhand = [h for h in hand]
nhand = pd.Series(nhand)
nhand

count_val = nhand.value_counts()
count_val

count_val.max() # 13 (y)
count_val[count_val == count_val.max()] #mask

count_val.min() # 4 (l)

# How many vowels are in the list? #34
cv = nhand.str.lower().str.count(r'[aeiou]').sum()
cv
# How many consonants are in the list? #166
cc = nhand.count()
cc
non_vo =  cc - cv
non_vo

# Create a series that has all of the same letters, but uppercased
dif_letter = nhand.unique()
dif_letter

nhand[nhand.duplicated()].str.upper()
same_letter = nhand[nhand.duplicated()]
same_letter
same_letter = same_letter.value_counts()
top = same_letter.nlargest(6)
top

top.plot(kind = 'bar', figsize = (5,5), title = 'Top 6 Repeated Letters')
