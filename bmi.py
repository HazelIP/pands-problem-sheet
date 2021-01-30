# This program calculates BMI
# Author: KA Ling Ip

# Ask for user input
weight = int (input("Enter weight:"))
height = int (input("Enter height:"))

# Convert height to metersquare
newHeight = (height/100)**2

# Calculate BMI and rounded to 2 decimal places
# ref: https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
BMI = round (weight/(newHeight), 2)
# Print out results
print("BMI is {}".format(BMI))