"""Data types"""


#string
# print(len('Hello'))
# print("Hello"[2])

#Integer
# print(123+456)

#Float
# print(3.14)

#Boolean
# print(bool(True))
# print(bool(False))



"""len"""
# num_char = len(input("whats your name?"))
# print(f"Your name is {num_char} characters long.")
# print(type(num_char))
# print(num_char)



"""math with python"""
# print(3+7)
# print(7-3)
# print(7**3)
# print(7//3)
# print(7%3)
# print(7/3)
# print(7*3)
# print(((3*3)+(3/3))-3)
# print(type(5*3))


"""BMI calculater code exersice"""
# height = int(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
#
# bmi = int(weight) / float(height)**2
# bmi_as_integer = int(bmi)
# if bmi_as_integer < 18.5:
#     print("you are under weight")
# if 18.5 <= bmi_as_integer <= 25:
#     print("you are over weight")
# if 25 <= bmi_as_integer <= 30:
#     print("you are over height")
# if bmi_as_integer >= 30:
#     print("you are under height")
# print(bmi_as_integer)

"""calculate years"""
# age = int(input("Enter your age: "))
# years_remaining = 90 - age
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
#
# print(f"your age is {age} years old and {years_remaining} years remaining and {days_remaining} days remaining and {weeks_remaining} weeks remaining and {months_remaining} months. and {years_remaining} years remaining.")
#

"""project"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
# print(type(bill))
tip = int(input("How much tip would you like to give? 10 , 12 or 15?"))
people = float(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_percent = total_bill / people
rounded = round(bill_per_percent, 2)
print(f"Each person should pay: ${rounded}")



