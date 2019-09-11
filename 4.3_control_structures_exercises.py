## Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not
Prompt_day = input("Which day is it (Monday - Sunday? ")
if Prompt_day == 'Monday':
	print("Yes it is Monday.")
else:
	print("not Monday")
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
Prompt_date = input("Which day is it (Monday - Sunday? ")
if Prompt_date == 'Saturday':
	print("Weekend")
elif Prompt_date == "Sunday":
	print("Weekend")
else:
	print("weekday")
#create variables and make up values for

#the number of hours worked in one week
hour_in_one_week = 70

#the hourly rate
hourly_rate = 15
#how much the week's paycheck will be 
weekly_paycheck = hour_in_one_week * hourly_rate

# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

weekly_paycheck_bonus = weekly_paycheck + (hour_in_one_week-40)*0.5*hourly_rate
weekly_paycheck
weekly_paycheck_bonus

## Loop Basics

# While

# Create an integer variable i with a value of 5.
i = 5
# Create a while loop that runs so long as i is less than or equal to 15
while i in range(1,16)
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i in range(5,16):
	print (i)
	i += 1
# print out: 5 6 7 ...14 15

# Create a while loop that will count by 2's starting with 0 and ending at 100. 
i = 0
while i in range(0,101):
	print(i)
	i+=2
# Follow each number with a new line.
i = 0
while i in range(0,101):
	print(i)
	print(' ')
	i+=2
# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i in range(-10,101):
	print(i)
	i-=5

# Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000. Output should equal:
i = 2
print(i)
while i in range(2,1000000):
	if i ** 2 < 1000000:
		print(i ** 2)
		i **= 2
	else:
		break
# Write a loop that uses print to create the output shown below.
"""
100
95
90
85
...
20
15
10
5
"""
i = 100
while i in range(5,101):
	print(i)
	i -= 5


## For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# For example, if the user enters 7, your program should output:
"""
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
"""
x = input('Please give me a number: ')
x = int(x)
for i in range(1,11):
	multiply = i * x
	print(x,' x ', i, ' = ', multiply)
	i += 1

# Create a for loop that uses print to create the output shown below.
for i in range(1,10):
	#i = str(i)
	print (str(i) * i)
	i += 1
"""
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

## break and continue

# prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

user_input = input("A number between 1 and 50: ")
user_input = int(user_input)

i = 1
for i in range (1,51):
	if user_input % 2 != 0:
		continue
	print('Here is an odd number: ', user_input)


if user_input 
	break

	continue
print('Here is an odd number': inp)
"""
Your output should look like this:

Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
...
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
"""


# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
count_to_inp = input("Give me a number: ")
print(count_to_inp.isdigit())
count_to_inp = int(count_to_inp)
i = 0
for 0 in range(0, count_to_inp+1):

