x = "yelp!"
import functions_exercises
functions_exercises.capitalize_consonant(x)

tip_percentage = '0.5'
bill = '50'
from functions_exercises import calculate_tip

x = '15,000'
from functions_exercises import handle_commas('15,000') as hc


In [38]: a = ['1','2','3']                                                      
In [39]: b = ['a','b','c']                                                      
In [40]: for r in itertools.product(a,b): print(r[0] + r[1])   

for r in itertools.product(b,b): print(r[0] + r[1])   #but how to count?



import json
from pprint import pprint                                              

with open('profiles.json', encoding='utf-8') as data_file: 
	data = json.loads(data_file.read()) 

data    

count = 0
for feature in data:
	count += 1
print(count)

#Total number of users
for feature in data:
	(data.count(feature["_id"]))

from collections import Counter
count = Counter()
for item in data:
    for key, value in item.items():
        if key.startswith('_id'):
            count.update([key[4:]])

# Number of active users
# Number of inactive users
ca = 0
ci = 0
for feature in data:
	print(sum(feature["isActive"].values(1)))

#find the lowest 
# lowest_balance = first_user = profile[0]
# go thru list, replace whenever lower than profile[0]
# so we have all the info associated for further use


# fruit_counts.items() > turn dictionary into [(k1,v1), (k2,v2)...]
counts = list(fruit_counts.items())
counts[1] = ('apple', 16)
min(counts, key=lambda pair: pair[1])
"""Define a function named is_two. 
It should accept one input and return True if the passed input is either 
the number or the string 2, False otherwise."""

def is_two(x):
	return x == 2 or x == '2' or x == 'two' 

def is_two(get_num):
	if get_num == 2 or get_num == str(2):
		return True
	else:
		return False

def is_two(x):
    return x in [2, '2', 'two']

assert is_two(2) == True
assert is_two('2') == True
assert is_two('four') == False
assert is_two(3) == False
assert is_two(4) == False
assert is_two('two') == True
"""Define a function named is_vowel. It should return True if the passed string is a vowel, 
False otherwise.
"""
def is_vowel(x):
	vowels = set('aeiouAEIOU')
	return len(x) == 1 and x in vowels

def is_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len(c) == 1 and c.lower() in vowels
    
def is_vowel(c):
    return len(c) == 1 and c.lower() in 'aeiou'


assert is_vowel('a') == True
assert is_vowel('e') == True
assert is_vowel('i') == True
assert is_vowel('o') == True
assert is_vowel('u') == True
assert is_vowel('b') == False
assert is_vowel('y') == False
assert is_vowel('A') == True
assert is_vowel('ab') == False
assert is_vowel('aa') == False
"""Define a function named is_consonant. It should return True if the passed string is a consonant, 
False otherwise. Use your is_vowel function to accomplish this."""

def is_consonant(x):
	vowels = set("aeiouAEIOU")
	return len(x) == 1 and x not in vowels


def is_consonant(c):
	return not is_vowel(c)

def is_consonant(c):
    return not is_vowel(c)


assert is_consonant('c') == True
assert is_consonant('C') == True
assert is_consonant('a') == False


	
"""Define a function that accepts a string that is a word. 
The function should capitalize the first letter of the word if the word starts with a consonant."""	
def capitalize_consonant(x):
	vowels = set("aeiouAEIOU")
	return x.capitalize() if x[0] not in vowels else x
	# x.capitalize() if x[0] not in vowels


def capitalize_consonant(c):
	if is_consonant(c[0]):
		return c.capitalize()
	return c


def cap_if_conso(word):
	word.capitalize() if is_consonant(c[0]) else c


def cap_if_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word

def cap_if_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize()
    return word

def cap_if_consonant(word):
    return word.capitalize() if is_consonant(word[0]) else word

assert cap_if_consonant('codeup') == 'Codeup'
assert cap_if_consonant('bayes') == 'Bayes'
assert cap_if_consonant('aardvark') == 'aardvark'


"""Define a function named calculate_tip. It should accept a tip percentage 
(a number between 0 and 1) and the bill total, and return the amount to tip."""
def calculate_tip(tip_percentage, bill):
	if tip_percentage > 0 and tip_percentage < 1:
		return bill * tip_percentage
assert calculate_tip(0.2, 18) == 3.6
assert calculate_tip(0.25, 80) == 20.0

def calculate_tip(tip_percentage, bill):
	if tip_percentage > 1:
		percentage /= 100

	return bill * tip_percentage
assert calculate_tip(0.2, 18) == 3.6
assert calculate_tip(0.25, 80) == 20.0


"""Define a function named apply_discount. It should accept a original price, 
and a discount percentage, and return the price after the discount is applied."""
def apply_discount(original_price, discount_percentage):
	if discount_percentage > 0 and discount_percentage < 1:
		return original_price * (1 - discount_percentage)

apply_discount(55,0.5)

"""Define a function named handle_commas. It should accept a string that is a number 
that contains commas in it as input, and return a number as output."""
def handle_commas(x):
	return float(x.replace(",",""))



def hand_commas(s):
	return float("".join([c for c in s if c != ',']))
assert hand_commas('55,555') == 55555
assert hand_commas('1,000,000') == 1000000

'a,b,b,d'.split(',') # turn string into list OR list('abcd') 
"".join([]) # .join will use a string as a 'glue' to put a list together


def handle_commas(s):
    return float(''.join([c for c in s if c != ',']))

assert handle_commas('1,000') == 1000.0
assert handle_commas('10') == 10.0
assert handle_commas('1,000,000') == 1000000



"""Define a function named get_letter_grade. 
It should accept a number and return the letter grade associated with that number (A-F)."""

