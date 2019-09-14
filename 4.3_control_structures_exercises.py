## Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not
Prompt_day = input("Which day is it (Monday - Sunday)? ")
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

if <= 40:
else: 


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
while i <= 15:
	print(i)
	i += 1
# print out: 5 6 7 ...14 15

# Create a while loop that will count by 2's starting with 0 and ending at 100. 
i = 0
while i in range(0,101):
	print(i)
	i+=2

while i <= 100:
	print(i)
	i += 2

for i in range(0,102,2):
	print(i)
# Follow each number with a new line.
i = 0
while i in range(0,101):
	print(i)
	print(' ')
	i+=2

for i in range (100,-10,-5):
	print(i)
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
i = 2
while i < 1000000:
	print(i)
	i = i**2
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
odd_num = ""
while True:
	odd_num

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
count_to_inp = input("Give me a positive number: ")
print(count_to_inp.isdigit())
count_to_inp = int(count_to_inp)
i = 0
for i in range(0,count_to_inp+1):
	print(i)
	i += 1


count_to_inp = input("Give me a positive number: ")
print(count_to_inp.isdigit())
count_to_inp = int(count_to_inp)
sum_range = range(0, count_to_inp+1)
counting = sum(sum_range)
print(counting)

# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
count_to_n_inp = input("Give me an integer: ")
print(count_to_n_inp.isdigit())
count_to_n_inp = int(count_to_n_inp)
i = count_to_n_inp
while i in range(1,count_to_n_inp+1):
	print(i)
	i -= 1


## Fizzbuzz

"""One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"."""
i = 1
for i in range(1,101):
	print(i)
	i += 1

fb = input("Give me a number between 1 and 100, please. ")
print(fb.isdigit())
fb = int(fb)
def fizzbuzz_check(fb):
	if fb % 3 == 0 and fb % 5 == 0:
		return "FizzBuzz"
	elif fb % 3 == 0:
		return "Fizz"
	elif fb % 5 == 0:
		return "Buzz"
	
fizzbuzz_check(fb)

## Display a table of powers.

"""Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
Example Output"""
power_table = input("What number would you like to go up to? ")
power_table.isdigit()
power_table = int(power_table)
print("                             ")
i = 1
print("Here is your table!")
print("                             ")
print('{:<8s}{:>8s}{:>8s}'.format("number","squared","cubed"))
print ('{:_^15}{:_^6}{:_^3}'.format(' | ',' | ',''))

for i in range(1,power_table+1):
	print('{0:2d} {1:9d} {2:9d}'.format(i, i ** 2, i ** 3))
	#print(str(i), str(i ** 2), str(i ** 3))
	#print('{:<8s}{:>8s}{:>8s}'.format(i, i ** 2, i ** 3))
	i += 1

""" What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125

"""

"""Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0"""

grader = input("Ask me to convert 0-100 score into letter grade: ")
grader.isdigit()
grader = int(grader)
while grader in range(0,101):
	if grader >= 88:
		print('A')
	elif grader <= 87 and grader >= 80:
		print('B')
	elif grader <= 79 and grader >= 67:
		print('C')
	elif grader <= 66 and grader >= 60:
		print('D')
	else:
		print('F')

	choice = input("Would you like to continue? ")
	if choice == "No":
		break


"""Create a list of dictionaries where each dictionary represents a book that you have read. 
Each dictionary in the list should have the keys title, author, and genre. 
Loop through the list and print out information about each book.

Prompt the user to enter a genre, then loop through your books list and print 
out the titles of all the books in that genre."""

book_list = [{"Title": "Vendetta In Death","Author": "J.D. Robb", "Genre": "Urban Fantasy"},
			{"Title": "Where the Crawdads Sing","Author":"Delia Owens", "Genre": "Literary Fiction"},
			{"Title": "The Goldfinch", "Author": "Donna Tartt", "Genre": "Literary Fiction"}]
"""for index in range(len(book_list)):
	for key in book_list[index]:
		print(book_list[index][key])
print(*[content for dic in book_list for content in dic.values()], sep=' ')
"""
lookup_genre = input("Genre? ")

#keyvalset = ["Urban Fantasy"]
def get_genre(lookup_genre):
	keyvalset = [lookup_genre]
	printout_genre = list(filter(lambda d: d['Genre'] in keyvalset, book_list))
	return printout_genre

get_genre(lookup_genre)





print([d for d if keyvalset in book_list])



"""  Conditional Basics
a)prompt the user for a day of the week, print out whether the day is Monday or not
b)prompt the user for a day of the week, print out whether the day is a weekday or a weekend
c)create variables and make up values for
 the number of hours worked in one week
  the hourly rate
how much the week's paycheck will be
write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours  """

#Exercise 1a
day_of_week=input("Enter a day of the week")
if day_of_week=='Monday':
    print("It's Monday")
else:
    print("Sorry not Monday!")    
