''''# Get the student's score
score = int(input("Enter the student's score: "))

# Determine the grade based on the score
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "Invalid score. Please enter a score between 0 and 100."

# Print the grade
print(f"The grade is: {grade}")'''


''''# Get the month input from the user
month = input("Enter the month: ").strip().capitalize()

# Determine the season based on the month
if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = "Invalid month. Please enter a valid month name."

# Print the season
print(f"The season is: {season}")
'''

''''# Define a dictionary mapping months to seasons
seasons = {
    "September": "Autumn", "October": "Autumn", "November": "Autumn",
    "December": "Winter", "January": "Winter", "February": "Winter",
    "March": "Spring", "April": "Spring", "May": "Spring",
    "June": "Summer", "July": "Summer", "August": "Summer"
}

# Get the month input from the user
month = input("Enter the month: ").strip().capitalize()

# Determine the season using the dictionary
season = seasons.get(month, "Invalid month. Please enter a valid month name.")

# Print the season
print(f"The season is: {season}")'''


