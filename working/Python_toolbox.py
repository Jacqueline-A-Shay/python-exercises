REPL, a read-eval-print-loop

-i flag to python (or ipython). python -i myscript.py



################# string #################
'abc' != 'def'
True
'abc' + 'def'

'abcdef'
'abc' * 3

'abcabcabc'

% formatting: a little older, but still fairly common
.format: a newer way to format strings
f-strings: introduced in python 3.6; comparable to string interpolation in other languages


name = 'world'
print('hello, %s!' %name)
print('hello, {}!'.format(name))
print(f'Hello, {name}!')


.lower and .upper: convert the string to all lower or upper case
.strip: remove any leading and trailing whitespace from the string
.isdigit: test whether or not the string is a number
.split: convert a string to a list
.join: convert a list to a string



All of the string methods here do not modify the original string, 
they return a new string with the modification.
Unless it was store/assigned into a variable then you can retrieve



################# list #################
[n * 2 for n in range(10) if n % 2 == 0]

numbers = [1, 2, 3]
numbers.append(4)	>>	[1, 2, 3, 4]
numbers.pop()	>>	[1, 2, 3] # pop out the last one
numbers.remove(4) >> [1,2,3] # remove the specific value
len(numbers)

numbers[0] # the first element in the list

## Slice
numbers[:2] # everything up to, but not including, the element at index 2
[1, 2]

numbers[1:2] # everything from index 1 up to, but not including, index 2
[2]

numbers[1:] # everything from index 1 to the end of the list
[2, 3]

return an iterable
range >> iterable range object, not a list
list(range(10)) >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list('abcdef') >> ['a', 'b', 'c', 'd', 'e']
list(map(str, [1, 2, 3]))
  
# Return double of n 
def addition(n): 
    return n + n 
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 

# Double all numbers using map and lambda 
numbers = [1,2,3,4]
result = map((lambda n: n + n for n in numbers), numbers) 
print(list(result))
""" 
TypeError                                 Traceback (most recent call last)
<ipython-input-28-c0896bf7a938> in <module>
      1 numbers = [1,2,3,4]
      2 result = map((lambda n: n + n for n in numbers), numbers)
----> 3 print(list(result))

TypeError: 'generator' object is not callable
"""
 
numbers = [1,2,3,4]
result = map(lambda x: x + x, numbers) 
print(result)
"""
In [30]: numbers = [1,2,3,4] 
    ...: result = map(lambda x: x + x, numbers)  
    ...: print(result)                                                                                                                      
<map object at 0x102dc7ef0>

"""

numbers = [1,2,3,4]
result = map(lambda x: x + x, numbers) 
print(list(result)) # [2, 4, 6, 8]

## list comprehension
transform one iteable item(ex: list) into another(ex:list)
elements can be conditionally included or transformed in new list

new_things = []
for item in old_things:
	if condtion_based_on(item):
		newthings.append("something with " + item)
new_things = ["something with" + item for item in old_things if item in condition_based_on(item)]

numbers = [1,2,3,4]
doubled_odds = [n*2 for n in numbers if n%2 == 1]
doubled_odds


numbers = [1,2,3,4]
doubled_odds = []
for n in numbers:
	if n % 2 != 0:
		doubled_odds.append(n * 2) 
doubled_odds

numbers = [1,2,3,4]
double_num = []
for n in numbers:
	double_num.append(n*2)
doubled_num

numbers = [1,2,3,4]
doubled_num = [n*2 for n in numbers]
doubled_num

##################### Tuple #######################

DON'T QUITE GET immutable, once established, can't cahnge them?
x = ('abc')                                                                                                                        

In [35]: x.upper()                                                                                                                          
Out[35]: 'ABC'

In [36]: x                                                                                                                                  
Out[36]: 'abc'

index = check
commonly used to store different data types
list are used for all same data type
EX: tuple_example = (1, 'one',[1])

