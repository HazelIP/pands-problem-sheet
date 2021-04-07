# the program reads in a text file and output the number of e's it contains
# it should take in the filename from an argument on the command line
# author: Ka Ling Ip

import sys # to use command line argument ref[7.1]
#file will be taken from argument on command line, filename would be of index 1, as index 0 is program name
filename = sys.argv[1] 
with open (filename, "rt") as f: 
    #use count() to count the occurence of "e" in the file, then store in variable "countE" ref[7.2]
    #note:case sensitive, here assume counting lower case e
    countE = f.read ().count("e") 
print (countE) # print output

# ref[7.1]:https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162
# ref[7.2]:https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/