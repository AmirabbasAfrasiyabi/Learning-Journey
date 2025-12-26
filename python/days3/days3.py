"""condition"""

# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")


"""example 1"""
# print("welcome to the rollercoaster!")
# height = int(input("enter your height: "))
# if height >= 120 :
#     print("your height is more than 120")
# else:
#     print("your height is less than 120")


"""example2 -> even or odd number"""
# numbers = int(input())
# if numbers % 2 == 0:
#     print("this is a even number")
# else:
#     print("this is a odd number")


"""example3 -> elif"""
# print("welcome to the rollercoaster!")
# height = int(input("enter your height: "))
#
# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("enter your age: "))
#
#     if age < 12:
#         bill = 5
#         print("Child thicket are 5$")
#
#     elif age <=18:
#         bill = 7
#         print("Youth ticket are 7$")
#
#     else:
#         bill = 12
#         print("Adult ticket are 12$")
#
#     wants_photo = input("Would you like to see the photo? (yes/no): ")
#     if wants_photo == "yes":
#         """Add three dollar too the bill"""
#         bill = bill + 3
#
#     print(f'your final bill is {bill}')
#
# else:
#     print("sorry, you are not enough height to ride the rollercoaster!")


"""Bmi calculation with if """

# height = float(input("height: "))
# weight = float(input("weight: "))
# bmi = round(weight / height ** 2, 2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi} , you are underweight")

# elif 18.5 <= bmi < 25:
#     print(f"Your BMI is {bmi} ,you are normal weight")

# elif 25 <= bmi < 30:
#     print(f"Your BMI is {bmi} ,you are obese weight")

# else:
#     print(f"Your BMI is {bmi} ,you are clinically obese")



"""pizza order program"""
# print("Welcome to python pizza Deliveries")
# size = input("What size of pizza do you want ? S , M , L ")
# add_peperoni = input("Do you want add peperoni? (Y/N)")
# extra_cheese = input("Do you want extra cheese? (Y/N)")
#
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# if add_peperoni == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M":
#         bill += 3
#     else:
#         bill += 4
# if extra_cheese == "Y":
#     if size == "S":
#         bill += 5
#     elif size == "M":
#         bill += 6
#     else:
#         bill += 7
#
# print(f"Your final bill is: {bill}")


"""love calculator exersice"""

# print("welcome to the love calculator")
# name1 = input("what is your name? \n")
# name2 = input("what is your name? \n")
#
# combined_string = name1 + name2
# print(combined_string)
#
# lower_case_string = combined_string.lower()
# print(lower_case_string)
#
# t = lower_case_string.count("t")
# print(t)
#