#Exercise 1b
weekend_or_not=input("Enter a day of the week")
if weekend_or_not in ['Saturday','Sunday']:
    print("It's the weekend!,Let's party") 
else:
     print("Sorry it's a workday") 
# Exercise 1c
num_hours=50
hour_wage=11

if num_hours<=40:
    paycheck=num_hours*hour_wage
    print(paycheck)
else:
    paycheck=(num_hours-40)*1.5*hour_wage+40*hour_wage
    print("The weeks paycheck will be: "+str(paycheck))

""" Loop Basics
While
Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.
Your output should look like this:
5
6
7
8
9
10
11
12
13
14
15
Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
Alter your loop to count backwards by 5's from 100 to -10.
Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
 2
 4
 16
 256
 65536
Write a loop that uses print to create the output shown below.
100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
For Loops
Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
For example, if the user enters 7, your program should output:
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
Create a for loop that uses print to create the output shown below.
1
22
333
4444
55555
666666
7777777
88888888
999999999
break and continue
Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
Your output should look like this:
Number to skip is: 27
Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49
The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.   
 """
#Exercise 2a.1
i=5
while i<=15:
    print(i)
    i+=1  

#Exercise 2a.2
for i in range(0,102,2):
    print(i)

i=0    
while i<=100:
    print(i)
    i+=2

#Exercise 2a.3
for i in range(100,-10,-5):
    print(i)

i=100
while i>=-10:
    print(i)
    i-=5


#Exercise 2a.4
i=2
while i<1000000:
    print(i)
    i=i**2
    

#Exercise 2a.5
for i in range(100,0,-5):
    print(i)

i=100
while i>=5:
    print(i)
    i-=5


#Exercise 2b.1
num=input("Enter a number") 
num=int(num)
for i in range(1,11):
    print(str(i)+"*"+str(num)+"="+str(i*num)) 

#Exercise 2b.2
for num in range(1,10):
    print(str(num)*num)

#Exercise 2c.1 

odd_num=""
while True:
    odd_num=input("Enter an odd number between 1 and 50")
    if odd_num.isdigit() and int(odd_num)%2==1 and int(odd_num)>1 and int(odd_num)<50:
        break

for i in range(1,50,2):
    if i==int(odd_num):
        print("Yikes! Skipping number: "+str(i))
        continue
    print("Here is an odd number: "+str(i))
# Exercise 2d.1
pos_num=""

while True:
    pos_num=input("Please enter a positive number")
    if pos_num.isdigit() and int(pos_num)>0:
        break

for i in range(1,int(pos_num)+1):
    print(i)

#Exercise 2e.1
pos_num=""
while True:
    pos_num=input("Please enter a positive number")
    if pos_num.isdigit() and int(pos_num)>0:
        break
for i in range(int(pos_num),0,-1):
    print(i)

""" Fizzbuzz
One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
 """

#Exercise 3
for i in range (1,101):
     if i%3==0 and i%5==0:
         print("FizzBuzz")
     elif i%3==0:
         print("Fizz")
     elif i%5==0:
         print("Buzz")
     else:
         print(str(i))
#Exercise 4
""" Display a table of powers.
Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
Example Output
What number would you like to go up to? 5
Here is your table!
number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
Bonus: Research python's format string specifiers to align the table   """ 
while True:
    num_test=int(input("Please enter an integer"))
    for i in range(1,num_test+1):
        if i==1:
            print('number  | squared  | cubed')
            print('______  |  ______  |  ______')
    print(i,'  |', i**2,'  |',i**3)
    user_choice=input("Should we continue ?")
    if user_choice="no":
        break
    
#Exercise 5
""" Convert given number grades into letter grades.
Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:
A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
Bonus
Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+). """
while True:
    num_grade=input("Please enter a grade between 0 and 100")
    num_grade=int(num_grade)
    if num_grade>=88:
        print('A')
    elif num_grade>=80:
        print('B')
    elif num_grade>=67:
        print('C')
    elif num_grade>=60:
        print('D') 
    else:
        print('F')
    prompt_user_continue=input("Would you like to continue? Y/N") 
    if prompt_user_continue.upper()=="N":
        break

#Exercise 6
""" Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre. """

book_list=[{'title':"Lamb",'author':"Christopher Moore",'genre':"fiction"},
{'title':"The Lean Startup",'author':"Eric Ries",'genre':"business"},{'title':"Devil in a White City",'author':"Eric Larson",'genre':"True Crime"},{'title':"Tom Sawyer",'author':"Mark Twain",'genre':"fiction"}]
for book in book_list:
    print("The book title is: "+book['title'])
    print("The book author is: "+book['author'])
    print("The book genre is: "+book['genre'])


#Exercise 6.a
genre_filter=input("Please enter a genre")
for book in book_list:
    if book['genre']==genre_filter:
        print("The book title is: "+book['title'])
        print("The book author is: "+book['author'])