def get_letter_grade(grade):
	if grade > 0 and grade < 100:
		grade = int(grade)
		if grade >= 90:
			print('A')
		elif grade >= 80:
			print('B')
		elif grade >= 70:
			print('C')
		elif grade >= 60:
			print('D')
		else:
			print('F')
get_letter_grade(88.5) 

grade = {
	'A':range(94,101),
	'B':range(87,94),
	'C':range (80,87),
	'D':range(70,80),
	'F':range(0,70)
}

def get_letter_grade(n):

	for grade_letter, grade_range in grades.item():
		if round(n) in grade_range:
			return grade_letter
		return 'Error'

grade_minimums = (
    ('A+',98.5),('A',91.5),('A-',89.5),
    ('B+',88.5),('B',81.5),('B-',79.5),
    ('C+',78.5),('C',71.5),('C-',69.5),
    ('D+',68.5),('D',61.5),('D-',59.5),
    ('F',0)
)

def get_letter_grade(numeric_grade):
    ubound = max(100, numeric_grade + .01)
    for grade in grade_minimums:
        if numeric_grade < grade[1]:
            ubound = grade[1]
        else:
            return grade[0]
        

assert get_letter_grade(150) == 'A+'
assert get_letter_grade(98.4) == 'A'
assert get_letter_grade(91) == 'A-'
assert get_letter_grade(59.4) == 'F'
assert get_letter_grade(81.5) == 'B'
assert get_letter_grade(89.5) == 'A-'

get_letter_grade(90)

grades = {
    'A': range(94, 101),
    'B': range(87, 94),
    'C': range(80, 87),
    'D': range(70, 80),
    'F': range(0, 70)
}

def get_letter_grade(n):
    for grade_letter, grade_range in grades.items():
        if round(n) in grade_range:
            return grade_letter
    return 'Error: don\'t know how to get a letter grade for %s' % n

get_letter_grade(80)




"""Define a function named remove_vowels that accepts a string and 
returns a string with all the vowels removed."""

def remove_vowels(rm_target):
	vowel_set = set('aeiouAEIOU')
	#edited_no_vowel = [i for i in rm_target if i not in vowel_set]
	return ("".join([i for i in rm_target if i not in vowel_set])).replace(" ","")
remove_vowels('apple of my eye')

"""Define a function named normalize_name. It should accept a string and 
return a valid python identifier, that is:
anything that is _______ should be removed:
	not a valid python identifier (ex: !, @, #, $, %)
	leading and trailing whitespace 
	everything should be lowercase
	spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed"""
def normalized_name(x):
	weird = set('!@#$%')
	alphabets = set("_abcdefghijklmnopqrstuvwxyz0123456789")
	x = x.strip()
	return [w.lower() for w in x if w.lower() in alphabets and not in weird]
	
assert normalized_name('% Completed') == 'completed'


def normalized_name(valid_py_name):
	NG_py_identifier = set('!@#$%')
	valid_py_name = str(valid_py_name)
	valid_py_name = valid_py_name.strip()
	valid_py_name = valid_py_name.replace(' ','_')
	valid_py_name = valid_py_name.lower()
	return  "".join([i for i in valid_py_name if i not in NG_py_identifier])
	
normalized_name('% Completed')
# this will turn ALL space into underscore
# but for the leading and trailing white space we want to remove instead
def normalized_name(valid_py_name):
	NG_py_identifier = set('!@#$%^&*()+,?')
	valid_py_name = str(valid_py_name)
	valid_py_name = valid_py_name.lower()
	valid_py_name = [valid_py_name]
	if valid_py_name[0] == ' ':
		valid_py_name = valid_py_name[1:]
	if valid_py_name[-1 ] == ' ':
		valid_py_name = valid_py_name[:-1]
		# valid_py_name = str(valid_py_name)
		# valid_py_name = valid_py_name.replace(' ','_')
		return  "".join([i for i in valid_py_name if i not in NG_py_identifier])

	"""
				valid_py_name = valid_py_name.strip(' ')
				valid_py_name = valid_py_name.replace(' ','_')"""

	"""
		turn into list
		loop to 
		slice off x[0] x[-1] space
		turn all remaining space into underscore

	"""
return_value = normalized_name('% Completed ')
assert return_value == '_completed','you can comment on your assert'
def sayhello(name):
	return 'hello, {}!'.format(name)
	return 'hello,' + name + '!'
	return 'hello, %s!' %name
	return f'hello, {name}!' #most recommended
sayhello('bayes')
assert sayhello('bayes') == 'hello, bayes!'
# assert
# sanity check, also better for future code reader to understand what's 
# the expected output and more clear there's this sanity check here
# if test ok, no result will show
# only show false

# ipython -i file_name.py
# can pass in different part of the code and run individually

"""Write a function named cumsum that accepts a list of numbers and 
returns a list that is the cumulative sum of the numbers in the list.
cumsum([1, 1, 1]) returns [1, 2, 3]
cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]"""
LETTERS = ' _abcdefghijklmnopqrstuvwxyz0123456789'
def normalize_name(python_identifier):
    python_identifier = python_identifier.lower()
    valid_chars = []
    for character in python_identifier:
        if character in LETTERS:
            valid_chars.append(character)
    return ''.join(valid_chars).strip().replace(' ', '_')



# Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format. 

# Bonus write a function that does the opposite.

def twelveto24(time):
	if time[-2: ] != "PM":
		return (time.replace("AM",""))
	if time[-2: ] == "PM":
		time = time.replace("PM","")
		return time.replace(time[0:2], str((int(time[0:2]) + 12)))
		# hh + 12

twelveto24("09:45AM")





# Create a function named col_index. It should accept a spreadsheet column name, 
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

def col_index(col_name):
	#converty alphabets to numbers







