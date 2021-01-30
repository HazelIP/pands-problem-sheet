# This program calculates BMI
# Author: KA Ling Ip

# Ask for user input
weight = int (input("Enter weight:"))
height = int (input("Enter height:"))

# Convert height to metersquare
newHeight = (height/100)**2

# Calculate BMI and rounded to 2 decimal places
BMI = round (weight/(newHeight), 2)
# Print out results
print("BMI is {}".format(BMI))