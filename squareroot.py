# the program takes a positive floating point number as input
# output an apporximation of its square root by newton method
# create a function called "sqrt"
# author: Ka Ling Ip

inputNum= float(input("Please enter a postive number: ")) #ask user for an input
precision = float (input("Please enter the precision, default 0.01"))
def sqrt(n,p = 0.0): #takes 2 parameters, input and precision
    n = inputNum #newton method, ref: 
    p = precision
    R = 1
    for R > p: #sqrt precision, program stops when R<precision
        R= (p + n/p)/2
    
    R = sqrt
    return sqrt

print (150,0.001)