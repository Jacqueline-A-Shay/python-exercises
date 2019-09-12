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














