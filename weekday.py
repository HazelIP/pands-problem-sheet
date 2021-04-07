# this program outputs whether or not today is a weekday
# author: Ka Ling Ip

# import the datetime module which has a weekday function
import datetime 
today = datetime.date.today() #Find out date of today ref[5.1]
day_today = today.weekday() # Find out what day of the week it is
# The following shows day of the week and date for checking purpose
# today_nice = today.strftime("%A %d %B %Y") ref[5.2]
# print (day_today) #0=monday, 6=sunday
# print ("Today is {}".format(today_nice))  
if day_today == 5 or day_today == 6: #5,6 are sunday and saturday respectively ref[5.3] 
    print ("It is weekend, yay!")
else: #0-5 are monday to friday respectively ref[5.3]
    print ("Yes, unfornately today is a weekday.")

# ref[5.1]: https://www.programiz.com/python-programming/datetime/current-datetime
# ref[5.2]: https://www.w3schools.com/python/python_datetime.asp 
# ref[5.3]: https://pythontic.com/datetime/datetime/weekday