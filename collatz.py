# This program ask user to input any positive integer and outputs successive values of the below calculation
# At each step calculate the next value by taking the current value
# if the input is even divided by 2, if odd x3 +1
# end program while output = 1
# Author: Ka Ling Ip

def main(): #create a function called main (ref[4.1])
    numIn = int(input("Please enter a positive integer:")) #ask for a positive integer
    allNum = [] #create a list to store the calculations
    allNum.append(numIn)# store user input in the list (ref[4.2])
    if numIn > 1: #proceed to calculation only when input is a positive integer (ref[4.3])
        while numIn != 1: # program ends while output =1 (ref[4.4])
            if numIn % 2 == 0: #do the following if user input/successive value is an even number
                numIn = int(numIn/2)
                allNum.append(numIn) # put the calculation in the list
            else:
                numIn = int(numIn*3+1) #do this if user input is an odd number
                allNum.append(numIn) # put the calculation in the list
        print (allNum) #print the list of output
    elif numIn <= 0: #if user input a negative number prompt again
        main()

main() #call the function
    
#ref[4.1]: https://www.w3schools.com/python/python_functions.asp 
#ref[4.2]: https://www.w3schools.com/python/python_lists_add.asp 
#ref[4.3]: https://www.w3schools.com/python/python_conditions.asp 
#ref[4.4]: https://www.w3schools.com/python/python_while_loops.asp 