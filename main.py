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

# test case for git branch push
# print("test case for git branch push")

# test case for ide vcs
# print("test case for ide vcs")

# case 21 Write a Python Program to Find Armstrong Number in an Interval
"""
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    temp_num = num
    sum = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10

    if num == sum:
        print(num)
"""

# case 22 Write a Python Program to Find the Sum of Natural Numbers.
"""
limit = int(input("Enter the limit: "))
sum = 0

for i in range(1, limit + 1):
    sum += i

print("The sum of natural numbers up to", limit, "is:", sum)
"""

# case 23 Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
"""
dec_num = int(input('Enter a decimal number: '))
print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")
"""

# case 24 Write a Python Program To Find ASCII value of a character.
"""
char = str(input("Enter the character: "))
print("The ASCII value of '" + char + "' is", ord(char))
"""

# case 25 Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.
"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: A number cannot be divided by zero!"
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no):")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
"""

# case 26 Write a Python Program to Display Fibonacci Sequence Using Recursion.
"""
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))

nterms = int(input("Enter the number of terms (greater than 0): "))

if nterms <= 0:
    print("Plese enter a positive integer")

else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
"""

# case 27 Write a Python Program to Find Factorial of Number Using Recursion.
"""
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

num = int(input("Enter the number: "))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
"""

# case 28 Write a Python Program to calculate your Body Mass Index.
"""
def bodymassindex(height, weight):
    return round((weight / height**2),2)

h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))

print("Welcome to the BMI calculator.")

bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
"""

# case 29 Write a Python Program to calculate the natural logarithm of any number.
"""
import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number.")

else:
    result = math.log(num)
    print(f"The natural logarithm of {num} is: {result}")
"""

# case 30 Write a Python Program for cube sum of first n natural numbers?
"""
def cube_sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        total = sum([i ** 3 for i in range(1, n + 1)])
        return total

n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")

else:
    result = cube_sum_of_natural_numbers(n)
    print(f"The cube sum of the first {n} natural numbers is: {result}")
"""

# case 31 Write a Python Program to find sum of array
"""
#  Finding Sum of Array Using sum()
arr = [1,2,3]
ans = sum(arr)
print('Sum of the array is ', ans)

# Function to find the sum of elements in an array
def sum_of_array(arr):
    total = 0

    for element in arr:
        total += element

    return total

array = [1, 2, 3]
result = sum_of_array(array)
print("Sum of the array:", result)
"""

# case 32 Write a Python Program to find largest element in an array.
"""
def find_largest_element(arr):
    if not arr:
        return "Array is empty"

    largest_element = arr[0]

    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element        


my_array = [10, 20, 30, 99]
result = find_largest_element(my_array)
print(f"The largest element in the array is: {result}")
"""

# case 33 Write a Python Program for array rotation.
"""
def rotate_array(arr, d):
    n = len(arr)

    if d < 0 or d >= n:
        return "Invalid rotation value"

    # Create a new array to store the rotated elements.
    rotated_arr = [0] * n

    # Perform the rotation.
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr

#Input array
arr = [1, 2, 3, 4, 5]

# Number of positions to rotate
d = 2

# Call the rotate_array function
result = rotate_array(arr, d)

# Print the rotated array
print("Original Array:", arr)
print("Rotated Array:", result)
"""

# case 34 Write a Python Program to Split the array and add the first part to the end?
"""
def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr

    # Split the array into two parts
    first_part = arr[:k]
    second_part = arr[k:]

    # Add the first part to the end of the second part
    result = second_part + first_part

    return result


arr = [1, 2, 3, 4, 5]
k = 3

result = split_and_add(arr, k)

print("Original Array:", arr)
print("Array after splitting and adding:", result)
"""

# case 35 Write a Python Program to check if given array is Monotonic.
# A monotonic array is one that is entirely non-increasing or non-decreasing.
"""
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing        


arr1 = [1, 2, 2, 3] # Monotonic (non-decreasing)
arr2 = [3, 2, 1]    # Monotonic (non-increasing)
arr3 = [1, 3, 2, 4] # Not monotonic

print("arr1 is monotonic:", is_monotonic(arr1))
print("arr2 is monotonic:", is_monotonic(arr2))
print("arr3 is monotonic:", is_monotonic(arr3))
"""

# case 36 Write a Python Program to Add Two Matrices.
"""
# Function to add two matrices
def add_matrices(mat1, mat2):
        # Check if the matrices have the same dimensions
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            return "Matrices must have the same dimensions for addition"

        # Initialize an empty result matrix with the same dimensions
        result = []

        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[0])):
                row.append(mat1[i][j] + mat2[i][j])
            result.append(row)

        return result

# Input matrices
matrix1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

matrix2 = [
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]

# Call the add_matrices function
result_matrix = add_matrices(matrix1, matrix2)

# Display the result
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Sum of matrices:")
    for row in result_matrix:
        print(row)
