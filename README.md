# Pands-problem-sheet 2021
---------------------------

## Programing and Scripting 2021 weekly task
## Author: Ka Ling Ip (G00398581)

This README is a summary and explaination to codes of weekly task 

### Week 2 (bmi.py)
This programs is used to calculate Body Mass Index when user input their height in cm and weight in kg. 
#### Actual code
    weight = int (input("Enter weight:"))
    height = int (input("Enter height:"))
    newHeight = (height/100)**2
    BMI = round (weight/(newHeight), 2)
    print("BMI is {}".format(BMI))
#### Explainning the code
1. Ask user for input and define variables and variable types
2. Convert user input "height" from cm to meter and then square it, so it can be applied to the fomular in the next step
3. Apply BMI fomular which is user input "weight" divided by height converted in step 2 
4. Print out BMI
#### List of Reference: 
ref[2.1]: https://en.wikipedia.org/wiki/Body_mass_index
ref[2.2]: https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

### Week 3 (secondString.py)
This program asks a user to input a string and outputs every second letter in reverse order
#### Actual code
    reverse = input ("Please enter a sentence:") [::-2]
    print (reverse)
#### Explainning the code
1. Ask user to input a string
2. Takes in the whole string [::]
3. Output every second letter [::2] (ref[3.1]), 
4. Output in reverse order [::-2] (ref[3.2])
#### List of Reference:
ref[3.1]:https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word 
ref[3.2]:https://www.w3schools.com/python/python_howto_reverse_string.asp

### Week 4 (collatz.py)
This program asks user to input any positive integer and outputs successive values of the below calculation. At each step calculate the next value by taking the current value. If the input is even, divide input by 2, if input is odd,then input x3 +1. Program ends when output = 1. 
#### Actual code
    def main(): 
        numIn = int(input("Please enter a positive integer:")) 
        allNum = [] 
        allNum.append(numIn)
        if numIn > 1: 
            while numIn != 1: 
                if numIn % 2 == 0: 
                    numIn = int(numIn/2)
                    allNum.append(numIn) 
                else:
                    numIn = int(numIn*3+1) 
                    allNum.append(numIn) 
            print (allNum) 
        elif numIn <= 0: 
            main()
        main() 
#### Explainning the code
1. Create a function called main (ref[4.1])
2. Ask user to input a positive integer and the input in "numIn"
3. Create a list to store the calculations
4. Store user input in the list (ref[4.2])
5. Proceed to calculation only when input is a positive integer bigger than 1, otherwise the while loop will not work (ref[4.3]). If user input an integer smaller or equal to 0, prompt again in "elif" session
6. Program will end while output of calculation =1, using while loop (ref[4.4])
7. If user input/successive value is an even number, divide it by 2. Store the output in "allNum"
8. If user input/successive value is an odd number, times it by 3 and plus 1. Store the output in "allNum"
9. Print the list of output when the while loop ends
10. Call the function
#### List of Reference
ref[4.1]: https://www.w3schools.com/python/python_functions.asp 
ref[4.2]: https://www.w3schools.com/python/python_lists_add.asp 
ref[4.3]: https://www.w3schools.com/python/python_conditions.asp 
ref[4.4]: https://www.w3schools.com/python/python_while_loops.asp 

### Week 5 (weekday.py)
This program outputs whether or not today is a weekday
#### Actual code
    import datetime 
    today = datetime.date.today() 
    day_today = today.weekday() 
    if day_today == 5 or day_today == 6: 
        print ("It is weekend, yay!")
    else:
        print ("Yes, unfornately today is a weekday.")
#### Explainning the code
1. Import the datetime module which has a weekday function
2. Get date of today as variable "today" ref[5.1] from w3school # namespace of module
3. Find out what day of the week it is as "day_today", 0=monday, 6=sunday
4. #5,6 are Saturday and Sunday respectively, i.e. print "It is weekend, yay!"
5. #0-4 are Monday to Friday respectively, i.e. print "Yes, unfornately today is a weekday."
#### List of Reference
ref[5.1]: https://www.programiz.com/python-programming/datetime/current-datetime
ref[5.2]: https://www.w3schools.com/python/python_datetime.asp 
ref[5.3]: https://pythontic.com/datetime/datetime/weekday

### week 6 (squareroot.py)
The program takes a positive floating point number as input, and output an apporximation of its square root by newton method. 
#### Actual code
    def main():
        n = float(input("Please enter a positive number: ")) 
        if n>0: 
            print (sqrt(n))
        else:
            #prompt again if user input a negative number
            n = float(input("Please enter a positive number: "))
            main()
    def sqrt(n):
        p = 0.01 
        R = n 
        while abs(n-R**2)> p: 
            R= (R + n/R)/2
        return (R)
    main()

#### Explainning the code
1. Main() asks user for a positive float point number and stored as n, then compute square root approximation
2. Prompt again if user input a negative number
3. sqrt(n) takes in input from user as argument 
4. Define precision as p, R as approximation of root
5. The program stops when difference between n and R squared is close enough to precision
#### List of Reference
ref [6.1]: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo

### week 7 (es.py)
The program reads in a text file and output the number of e's it contains. It should take in the filename from an argument on the command line
#### Actual code
    import sys 
    filename = sys.argv[1] 
    with open (filename, "rt") as f: 
        countE = f.read ().count("e") 
    print (countE) # print output
#### Explainning the code
1. Import sys in order to use command line argument
2. File will be taken from argument on command line, filename would be of index 1, as index 0 is program name.
3. Read the text file
4. Use count() to count the occurence of "e" in the file, then store in variable "countE"
5. note:case sensitive, here assumes counting lower case e
#### List of Reference
ref[7.1]: https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162
ref[7.2]: https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

### Week 8 (plottask.py)
The program displays a plot of the functions, f(x)=x, g(x)=x squared and h(x)=x cubed in the range [0, 4] on the one set of axes.
#### actual code
    import numpy as np
    import matplotlib.pyplot as plt
    f = np.array ([0,1,2,3,4]) 
    g = f * f 
    h = f * f * f 
    plt.plot (f,'r', linewidth = '3', label = 'f(x)') #f(x) in red line
    plt.plot (g,'b', linewidth = '3', label = 'g(x)') #g(x) in blue line
    plt.plot (h,'y', linewidth = '3', label = 'h(x)') #h(x) in yellow line
    plt.title("Functions f(x), g(x), h(x)")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend(loc="upper left")
    plt.show()
#### Explaining the code
1. Import numpy and matplotlib to set f(x) in range [0,4] and create plot
2. Define f as an numpy array in range [0,4]
3. Define g = f squared and h = f cubed
4. Create a plot showing the 3 functions, shown in different colors and with labels
5. Set name of title, x-axis and y-axis, set legend of the plot at upper left corner
6. Show the plot
#### List of Reference
ref[8.1]: https://www.w3schools.com/python/matplotlib_line.asp
ref[8.2]: https://www.w3schools.com/python/matplotlib_labels.asp
