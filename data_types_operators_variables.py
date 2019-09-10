type("False") # string
type(False) #Boolean
type("0") #str
type(0) #int
type(True) #Boolean
type("True") #str
type([{}]) #list
type({'a':[]}) #dict

"""
What data type would best represent:

A term or phrase typed into a search box? 
# str

If a user is logged in?
# Boolean

A discount amount to apply to a user's shopping cart?
# float

Whether or not a coupon code is valid?
# Boolean

An email address typed into a registration form?
# str

The price of a product?
# float

A Matrix?
# list or dict?

The email addresses collected from a registration form?
# dict

Information about applicants to Codeup's data science program? 
# dict
"""

'1' + 2 # type error

6 % 4 # 2

type(6 % 4) # int

type(type(6 % 4)) # type

'3 + 4 is' + 3 + 4 # type error
 
 0 < 0 # False

 'False' == False # False

 True == 'True' #False

5 >= -5 # True

!False or False # return nothing

True or "42" # True

!True && !False # /bin/bash: !False: command not found

6 % 5 # 1

5 < 4 and 1 == 1 # False

'codeup' == 'codeup' and 'codeup' == 'Codeup' # False

4 >= 0 and 1 !== '1'  # !== invalid 
4 >= 0 and 1 != '1'	# True

6 % 3 == 0 # True

5 % 2 != 0 # True

[1] + 2 # can't concat list and int

[1] + [2] # [1,2]

[1] * 2 # [1,1]

[1] * [2] # can't multiply list by non-int

[] + [] == [] # true

{} + {} # type error

"""You have rented some movies for your kids: 
The little mermaid (for 3 days), 
Brother Bear (for 5 days, they love it), 
and Hercules (1 day, you don't know yet if they're going to like it). 
If price for a movie per day is 3 dollars, how much will you have to pay?"""


little_mermaid = 3
Brother_bear = 5
Hercules = 1
Total_rental_fee = (little_mermaid + Brother_bear + Hercules) * 3
Total_rental_fee

"""
Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
and Facebook 350. How much will you receive in payment for this week? 
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
"""

Google = 400
Amazon = 380
Facebook = 350
Salary = Google * 6 + Facebook * 10 + Amazon * 4
Salary

"""
A student can be enrolled to a class only if the class is not full and 
the class schedule does not conflict with her current schedule.
"""
if schedule >= 21:
	print("reject enrollment")
elif schedule == :
	print("reject enrollment")
else:
	print("proceed")



"""A product offer can be applied only if people buys more than 2 items, 
and the offer has not expired. Premium members do not need to buy a specific amount of products."""
if membership == "Premium":
	print("good to go")
elif item >= 2 and offer_expire = False:
	print("good to go")
else:
	print("promo reject")

username = 'codeup'
password = 'notastrongpassword'
"""Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace"""

len(password) >= 5
len(username) < 20
username != password

result = [password.startswith(' '), username.startswith(' ')]
print(result)









