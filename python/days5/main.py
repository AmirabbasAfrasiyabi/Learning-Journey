"""Average Height Exersice"""
import string

# student_height = input('Input a l ist of student height: ').split()
# for i in range(0 , len(student_height)):
#     student_height[i] = int(student_height[i])
# print(student_height)

"""or"""
"""ather solution for sum """
# total_height = 0
# for height in student_height:
#     total_height += height
# print(total_height)

"""or"""
"""other solution for len function"""
# number_of_students= 0
# for student in student_height:
#     number_of_students += 1
# print(number_of_students)
# average_height = round(total_height / number_of_students)
# print(average_height)


"""example2"""
# student_course = input("Input a list of Student Courses").split()
# for n in range(0 , len(student_course)):
#     student_course[n] = int(student_course[n])
# print(student_course)

# print(max(student_course))
"""other solution for max function"""
# height_score = 0
# for score in student_course:
#     if score > height_score:
#         height_score = score
# print(f'the height score in a class is: {height_score}')


"""example3 |-> Adding Evens"""

# total = 0
# for number in range(2,101,2):
#     print(number)
#     total += number
# print(total)
#
# total2 = 0
# for number in range(1,101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

"""password generator"""
print("How many letters would you like in your password?")
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z' 
            ,'A','B','C','D','E','F','G','H','I','J','K','L','M', 
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

number = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' ,'9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+' ,'@' ,'^']

print("welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))

"""Easy level"""
# password = ""
#
# """nr_letters = 4"""
# for char in range(1,nr_letters+1):
#     password += random.choice(letters)
#
# for char in range(1,nr_symbols+1):
#     password += random.choice(symbols)
#
# for char in range(1,nr_numbers+1):
#     password += random.choice(number)
#
# print(password)

"""Hard level"""
password= []
for char in range(1,nr_letters+1):
    password.append(random.choice(letters))

for char in range(1,nr_symbols+1):
    password.append(random.choice(symbols))

for char in range(1,nr_numbers+1):
    password.append(random.choice(number))

print(password)
random.shuffle(password)
print(password)


