# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]
output1 = [fruit.upper() for fruit in fruits]
output1

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like 
# ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint:You'll need a way to check if something is a vowel.
vowel = 'a','e','i','o','u','A','E','I','O','U'
vowels = "AeEeIiOoUu"

fruits_with_more_than_two_vowels = [fruit in fruits if vowel in fruit]
fruits_with_more_than_two_vowels
# len(result from determining if vowel exist) > 2


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# Exercise 5 - make a list that contains each fruit with more than 5 characters

more_than_5_char = [fruit for fruit in fruits if len(fruit) > 5]
more_than_5_char

Out: ['strawberry', 'pineapple', 'mandarin orange']
# Exercise 6 - make a list that contains each fruit with exactly 5 characters
exactly_5_char = [fruit for fruit in fruits if len(fruit) == 5]
exactly_5_char

Out: ['mango', 'guava']
# Exercise 7 - Make a list that contains fruits that have less than 5 characters

less_than_5_char = [fruit for fruit in fruits if len(fruit) < 5]
less_than_5_char
Out: ['kiwi']
# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
count_fruit_char = [len(fruit) for fruit in fruits]
count_fruit_char
Out: [5, 4, 10, 5, 9, 15]
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
fruits_with_letter_a
Out: ['mango', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number%2 == 0]
even_numbers
Out: [2, 4, 6, 8, 10, 256, -8, -4, -2]
# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number%2 == 1]
odd_numbers
Out: [3, 5, 7, 9, 11, 13, 17, 19, 23, 5, -9]
# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
positive_numbers
Out: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, 5]
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
negative_numbers
Out: [-8, -4, -2, -9]
# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
more_numerals = [number for number in numbers if len(str(number).strip('-')) >= 2]
more_numerals

Out: [10, 11, 13, 17, 19, 23, 256]
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. 
# Output is [4, 9, 16, etc...]
numbers_squared = [(number, number**2) for number in numbers]
numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.