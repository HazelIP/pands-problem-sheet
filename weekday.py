# this program out whether or not today is a weekday
# author: Ka Ling Ip

# use datetime import
# input of today as "date"
import datetime #import the built-in module which has a weekday function
# weekday()
today = datetime.date(input("enter a date (in 'yyyy.mm.dd' format): "))
# weekdays as a tuple
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# Find out what day of the week it is
#day_today = datetime.date(today)

day_today = today.weekday()

day_todayAsString = weekDays[day_today]
if weekday: #0-4 are monday to friday
    print ("Yes, unfornately today is a weekday.")
else: #5,6 are weekend
    print ("It is weekend, yay!")


# ask for an input of date in specified format
# change the input in 0-6 day datetime format (function)
# if 0-4 print weekday
# else print weekend 