##################### Dictionary #######################
{"key":"value"} 
created by writing a dictionary literal, which is delimeted with curly braces
keys are separated from the values with a colon, and key-value pairs are separated by commas.

created with the built-in dict function:
x = {}
x = dict(name='Codeup', age=4)
x
{'name': 'Codeup', 'age': 4}

# access dic just like list
school['name']
'Codeup'

In [46]: school = {"name":"Codeup","age":4}                                                                                                 
In [47]: school["age"] += 1                                                                                                                 
In [48]: school                                                                                                                             
Out[48]: {'name': 'Codeup', 'age': 5}

me = {'name': 'JQ'}
me['name'] = 'JQ'
me['name'] = me['name'].lower() >>  {'name': 'jq'}
me['capitalized_name'] = me['name'].capitalize() >> {'name': 'jq', 'capitalized_name': 'Jq'}

Code that makes a new dictionary by swapping the keys and values of the original one:
new_dic = {v: k for k, v in school.item()}

new_dic = {}
for k, v in school.items():
	new_dic[v] = k
new_dic

Code that creates a set of all the first letters in a sequence of words:

first_letters = set()
for w in words:
    first_letters.add(w[0])

first_letters = {w[0] for w in words}

flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)
flattened = [n for row in matrix for n in row]

doubled_numbers = []
for n in numbers:
    doubled_numbers.append(n * 2)
doubled_numbers = [n * 2 for n in numbers]




##################### control structure #######################

conditionals: allow us to execute code conditionally
loops: allow us to execute code repeatedly

if
keyword if
a condition that evaluates to a boolean value followed by a colon (:)
the body of the statement indented by 4 spaces




while loop will execute it's body until the condition evaluates to false

i = 5
while i <= 10: # false when i > 10, break
    print(i)
    i += 1

 If the condition in the while loop never evaluates to False, you will end up with 
 what is called an infinite loop


 2 special keywords in Python that can change how the control flows through a loop:

continue will skip to the next iteration of a loop
break will stop executing the loop entirely



def factorial(number):
	if number == 1:
		return number
	else:
		return number*factorial(number-1)




dataset = [{'name': 'age', 'type': 'int', 'data': [20, 25, 43, 11, 15, 53, 36]},
           {'name': 'is_vegetarian', 'type': 'boolean', 'data': [False, True, False, False, True, False, False]},
           {'name': 'shoe size', 'type': 'int', 'data': [8, 11, 7, 10, 7, 9, 10]},
           {'name': 'ISP', 'type': 'categorical', 'data': ['AT&T', 'Spectrum', 'Spectrum', 'Spectrum', 'AT&T', 'Spectrum', 'AT&T']},
           {'name': 'BMI', 'type': 'float', 'data': [29.9, 20.4, 23.3, 21.7, 22.2, 22.8, 27.0]}]

# print the means for the numeric data
for feature in dataset:
    if feature['type'] == 'categorical' or feature['type'] == 'boolean':
        print('{} is not numeric, skipping'.format(feature['name']))
        continue
    avg = sum(feature['data']) / len(feature['data'])
    print('{} average: {:.2f}'.format(feature['name'], avg))


 ########################
 import std lib (json, collection, itertools, math)
 anaconda (include some popular 3rd party pkgs)
 install 3rd party (matplotlib, beautifulsoup, numpy, pandas)


 'bayes' # string literal
 1+1 #1 iter
 operator + can mean plus or concat
 '1'+'1' > '11'
 'a' * 3 > 'aaa' 
 ### don't assume numbers are numbers, always check type or assing int or float if absolutely need a number
 max(['1','2','3','10']) > 3 #when it's string, it will be sorted alphabetically instead of number


 pwd #right dir
 python -m doctest file_name.py # nothing if all correct!


##################################### NUMPY ###########################################
b.sum() # calling sum from the object (method)
np.sum(b) # calling sum from the class (function)





