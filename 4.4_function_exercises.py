"""Define a function named is_two. 
It should accept one input and return True if the passed input is either 
the number or the string 2, False otherwise."""

def is_two(get_num):
	if get_num == 2 or get_num == str(2):
		return True
	else:
		return False
is_two(5)

"""Define a function named is_vowel. It should return True if the passed string is a vowel, 
False otherwise.
"""
def is_vowel(obtain_string):
	# obtain_string = str(obtain_string.split('').lower())
	obtain_string = str(obtain_string)
	obtain_string = obtain_string.lower()
	if obtain_string in ('a','e','i','o','u'):
		return True
is_vowel('a')


def is_vowel(strin):
	strin = ','.join(strin)
	strin = strin.split(',')
	x = [s for s in strin if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') > 1]
	if x != 0:
		True
	else:
		False
	
is_vowel('apple')


"""Define a function named is_consonant. It should return True if the passed string is a consonant, 
False otherwise. Use your is_vowel function to accomplish this."""

def is_consonant(c_strin):
	vowel_set = set("aeiouAEIOU")
	for c in c_strin:
		if c not in vowel_set:
			return True
		else:
			True
is_consonant('csq')		


"""Define a function that accepts a string that is a word. 
The function should capitalize the first letter of the word if the word starts with a consonant."""	
def capitalize_consonant(target_con):
	vowel_set = set("aeiouAEIOU")
	for word in target_con:
		if word in vowel_set:
			return target_con
		else:
			return target_con.capitalize()


capitalize_consonant("kpple")


"""Define a function named calculate_tip. It should accept a tip percentage 
(a number between 0 and 1) and the bill total, and return the amount to tip."""
def calculate_tip(tip_percentage, bill):
	if tip_percentage > 0 and tip_percentage < 1:
		return bill * tip_percentage
calculate_tip(0.2, 18)

"""Define a function named apply_discount. It should accept a original price, 
and a discount percentage, and return the price after the discount is applied."""
def apply_discount(original_price, discount_percentage):
	if discount_percentage > 0 and discount_percentage < 1:
		return original_price * (1 - discount_percentage)

apply_discount(55,0.5)

"""Define a function named handle_commas. It should accept a string that is a number 
that contains commas in it as input, and return a number as output."""
def hand_commas(num_with_commas):
	return (num_with_commas.replace(',',''))
hand_commas('55,555')

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

"""Define a function named remove_vowels that accepts a string and 
returns a string with all the vowels removed."""

def remove_vowels(rm_target):
	vowel_set = set('aeiouAEIOU')
	edited_no_vowel = [i for i in rm_target if i not in vowel_set]
	return edited_no_vowel
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

def normalized_name(valid_py_name):
	NG_py_identifier = set('!@#$%^&*()+,?')
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
def cumsum(list_of_num):
	list_of_num = [list_of_num]
	post_process = []
	sum_num = 0
	for idx, val in enumerate(list_of_num):
		sum_num += int(val)
		post_process = post_process.append(sum_num)
	return post_process
		
	#return post_process
cumsum('1, 2, 3')


def cumsum(list_of_num):
	list_of_num = [list_of_num]
	post_process = []
	sum_num = 0
	for val in enumerate(list_of_num):
		print(idx, val)
cumsum('1, 2, 3')
	#index sum(i in range(x[0],x[current ])

	# for i in range(list_of_num) and x in list_of_num:
	# 	append(x + 

cumsum('1, 2, 3')
def cumsum(list_of_num):
	sum = 0
	post_process = []
	for item in list_of_num:
		yield sum
		sum += item
		post_process = post_process.append(sum)
	return post_process
cumsum('1, 2, 3')


def cumsum(it):
    total = 0
    new_ls = []
    for x in it:
        total += x
        yield total
list(cumsum([1,2,3,4,5]))

a = [1, 2, 3 ,4, 5]
print(type(a))
cumsum = [sum(a[:i+1]) for i in range(len(a))]   
cumsum

def cumsum(list_of_num):
	list_of_num = [list_of_num]
	result = [sum(list_of_num[:i+1]) for i in range(len(list_of_num))]   
	return result
cumsum('1, 2, 3')


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







