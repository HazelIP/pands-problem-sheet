# This program ask user to input any positive integer and outputs successive values of the below calculation
# At each step calculate the next value by taking the current value
# if the input is even divided by 2, if odd x3 +1
# end program while output = 1
# Author: Ka Ling Ip

# validate input >0
allNum = [] # store the calculations in a list
week4 = int(input("Please enter a positive interger:")) #ask for a positive interger
#if week4 < 0:
    #print ("Please enter a POSITIVE interger:")
#else:
while week4 != 1: # program ends while output =1
    if week4 % 2 == 0: #do this if user input/successive value is an even number
        week4/2
        allNum.append(week4) # put the calculation in the list
    else:
        week4*3+1 #do this if user input is an odd number
        allNum.append(week4) # put the calculation in the list
print(week4, allNum)  