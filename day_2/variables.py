# Day 2: 30 Days of Python programming

# Declaring variables
first_name = "Dan"
last_name = "Saviour"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Lagos"
age = 25
year = 2024
is_married = False
is_true = True
is_light_on = True

# Declaring multiple variables on one line
a, b, c = 1, 2, 3

'''Exercises: Level 2
Checking the Data Type of Variables'''

# Checking the data type of all variables
print(type(first_name))  # str
print(type(last_name))   # str
print(type(full_name))   # str
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # bool
print(type(is_true))     # bool
print(type(is_light_on)) # bool
print(type(a), type(b), type(c)) # int, int, int


# Finding the length of first_name
print(len(first_name))  # Output: Length of the first name
# Comparing lengths of first_name and last_name
print(len(first_name) == len(last_name))  # True/False
print(len(first_name) > len(last_name))   # True/False
print(len(first_name) < len(last_name))   # True/False
# Declaring numbers
num_one = 5
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Printing results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

# Declaring numbers
num_one = 5
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Printing results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

# Radius of the circle
radius = 30

# Calculations
pi = 3.14159
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

# Results
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

# Getting user details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

# Displaying user details
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# Checking Python reserved keywords
help('keywords')
