# Day 3: 30 Days of Python programming - Operators Exercise

# Task 1:Declaring variables
age = 25                 # Integer variable
height = 5.9             # Float variable
complex_number = 3 + 4j  # Complex number variable

# Task2: Prompting user for base and height of a triangle
base = float(input("Enter the base of the triangle (in meters): "))
height_of_triangle = float(input("Enter the height of the triangle (in meters): "))
# Calculating the area of the triangle
area = 0.5 * base * height_of_triangle
# Displaying the result
print(f"The area of the triangle is {area} square meters.")

# Prompting user for the sides of the triangle
side_a = float(input("Enter the length of side a (in meters): "))
side_b = float(input("Enter the length of side b (in meters): "))
side_c = float(input("Enter the length of side c (in meters): "))

# Calculating the perimeter of the triangle
perimeter = side_a + side_b + side_c

# Displaying the result
print(f"The perimeter of the triangle is {perimeter} meters.")


# Rectangle calculations
length = float(input("Enter the length of the rectangle (in meters): "))
width = float(input("Enter the width of the rectangle (in meters): "))

# Calculating area and perimeter of the rectangle
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

# Displaying rectangle results
print(f"The area of the rectangle is {rectangle_area} square meters.")
print(f"The perimeter of the rectangle is {rectangle_perimeter} meters.")

# Circle calculations
radius = float(input("\nEnter the radius of the circle (in meters): "))
pi = 3.14

# Calculating area and circumference of the circle
circle_area = pi * radius ** 2
circle_circumference = 2 * pi * radius

# Displaying circle results
print(f"The area of the circle is {circle_area} square meters.")
print(f"The circumference of the circle is {circle_circumference} meters.")

# Line equation: y = 2x - 2
slope = 2  # Coefficient of x
x_intercept = -(-2 / 2)  # Solving for x when y = 0
y_intercept = -2  # Constant term when x = 0

# Displaying line properties
print("\nFor the line equation y = 2x - 2:")
print(f"The slope of the line is {slope}.")
print(f"The x-intercept of the line is {x_intercept}.")
print(f"The y-intercept of the line is {y_intercept}.")


import math

# Task 9: Slope and Euclidean distance
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope calculation
slope = (y2 - y1) / (x2 - x1)

# Euclidean distance calculation
euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Slope between points (2, 2) and (6, 10): {slope}")
print(f"Euclidean distance between points (2, 2) and (6, 10): {euclidean_distance}")

# Task 10: Compare slopes
slope_task_8 = 2  # From task 8
print(f"Are slopes equal? {slope == slope_task_8}")

# Task 11: Find value of y
for x in [-3, 0, 3, -6, 6]:
    y = x ** 2 + 6 * x + 9
    print(f"For x = {x}, y = {y}")

# Check when y = 0
print("y will be 0 when x = -3")

# Task 12: Length of 'python' and 'dragon' and falsy comparison
length_python = len('python')
length_dragon = len('dragon')
print(f"Length of 'python': {length_python}, Length of 'dragon': {length_dragon}")
print(f"Falsy comparison: {length_python != length_dragon}")

# Task 13: Use and operator
print(f"Is 'on' found in both 'python' and 'dragon'? {'on' in 'python' and 'on' in 'dragon'}")

# Task 14: Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
print(f"Is 'jargon' in the sentence? {'jargon' in sentence}")

# Task 15: No 'on' in both dragon and python
print(f"There is no 'on' in both dragon and python: {'on' not in 'dragon' and 'on' not in 'python'}")

# Task 16: Length of 'python', convert to float, and then to string
length_python_float = float(len('python'))
length_python_str = str(length_python_float)
print(f"Length of 'python' as float: {length_python_float}, as string: {length_python_str}")

# Task 17: Check if a number is even
number = int(input("Enter a number to check if it's even: "))
is_even = number % 2 == 0
print(f"The number {number} is even: {is_even}")

# Task 18: Check floor division and int conversion
print(f"Is floor division of 7 by 3 equal to int(2.7)? {7 // 3 == int(2.7)}")

# Task 19: Check types of '10' and 10
print(f"Is type of '10' equal to type of 10? {type('10') == type(10)}")

# Task 20: Check if int('9.8') equals 10
try:
    int_value = int('9.8')
except ValueError:
    int_value = None
print(f"Can int('9.8') equal 10? {int_value == 10}")

# Task 21: Calculate pay
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print(f"Total pay is: {pay}")



#Task 22: Script to calculate the number of seconds a person can live
# Assuming a person can live up to 100 years

# Constants
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # 1 year = 365 days

# Prompt user to enter the number of years
years = int(input("Enter the number of years: "))

# Check if the entered years exceed the assumed lifespan
if years > 100:
    print("The number of years exceeds the assumed lifespan of 100 years.")
    years = 100

# Calculate the number of seconds
seconds_lived = years * SECONDS_IN_A_YEAR

# Output the result
print(f"In {years} years, a person can live approximately {seconds_lived:,} seconds.")
