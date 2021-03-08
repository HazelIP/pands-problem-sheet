# This program asks a user to input a string and outputs every second letter in reverse order
# Author: Ka Ling Ip

reverse = input ("Please enter a sentence:") [:: -2] #slicing
print (reverse)

# This part try to print the sentence in reverse order
reverse = input ("Please enter a sentence:") [:: -1]
print (reverse)

# [::2] print every second letter of a string
reverse = input ("Please enter a sentence:") [:: 2]
print (reverse)
