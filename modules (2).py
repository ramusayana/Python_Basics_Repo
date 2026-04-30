#import java.lang

import greetings

string = 'GreatMinds'

print(greetings.reverse(string))

# modules contains functions and variabless

import datetime

#  modulename(filename) => class name => function name

tdate = datetime.date(2023,8,15)
print("DATE FORMAT:",tdate)

tdate = datetime.date.today()
print("DATE FORMAT:",tdate)

print("Year:", tdate.year)
print("Day:", tdate.day)


print("Weekday:", tdate.weekday())
print("Weekday:", tdate.isoweekday())

# timedelta => diff b/w 2 days

tdate = datetime.date.today()

tdelta = datetime.timedelta(days = 35)
print(tdelta)

print(tdate+tdelta)
print(tdate-tdelta)

# find no of days passed in this year

newyear = datetime.date(2021,1,21)
print("no of days passed:", tdate - newyear)


print("no of days passed:", (tdate - newyear).days)

# date = yyyy/mm/dd

# time =  h/m/s/microsec

mytime = datetime.time(7,23,56,587389)

print(mytime)

print(mytime.hour)
print(mytime.minute)

# python math module

import math 

x = 5.4

print(math.floor(x)) #min integer value
print(math.ceil(x)) # max integer value

print(math.factorial(3)) # 1*2*3
print(math.sqrt(2))
print(math.isqrt(2))

#constant

print(math.pi)
print(math.tau) #2pi
print(math.e)
print(math.nan) # not a number
print(math.inf) #infinity


    


