"""reusable block of code
black box
functions do things or transform things
function are commands 
functions are operators that transform values
built-in functions exist in every language and we have user-define functions
Our functions are concretions/manifestations of our design"""

functions are like lil' machines
f(x) = x + 1
f(3) = 3 + 1

anatomy of a function
1. def keyword
2. snake_case of the function name 
    - name the function a verb or verb phrase
3. parameters in the parentheses (variable(s) to hold inputs):
4. body of the function is all the code that's indented into the function
5. return value (return exits the function and returns the value to where you called the function

def add_one(x):
    return x + 1

result = add_one(5)
print(result)

## Function Two-Step Process
Step 1: Define the function w/ the functionality you need
Step 2: Call the function, sending in any inputs

result = one_add(5)

def honk():
    print("HONK HONK")

result = honk()


0 -> 0
23 -> 23
"banana" -> "banana"
len("mango") -> 5

def print_twenty():
    return print(20)

def return_twenty():
    return 20

// defining the result variable to hold the return of return_twenty() + 5
result = return_twenty() + 5

result = int(print_twenty()) + 5


x = add_one(5)
y = add_one(1)
z = add_one(-238)

result = add_one(times_three(10))
print(result)

print(add_one(add_one(add_one(11))))

what is a function?
anatomy of a function?


lambda = greek letter L
lambda calculus
lambdas can only be a single line
lambdas have an implicit return

lambda syntax
square = lambda x: x**2

function definition syntax
def square(x):
    return x ** 2


fruits = [
    {
        "name": "mango",
        "quantity": 10,
        "price": 3
    },
    {
        "name": "banana",
        "quantity": 3,
        "price": 1
    }
    {
        "name": "kiwi",
        "quantity": 23,
        "price": 4
    }
]

# Sort the fruits in alphabetical order 

# get the fruit with the lowest price
min(fruits, key=lambda x: x["price"])

# get the fruit with the lowest quantity
min(fruits, key=lambda x: x["quantity"])["quantity"]

def get_by_quantity(x):
    return x["quantity"]

min(fruits, key=get_by_quantity)

# sort the list of dictionaries alphabetically
sorted(fruits, key=lambda x:x["name"])

# sort the list of dictionaries by quantity
sorted(fruits, key=lambda x:x["quantity"])

# sort the list of dictionaries by price
sorted(fruits, key=lambda x:x["price"])