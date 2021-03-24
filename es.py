# the program reads in a text file and output the number of e's it contains
# it should take in the filename from an argument on the command line
# es.py mob$ python es.py moby-dick.txty-dick.txt (output 116960)
# author: Ka Ling Ip

import sys # to use command line argument
#file will be taken from argument on command line, filename would be of index 1, as index 0 is program name
filename = sys.argv[1] 

with open (filename, "rt") as f: 
    #use count() to count the occurence of "e" in the file, then store in variable "countE"
    #note:case sensitive, here assume counting lower case e
    countE = f.read ().count("e") 
print (countE) # print output


#https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
#Thus, the first element of the array sys.argv() is the name of the program itself. 
# sys.argv() is an array for command line arguments in Python. 
# To employ this module named “sys” is used. 
# sys.argv is similar to an array and the values are also retrieved like Python array.