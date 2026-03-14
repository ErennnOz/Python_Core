# case 1
# print("Hello Python")

# case 2 Addition
#num1 = float(input("Enter a number: "))
#num2 = float(input("Enter another number: "))
#sum_result = num1 + num2
#print(f"The sum is: {num1} + {num2} = {sum_result}")

# case 3 Division

#num3 = float(input("Enter a number: "))
#num4 = float(input("Enter another number: "))

#if num4 == 0:
    #print("Error: Division by zero is not allowed.")
#else:
    #print(f"result = {num3} / {num4} = {num3 / num4}")

# case 4 Write a Python program to find the area of a triangle.

#base = int(input("Enter base number: "))
#height = int(input("Enter height: "))
#area = (base * height) * 0.5
#print(f"The area of the triangle is: {area}")

# case 5  swap two variables.

#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter another number: "))
#print(f"Original values: num1 = {num1}, num2 = {num2}")
#tempNum = num2
#num2 = num1
#num1 = tempNum
#print(f"Swapped values: num1 = {num1}, num2 = {num2}")

# case 6 generate a random number.
#import random
#print(f"Random number: {random.randint(1, 100)}")

# case 7 convert kilometers to miles.

#kilometers = float(input("Enter distance in kilometers: "))
#conversion_factor = 0.621371
#miles = kilometers * conversion_factor
#print(f"{kilometers} kilometers is equal to {miles} miles")

# case 8  convert Celsius to Fahrenheit

#celsius = float(input("Enter temperature in Celsius: "))
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# case 9 display calendar.

#import calendar
#year = int(input("Enter year: "))
#month = int(input("Enter month: "))
#cal = calendar.month(year, month)
#print(cal)

# case 10 solve quadratic equation.
#import math
#print("𝑎𝑥 + 𝑏𝑥 + 𝑐 = 0")
#print("a, b and c are real numbers and 𝑎 ≠ 0")
#a = float(input("Enter coefficient a: "))
#b = float(input("Enter coefficient b: "))
#c = float(input("Enter coefficient c: "))
#if a == 0:
#    print("a not undefined.")
#else :
#    discriminant = b ** 2 - 4 * a * c
#   if discriminant > 0:
#       root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#       root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#        print(f"Root 1: {root1}")
#        print(f"Root 2: {root2}")
#    elif discriminant == 0:
#        root = -b / (2 * a)
#       print(f"Root 1: {root}")
#   else:
#       real_part = -b / (2 * a)
#        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
#        print(f"Root 1: {real_part} + {imaginary_part}i")
#        print(f"Root 2: {real_part} - {imaginary_part}i")

# case 11 Write a Python program to swap two variables without temp variable.
""""
a = 5
b = 10
# Swapping without a temporary variable
a , b = b, a
print("After swapping:")
print(f"a = {a}")
print(f"b = {b}")
"""

# case 12 Write a Python Program to Check if a Number is Positive, Negative or Zero.
"""
inputNumber = float(input("Enter a number: "))
if inputNumber > 0:
    print(f"Positive number: {inputNumber}")
elif inputNumber < 0:
    print(f"Negative number: {inputNumber}")
else:
    print(f"Number is Zero: {inputNumber}")
"""

# case 13 Write a Python Program to Check if a Number is Odd or Even.
"""
inputNumber = int(input("Enter a number: "))

if inputNumber % 2 == 0:
    print(f"This is a even number: {inputNumber}")
else:
    print(f"This is a odd number: {inputNumber}")
"""

# case 14 Write a Python Program to Check Leap Year.
"""
inputYear = int(input("Enter a year: "))

if (inputYear % 400 == 0) and (inputYear % 100 == 0):
    print("{0} is a leap year".format(inputYear))

elif (inputYear % 4 ==0) and (inputYear % 100 != 0):
    print("{0} is a leap year".format(inputYear))

else:
 print("{0} is not a leap year".format(inputYear))
"""

# case 15 Write a Python Program to Check Prime Number.
"""
inputNumber = int(input("Enter a number: "))

flag = False

if inputNumber == 1:
    print(f"{inputNumber}, is not a prime number")
elif inputNumber > 1:
    for i in range(2, inputNumber):
        if inputNumber % i == 0:
            flag = True
            break
if flag:
    print(f"{inputNumber}, is not a prime number")
else:
 print(f"{inputNumber}, is a prime number")
 """

# case 16 Write a Python Program to Print all Prime Numbers in an Interval of 1-10
"""
lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break             
        else:
            print(num)
"""

# case 17 Write a Python Program to Find the Factorial of a Number.
"""
num = int(input("Enter a number: "))
factorial = 1

if num <0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'The factorial of {num} is {factorial}')
"""

# case 18 Write a Python Program to Display the multiplication Table.
"""
num = int(input("Display multiplication table of: "))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
"""

# case 19 Write a Python Program to Print the Fibonacci sequence.
"""
numterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if numterms <= 0:
    print("Please enter a positive integer")
elif numterms == 1:
    print("Fibonacci sequence upto",numterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < numterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
"""

# case 20 Write a Python Program to Check Armstrong Number?
"""
num = int(input("Enter a number: "))

# Calculate the number of digits in num
num_str = str(num)
num_digits = len(num_str)

# Initialize variables
sum_of_powers = 0
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10

# Check if it's an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")

else:
    print(f"{num} is not an Armstrong number.")
"""

# test case for git push
#print("test case for git push")