"""

# case 37 Write a Python Program to Multiply Two Matrices.
"""
def multiply_matrices(mat1, mat2):
    # Determine the dimensions of the input matrices
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    # Check if multiplication is possible
    if cols1 != rows2:
        return "Matrix multiplication is not possible."

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Display the result
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)
"""

# case 38 Write a Python Program to Transpose a Matrix.
"""
# Function to transpose a matrix
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Create an empty matrix to store the transposed data
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

# Input matrix
matrix = [
 [1, 2, 3],
 [4, 5, 6]
]

# Transpose the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
for row in transposed_matrix:
    print(row)
"""

# case 39 Write a Python Program to Sort Words in Alphabetic Order.
"""
my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.capitalize() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words
print("The sorted words are:")
for word in words:
    print(word)
"""

# case 40 Write a Python Program to Remove Punctuation From a String
"""
# define punctuation
punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''

# To take input from the user
my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct += char

# display the unpunctuated string
print(no_punct)
"""

# case 41 Write a Python program to check if the given number is a Disarium Number.
"""
# A Disarium number is a number that is equal to the sum of its digits each raised to the
# power of its respective position. For example, 89 is a Disarium number because

def is_disarium(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)

    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    # Check if the sum is equal to the original number

    return digit_sum == number

# Input a number from the user
try:
    num = int(input("Enter a number: "))
    # Check if it's a Disarium number
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")

except ValueError:
 print("Invalid input. Please enter a valid number.")
"""

# case 42 Write a Python program to print all disarium numbers between 1 to 100.
"""
def is_disarium(num):
    num_str = str(num)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return num == digit_sum

disarium_numbers = [num for num in range(1, 101) if is_disarium(num)]

print("Disarium numbers between 1 and 100:")

for num in disarium_numbers:
    print(num, end=" | ")
"""

# case 43 Write a Python program to check if the given number is Happy Number.

# Happy Number: A Happy Number is a positive integer that, when you repeatedly replace
# the number by the sum of the squares of its digits and continue the process, eventually
# reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number
# is not a Happy Number.
"""
def is_happy_number(num):
    seen = set()  # To store previously seen numbers

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))

    return num == 1


# Test the function with a number
num = int(input("Enter a number: "))

if is_happy_number(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")
"""

# case 44 Write a Python program to print all happy numbers between 1 and 100.
"""
def is_happy_number(num):
    seen = set()

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))

    return num == 1

happy_numbers = []

for num in range(1, 101):
    if is_happy_number(num):
        happy_numbers.append(num)

print("Happy Numbers between 1 and 100:")
print(happy_numbers)
"""

# case 45 Write a Python program to determine whether the given number is a Harshad Number.
"""
def is_harshad_number(num):
    # Calculate the sum of the digits of the number
    digit_sum = sum(int(i) for i in str(num))

    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0

# Input a number
num = int(input("Enter a number: "))

# Check if it's a Harshad Number
if is_harshad_number(num):
    print(f"{num} is a Harshad Number.")

else:
    print(f"{num} is not a Harshad Number.")
"""

# case 46 Write a Python program to print all pronic numbers between 1 and 100.
"""
def is_pronic_number(num):
    for n in range(1, int(num ** 0.5) + 1):
        if n * (n + 1) == num:
            return True
    return False

print("Pronic numbers between 1 and 100 are:")
for i in range(1, 101):
    if is_pronic_number(i):
        print(i, end=" | ")
"""

# case 47 Write a Python program to find sum of elements in list
"""
# Sample list of numbers
numbers = [10, 20, 30, 40, 50]

# Initialize a variable to store the sum
sum_of_numbers = 0

# Iterate through the list and accumulate the sum
for i in numbers:
    sum_of_numbers += i

# Print the sum
print("Sum of elements in the list:", sum_of_numbers)
"""

# case 48 Write a Python program to Multiply all numbers in the list.
"""
# Sample list of numbers
numbers = [10, 20, 30, 40, 50]

# Initialize a variable to store the product
product_of_numbers = 1

# Iterate through the list and accumulate the product
for i in numbers:
    product_of_numbers *= i

# Print the product
print("Product of elements in the list:", product_of_numbers)
"""

# case 49 Write a Python program to find smallest number in a list.
"""
# Sample list of numbers
numbers = [30, 10, -45, 5, 20]

# Initialize a variable to store the minimum value
minimum = numbers[0]

for i in numbers:
    if i < minimum:
        minimum = i

# Print the minimum value
print("The smallest number in the list is:", minimum)
"""

# case 50 Write a Python program to find largest number in a list.
"""
# Sample list of numbers
numbers = [30, 10, -45, 5, 20]

# Initialize a variable to store the minimum value
minimum = numbers[0]

for i in numbers:
    if i > minimum:
        minimum = i

# Print the minimum value
print("The largest number in the list is:", minimum)
"""



































