large and multi-dimensional arrays
create a numpy array by passing a list to the np.array
Referencing elements in numpy arrays at it's most basic is the same as referencing elements in Python lists.

vectorization
normal py - need looping over the list
type > ndarray # n-dimensional

a = np.array([1, 2, 3])
>>> a 
>>> array([1, 2, 3])
a[0]
1
print('a    == {}'.format(a))
print('a[0] == {}'.format(a[0]))
print('a[1] == {}'.format(a[1]))
print('a[2] == {}'.format(a[2]))

a    == [1 2 3]
a[0] == 1
a[1] == 2
a[2] == 3



matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
>>> matrix
>>> array([ [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

matrix[1, 1] #accessing matrix @ 2nd row 2nd column
5

matrix[1:, :2]  # row: start grepping from 2nd and on, grep everything up to 2nd column
array([[4, 5],
       [7, 8]])


should_include_elements = [True, False, True] # if the respective include statement is True, will be included into new array
a[should_include_elements]

array([1, 3])

# vectorized operations, otherwise, need to use for loop to loop over the whole list in this following example
# Vectorizing operations means that operations are automatically applied to every element in a vector, 
# which in our case will be a numpy array. So if we are working with a numpy array, we can simply add 1:

original_array = np.array([1, 2, 3, 4, 5])
original_array + 1

array([2, 3, 4, 5, 6])

my_array = np.array([-3, 0, 3, 16])

print('my_array      == {}'.format(my_array))
print('my_array - 5  == {}'.format(my_array - 5))
print('my_array * 4  == {}'.format(my_array * 4))
print('my_array / 2  == {}'.format(my_array / 2))
print('my_array ** 2 == {}'.format(my_array ** 2))
print('my_array % 2  == {}'.format(my_array % 2))

my_array      == [-3  0  3 16]
my_array - 5  == [-8 -5 -2 11]
my_array * 4  == [-12   0  12  64]
my_array / 2  == [-1.5  0.   1.5  8. ]
my_array ** 2 == [  9   0   9 256]
my_array % 2  == [1 0 1 0]

my_array = np.array([-3, 0, 3, 16])

print('my_array       == {}'.format(my_array))
print('my_array == -3 == {}'.format(my_array == -3))
print('my_array >= 0  == {}'.format(my_array >= 0))
print('my_array < 10  == {}'.format(my_array < 10))

my_array       == [-3  0  3 16]
my_array == -3 == [ True False False False]
my_array >= 0  == [False  True  True  True]
my_array < 10  == [ True  True  True False]

# select a certain subset from an array

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
negative = a [a < 0]
len(negative)
# a > 0 -> get an array of bool


my_array[my_array > 0]
array([ 3, 16])

my_array[my_array % 2 == 0]
array([ 0, 16])
# actual process behind the scene of array selection is:
step_1 = my_array % 2
step_2 = step_1 == 0
step_3 = my_array[step_2]
step_3
array([ 0, 16])

# create array
np.random.randn(10)
np.random.randn(3, 4) # second argument to this function to define the shape of a two dimensional array

# create random array from normal distribution, consider the standard deviation(sigma) and avg(mu)
mu = 100
sigma = 30
sigma * np.random.randn(20) + mu

print('np.zeros(3)    == {}'.format(np.zeros(3))) # 3 zeros (float)
print('np.ones(3)     == {}'.format(np.ones(3))) # 3 ones
print('np.full(3, 17) == {}'.format(np.full(3, 17))) # 3 seventeenth
np.zeros(3)    == [0. 0. 0.]
np.ones(3)     == [1. 1. 1.]
np.full(3, 17) == [17 17 17]

np.zeros((2, 3)) # pass a tuple to generate matrix
array([[0., 0., 0.],
       [0., 0., 0.]])

np.arange(4) #basically np. a range
array([0, 1, 2, 3])

np.arange(1, 4) # specify a range, with designated start point, same as normal range in python
array([1, 2, 3])

np.arange(1, 4, 2) #step, a range + third parameter specifying "step" 
array([1, 3])

np.arange(3, 5, 0.5)
array([3. , 3.5, 4. , 4.5])

####### NOTE: MAX is INCLUSIVE! ##########
a range of numbers between a minimum and a maximum, with a set number of elements.
print('min: 1, max: 4, length = 4 -- {}'.format(np.linspace(1, 4, 4)))
print('min: 1, max: 4, length = 7 -- {} '.format(np.linspace(1, 4, 7)))

min: 1, max: 4, length = 4 -- [1. 2. 3. 4.]
min: 1, max: 4, length = 7 -- [1.  1.5  2.  2.5  3.  3.5  4.]


# array method
.min
.max
.sum
.mean
.std

b = [
    [3, 4, 5],
    [6, 7, 8]
]
summ = sum(b[0]) + sum(b[1])
num = len(b[0]) + len(b[1])
avg = summ/num
print(avg)


########################################## Pandas #######################################
Series = 1D
Dataframe = 2D

import pandas as pd

series = pd.Series([100, 43, 26, 17]) # from a list or numpy array
type(series) >> pandas.core.series.Series

series # contain: index (0-3)/ datatype (int64) / name
series.name = 'My Numbers'
series
>>
0    100
1     43
2     26
3     17
Name: My Numbers, dtype: int64 # can also be float64, object (ex: list of strings)

## Vectorized Operations
pandas series are vectorized by default, 
ex: we can easily use the basic arithmatic operators to manipulate every element in the series

apply an operation/ function to every item in a vector/ arrays, without looping

series + 1 # or -,*,/

0    101
1     44
2     27
3     18
Name: My Numbers, dtype: int64

Comparison operators

series == 17

0    False
1    False
2    False
3     True
Name: My Numbers, dtype: bool

series > 40

0     True
1     True
2    False
3    False
Name: My Numbers, dtype: bool


Series method
(series < 0).any() # return T/F any negative values?
(series > 0).all() # return T/F if all are...

pd.Series(['a', 'b', 'a', 'c', 'b', 'a', 'd', 'a']).value_counts()

vowels = list('aeiou')
letters = list('abcdefghijk')
letters_series = pd.Series(letters)
letters_series.isin(vowels) # if in a set or not

count sum mean median min max mode abs std quantile cumsum cummax cummin (cumulative sum, max, min)
{
    'count': series.count(),
    'sum': series.sum(),
    'mean': series.mean()
}


.apply method - apply the function to each element
reference that function when we call .apply

we are not calling the function
we are passing the even_or_odd function itself to .apply method, 
which pandas will then call on every element of the series.

def even_or_odd(n):
    '''
    A function that takes a number and returns a string indicating whether the passed number is even or odd.

    >>> even_or_odd(3)
    'odd'
    >>> even_or_odd(2)
    'even'
    '''
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

series.apply(even_or_odd)

0    even
1     odd
2    even
3     odd
Name: My Numbers, dtype: object


series.apply(lambda n: 'even' if n % 2 == 0 else 'odd')

0    even
1     odd
2    even
3     odd
Name: My Numbers, dtype: object

vectorize string manipulation

strings = ['hello', 'Codeup', 'stUdenTs']
string_series = pd.Series(strings)
string_series.str.lower()

0       hello
1      codeup
2    students
dtype: object

use a series of boolean values to subset a series
series[series > 40]

vowels = list('aeiou')
letters_series[letters_series.isin(vowels)]


cut function from pandas - numerical values >>> discrete bins
s = pd.Series(list(range(15)))
s

pd.cut(s, 3)

0     (-0.014, 4.667]
1     (-0.014, 4.667]
2     (-0.014, 4.667]
3     (-0.014, 4.667]
4     (-0.014, 4.667]
5      (4.667, 9.333]
6      (4.667, 9.333]
7      (4.667, 9.333]
8      (4.667, 9.333]
9      (4.667, 9.333]
10      (9.333, 14.0]
11      (9.333, 14.0]
12      (9.333, 14.0]
13      (9.333, 14.0]
14      (9.333, 14.0]
dtype: category
Categories (3, interval[float64]): [(-0.014, 4.667] < (4.667, 9.333] < (9.333, 14.0]]

# plot from pandas 
%matplotlib inline
import matplotlib.pyplot as plt

series.plot()
series.plot.hist()

# The .value_counts method returns a series, so we can call .plot on the resulting series
pd.Series(['a', 'b', 'a', 'c', 'b', 'a', 'd', 'a']).value_counts().plot.bar()



### pandas dataframe
# create data

import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df) # pandas.core.frame.DataFrame

print(df) # nice organized tabular form
       name  math  english  reading
0     Sally    62       85       80
1      Jane    88       79       67
2     Suzie    94       74       95
3     Billy    98       96       88
4       Ada    77       92       98
5      John    79       76       93
6    Thomas    82       64       81
7     Marie    93       63       90
8    Albert    92       62       87
9   Richard    69       80       94
10    Isaac    92       99       93
11     Alan    92       62       72

df.describe() 
# get descriptive stat
# count, mean, std, min, 25-50-75%, max

# important dataframe "attributes"
# ex: df.dtypes will print out data type of each column 
.dtypes: the data type of each column # no adding parentheses!!!
shape: the number of rows and columns in the dataframe
columns: the list of column names
index: the labels for each row (usually an autogenerated number)

df.index # RangeIndex(start=0, stop=12, step=1)
df.columns = [col.upper() for col in df.columns] # can change name or format of col name

### subset
df[['name', 'math']] # access multiple col

df.math # access 1 col ### PREFERED WAY!
df['math'] # but this way is required if the name of the column is not a valid python identifier

df.drop(columns=['english', 'reading'])
df.rename(columns={'name': 'student'}) # change column name of 'name' to 'student'
df.drop(columns=['english', 'reading']).rename(columns={'name': 'student'}) # chain the above actions into 1 

df['passing_math'] = df.math > 70 # create new column containing the math > 70 result (Bool)
df.assign(passing_english=df.english >= 70) # create new df instead of change old df



# accessing ROWs
df.head() # first 5
df.tail()  # bottom 5
df.sample() # randomly pick the designamted number of rows # df.sample(4) will pick 4 randomly selected rows from df

df.math < 80 # return bool, with math score < 80 printing True
df[df.math < 80] # will return the entire row containing ppl with math score lower than 80

	name	    math    english reading
0	Sally	    62	    85	    80
4	Ada	        77	    92	    98
5	John	    79	    76	    93
9	Richard	    69	    80	    94

df.sort_values(by='english')

# most df methods create a new df, so chaining is common

# find the name of the student with the lowest english grade above a 90
# .name: extract just the name part of the record
df[df.english > 90].sort_values(by='english').head(1).name

# connect SQL
Whenever we want to connect to a database from our python code  
we will need a driver, a bit of software that handles the details of the database connection.
## software: mysqlclient
create_engine function from the sqlalchemy module 
to create an engine that pandas can use to execute a query and construct a dataframe

from sqlalchemy import create_engine

from env import user, password, host

url = 'mysql+pymysql://{}:{}@{}/fruits_db'.format(user, password, host)

dbc = create_engine(url)

df = pd.read_sql('SELECT * FROM fruits', dbc)

# JSON
data = '''
[
  {"name": "apple", "quantity": 3},
  {"name": "banana", "quantity": 4},
  {"name": "cantelope", "quantity": 16},
  {"name": "dragonfruit", "quantity": 1},
  {"name": "elderberry", "quantity": 2}
]
'''.strip()

with open('fruits.json', 'w') as f:
    f.write(data)
pd.read_json('fruits.json')
