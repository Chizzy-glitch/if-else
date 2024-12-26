any = int(input("Enter the number to be checked"))
if any %2==0:
    print("This is an even number")
else:
    print("This is an odd number")

#BMI Calculator
height = float(input("Enter the height"))
weight = float(input("Enter the weight"))

BMI = weight/(height/100)**2

if BMI <= 18.9:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are Healthy")
elif BMI <= 29.9:
    print("You are overweight")
else:
    print("You are obese")

#Double Check Number
num = int(input("Enter the number to be checked"))
if num >= 50:
    print("The number is greater than 50")
    if num %2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("number is less than 50")

#Datetime and Calendar Module
import datetime 
currenttime = datetime.datetime.now()
print(currenttime)

import calendar
print(calendar.calendar(2011))