# the program takes a positive floating point number as input
# and output an apporximation of its square root by newton method
# author: Ka Ling Ip

def main():
    #ask user for an positive float point number
    n = float(input("Please enter a positive number: ")) 
    if n>0: #takes in only postive number
        print (sqrt(n))
    else:
        #prompt again if user input a negative number
        n = float(input("Please enter a POSITIVE number: "))
        main()

# newton method square root approximation, ref [6.1]
def sqrt(n): #argument n = user input
    p = 0.01 #precision
    R = n #R is approximation of root
    #program stops when n-(R^2)<precision
    while abs(n-R**2)> p: 
        R= (R + n/R)/2
    return (R)

main()

# ref[6.1]: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo