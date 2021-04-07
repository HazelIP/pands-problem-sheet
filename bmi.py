# This program calculates BMI
# Author: KA Ling Ip

# Ask for user input, as well as defining variables
weight = int (input("Enter weight:"))
height = int (input("Enter height:"))

# Convert height to metersquare
newHeight = (height/100)**2

# Calculate BMI = kg/meter squared (ref[2.1]) and rounded to 2 decimal places (ref[2.2])
BMI = round (weight/(newHeight), 2)
# Print out results
print("BMI is {}".format(BMI))

# ref[2.1]: https://en.wikipedia.org/wiki/Body_mass_index
# ref[2.2]: https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python