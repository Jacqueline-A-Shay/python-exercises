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
	valid_py_name = valid_py_name.strip(' ')
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
	"""
				valid_py_name = valid_py_name.strip(' ')
				valid_py_name = valid_py_name.replace(' ','_')"""

	"""
		turn into list
		loop to 
		slice off x[0] x[-1] space
		turn all remaining space into underscore

	"""

	return  "".join([i for i in valid_py_name if i not in NG_py_identifier])
	
normalized_name('% Completed')

"""Write a function named cumsum that accepts a list of numbers and 
returns a list that is the cumulative sum of the numbers in the list.
cumsum([1, 1, 1]) returns [1, 2, 3]
cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]"""
