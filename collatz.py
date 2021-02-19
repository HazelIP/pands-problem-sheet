# This program ask user to input any positive integer and outputs calculation
# if the input is even divided by 2, if odd x3 +1
# end program while output = 1
# Author: Ka Ling Ip

# validate input >0
allNum = []
week4 = int(input("Please enter a positive interger:")) #ask for a positive interger
# program ends while output =1
while week4 != 1:
    if week4 % 2 == 0:
        week4/2
        allNum.append(week4)
    else:
        week4*3+1
        allNum.append(week4)

print(week4 + allNum)