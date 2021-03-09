# this program outputs whether or not today is a weekday
# author: Ka Ling Ip

# use datetime import

import datetime #import the datetime module which has a weekday function
today = datetime.date.today() #x = datetime.datetime.now() from w3school # namespace of module
day_today = today.weekday() # Find out what day of the week it is
today_nice = today.strftime("%A %d. %B %Y") # show day of the week and date
# print (day_today) #0=monday, 6=sunday
# print ("Today is {}".format(today_nice))  
if day_today == 5 or day_today == 6: #5,6 are sunday and saturday respectively  
    print ("It is weekend, yay!")
else: #0-5 are monday to friday respectively
    print ("Yes, unfornately today is a weekday.")