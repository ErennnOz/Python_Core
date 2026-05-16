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

# case 51 Write a Python program to find second largest number in a list.
"""
# Sample list of numbers
numbers = [30, 10, 45, 5, 20]

# Sort the list in descending order
numbers.sort(reverse=True)

# Check if there are at least two elements in the list
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")
"""

# case 52 Write a Python program to find N largest elements from a list
"""
# Sample list of numbers
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

def find_n_largest_elements(lst, n):
    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)

    # Get the first N elements
    largest_elements = sorted_lst[:n]

    return largest_elements


# Number of largest elements to find
N = int(input("N = " ))

# Find the N largest elements from the list
result = find_n_largest_elements(numbers, N)

# Print the N largest elements
print(f"The {N} largest elements in the list are:", result)
"""

# case 53 Write a Python program to print even numbers in a list.
"""
# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a list comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Print the even numbers
print("Even numbers in the list:", even_numbers)
"""

# case 54 Write a Python program to print odd numbers in a List.
"""
# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a list comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 != 0]

# Print the even numbers
print("Odd numbers in the list:", even_numbers)
"""

# case 55 Write a Python program to Remove empty List from List.
"""
# Sample list containing lists
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

# Using a list comprehension to remove empty lists
filtered_list = [i for i in list_of_lists if i]

# Print the filtered list
print("List after removing empty lists:", filtered_list)
"""

# case 56 Write a Python program to Cloning or Copying a list.
"""
# 1. Using Using the Slice Operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)

# 2. Using the list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print(cloned_list)

# # 3. Using List Comprehension
original_list = [1, 2, 3, 4, 5]
cloned_list = [item for item in original_list]
print(cloned_list)
"""

# case 57 Write a Python program to Count occurrences of an element in a list
"""
def count_occurrences(l, element):
    count = l.count(element)
    return count

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = 2

occurrences = count_occurrences(my_list, element_to_count)
print(f"the element {element_to_count} appears {occurrences} times in the list")
"""

# case 58 Write a Python program to find words which are greater than given length k.
"""
def find_words(words, k):
    # Create an empty list to store words greater than k
    result = []
    # Iterate through each word in the list
    for i in words:
        if len(i) > k:
            result.append(i)

    return result


# Example usage
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragonfruit"]
k = 5
long_words = find_words(word_list, k)

print(f"Words longer than {k} characters: {long_words}")
"""

# case 59 Write a Python program for removing 𝑖-th character from a string.
"""
def remove_char(input_str, i):
    # Check if i is a valid index
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
    # Remove the i-th character using slicing
    result_str = input_str[:i] + input_str[i + 1:]

    return result_str

# Input string
input_str = "Hello, wWorld!"

# Index of the character to remove
i = 7
# Remove the i-th character
new_str = remove_char(input_str, i)

print(f"Original String: {input_str}")
print(f"String after removing {i}th character : {new_str}")
"""

# case 60 Write a Python program to split and join a string.
"""
# Split a string into a list of words
input_str = "Python program to split and join a string"
word_list = input_str.split() # By default, split on whitespace

# Join the list of words into a string
separator = " "
output_str = separator.join(word_list)

# Print the results
print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)
"""

# case 61 Write a Python program to check if a given string is binary string or not
"""
def is_binary_str(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True


# Input string to check
input_str = "1001110"

# Check if the input string is a binary string
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")
"""
# case 62 Write a Python program to find uncommon words from two Strings.
"""
def uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())

    # Find uncommon words by taking the set difference
    uncommon_words_set = words1.symmetric_difference(words2)

    # Convert the set of uncommon words back to a list
    uncommon_words_list = list(uncommon_words_set)

    return uncommon_words_list


# Input two strings
string1 = "This is the first string"
string2 = "This is the second string"

# Find uncommon words between the two strings
uncommon = uncommon_words(string1, string2)

# Print the uncommon words
print("Uncommon words:", uncommon)
"""

# case 63 Write a Python program to find all duplicate characters in string
"""
def find_duplicates(input_str):
    # Create an empty dictionary to store character counts
    char_count = {}

    # Initialize a list to store duplicate characters
    duplicates = []

    # Iterate through each character in the input string
    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    # Iterate through the dictionary and add characters with count > 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)

    return duplicates

# Input a string
input_string = "EREN ÖZDEMİR"

# Find duplicate characters in the string
duplicate_chars = find_duplicates(input_string)

# Print the list of duplicate characters
print("Duplicate characters:", duplicate_chars)
"""

# case 64 Write a Python Program to check if a string contains any special character.
"""
import re

def check_special_char(in_str):
    # Define a regular expression pattern to match special characters
    pattern = r'[!@#$%^&*()_+{}[\]:;<>,.?~\\/\'"-=]'

    # Use re.search to find a match in the input string
    if re.search(pattern, in_str):
        return True
    else:
        return False


# Input a string
input_string = str(input("Enter a string: "))

# Check if the string contains any special characters
contains_special = check_special_char(input_string)

# Print the result
if contains_special:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
"""

# case 65 Write a Python program to Extract Unique dictionary values.
"""
# Sample dictionary
my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}

# Initialize an empty set to store unique values
uni_val = set()

# Iterate through the values of the dictionary
for i in my_dict.values():
    # Add each value to the set
    uni_val.add(i)

# Convert the set of unique values back to a list (if needed)
unique_values_list = list(uni_val)

# Print the unique value
print("Unique values in the dictionary:", unique_values_list)
"""

# case 66 Write a Python program to find the sum of all items in a dictionary.
"""
# Sample dictionary
my_dict = {
 'a': 10,
 'b': 20,
 'c': 30,
 'd': 40,
 'e': 50
}

# Initialize a variable to store the sum
total_sum = 0

# Iterate through the values of the dictionary and add them to the total
for i in my_dict.values():
    total_sum += i

# Print the sum of all items in the dictionary
print("Sum of all items in the dictionary:", total_sum)
"""

# case 67 Write a Python program to Merging two Dictionaries.
"""
# 1. Using the update() method:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

# The merged dictionary is now in dict1
print("Merged Dictionary (using update()):", dict1)

# 2. Using dictionary unpacking

# Merge dict2 into dict1 using dictionary unpacking
merged_dict = {**dict1, **dict2}

# The merged dictionary is now in merged_dict
print("Merged Dictionary (using dictionary unpacking):", merged_dict)
"""

# case 68 Write a Python program to convert key-values list to flat dictionary
"""
key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Initialize an empty dictionary
flat_dict = {}

# Iterate through the list and add key-value pairs to the dictionary
for key, value in key_values_list:
    flat_dict[key] = value

# Print the resulting flat dictionary
print("Flat Dictionary:", flat_dict)
"""

# case 69 Write a Python program to insertion at the beginning in OrderedDict.
"""
from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])

# Item to insert at the beginning
new_item = ('a', 1)

# Create a new OrderedDict with the new item as the first element
new_ordered_dict = OrderedDict([new_item])

# Merge the new OrderedDict with the original OrderedDict
new_ordered_dict.update(ordered_dict)

# Print the updated OrderedDict
print("Updated OrderedDict:", new_ordered_dict)
"""

# case 70 Write a Python program to check order of character in string using OrderedDict().
"""
from collections import OrderedDict

def check_order(string, reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)

    return string_dict == reference_dict

input_string = "hello world"
reference_string = "helo wrd"

if check_order(input_string, reference_string):
    print("The order of characters in the input string matches")
else:
    print("The order of characters in the input string does not match")
"""

# case 71 Write a Python program to sort Python Dictionaries by Key or Value
"""
# Sort by Keys:
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

sorted_dict_by_keys = dict(sorted(sample_dict.items()))

print("Sorted by keys:")

for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")

# Sort by values
sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
    print(f"{key}: {value}")
"""
# case 72 Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
"""
# Accept input from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Split the input into a list of words
words = input_sequence.split(',')

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words into a comma-separated sequence
sorted_sequence = ','.join(sorted_words)

# Print the sorted sequence
print("Sorted words:", sorted_sequence)
"""

# case 73 Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them
# alphanumerically.
"""
# Accept input from the user
input_sequence = input("Enter a sequence of whitespace-separated words: ")

# Split the input into words and convert it into a set to remove duplicate
words = set(input_sequence.split())

# Sort the unique words alphanumerically
sorted_words = sorted(words)

# Join the sorted words into a string with whitespace separation
result = ' '.join(sorted_words)

# Print the result
print("Result:", result)
"""

# case 74 Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program:
"""
# Accept input from the user
sentence = input("Enter a sentence: ")

# Initialize counters for letters and digits
letter_count = 0
digit_count = 0

# Iterate through each character in the sentence
for char in sentence:
    if char.isalpha():
        letter_count += 1
    if char.isdigit():
        digit_count += 1

# Print the results
print("LETTERS", letter_count)
print("DIGITS", digit_count)
"""

# case 75 A website requires the users to input username and password to register. Write a
# program to check the validity of password input by users. Following are the criteria
# for checking the password:
"""
import re

def is_valid_password(password):
    # 1. Şifre uzunluğu 6 ile 12 karakter arasında olmalı
    if 6 <= len(password) <= 12:
        # 2. Regex ile kriterleri kontrol et:
        # (?=.*[a-z]) -> En az bir küçük harf
        # (?=.*[A-Z]) -> En az bir büyük harf
        # (?=.*[0-9]) -> En az bir rakam
        # (?=.*[$#@]) -> En az bir özel karakter ($ veya # veya @)
        # .* -> Tüm bu şartlardan sonra karakterlerin devam edebileceğini belirtir
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).*$"

        if re.match(pattern, password):
            return True
    return False


# Kullanıcıdan virgülle ayrılmış şifreleri al
user_input = input("Şifreleri virgülle ayırarak girin: ")
passwords = user_input.split(',')

valid_passwords = []

# Her bir şifreyi kontrol et (strip() ile gereksiz boşlukları temizliyoruz)
for psw in passwords:
    clean_psw = psw.strip()
    if is_valid_password(clean_psw):
        valid_passwords.append(clean_psw)

# Geçerli şifreleri virgülle birleştirerek yazdır
print(",".join(valid_passwords))
"""
# case 76 Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.
"""
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        # 0'dan n'e kadar 7'şer atlayarak gitmek daha verimlidir
        for num in range(0, self.n + 1, 7):
            yield num

try:
    n = int(input("Lütfen bir sayı girin: "))
    # Class'ı başlat ve generator'ı al
    generator = DivisibleBySeven(n).generate_divisible_by_seven()

    print(f"0 ile {n} arasındaki 7'ye bölünen sayılar:")
    for num in generator:
        print(num)
except ValueError:
    print("Lütfen sadece tam sayı giriniz.")
"""

# case 77 Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically. Suppose the following input is
# supplied to the program:
"""
input_sentence = input("Enter a sentence: ")

# Split the sentence into words
words = input_sentence.split()

# Create a dictionary to store word frequencies
word_freq = {}

# Count word frequencies
for word in words:
    # Remove punctuation (., ?) from the word
    word = word.strip('.,?')
    # Convert to lowercase to ensure 'Apple' and 'apple' are counted as the same word
    word = word.lower()
    # Update the word frequency in the dictionary
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the words alphanumerically
sorted_words = sorted(word_freq.items())

# Print the word frequencies
for word, frequency in sorted_words:
    print(f"{word}:{frequency}")
"""

# case 78 Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female
# class.
"""
class Person:
    def getGender(self):
         return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

person = Person()
male = Male()
female = Female()

print(person.getGender())
print(male.getGender())
print(female.getGender())
"""

# case 79 Please write a program to generate all sentences where subject is in ["I", "You"] and
# verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentences = []

for sub in subjects:
    for vrb in verbs:
        for obj in objects:
            sentence = f"{sub} {vrb} {obj}."
            sentences.append(sentence)

for sentence in sentences:
    print(sentence)
"""

# case 80 Please write a program to compress and decompress the string "hello world!hello
# world!hello world!hello world!".
"""
import zlib

string = "hello world!hello world!hello world!hello world!"

# Compress the string
compressed_string = zlib.compress(string.encode())

# Decompress the string
decompressed_string = zlib.decompress(compressed_string).decode()

print("Original String:", string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)
"""

# case 81 Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list.
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1 # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half

    return -1 # Element not found in the list


# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 4

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")
"""
# case 82 Please write a program using generator to print the numbers which can be divisible
# by 5 and 7 between 0 and n in comma separated form while n is input by console.
"""
def divisible_by_5_and_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

try:
    n = int(input("Enter a value for n: "))
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
"""
# case 83 Please write a program using generator to print the even numbers between 0 and n in
# comma separated form while n is input by console.
"""
def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num


try:
    n = int(input("Enter a value for n: "))
    result = even_numbers(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
"""

# case 84 please write program to print the username of a given email address.
"""
def extract_username(email):
    # Split the email address at '@' to separate the username and domain
    parts = email.split('@')

    # Check if the email address has the expected format
    if len(parts) == 2:
        return parts[0] # The username is the first part
    else:
        return "Invalid email format"

try:
    email = input("Enter an email address: ")
    username = extract_username(email)
    print(username)
except ValueError:
    print("Invalid input. Please enter a valid email address.")
"""

# case 85 Define a class named Shape and its subclass Square. The Square class has an init
# function which takes a length as argument. Both classes have an area function which
# can print the area of the shape where Shape's area is 0 by default.
"""
class Shape:
    def __init__(self):
        pass # Default constructor, no need to initialize anything

    def area(self):
        return 0 # Shape's area is 0 by default

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length # Call the constructor of the parent class

    def area(self):
        return self.length ** 2 # Calculate the area of the square

# Create instances of the classes
shape = Shape()
square = Square(float(input("Enter the shape of the square: ")))

# Calculate and print the areas
print("Shape's area by default:", shape.area())
print("Area of the square:", square.area())
"""

# case 86 Write a function that stutters a word as if someone is struggling to read it. The first
# two letters are repeated twice with an ellipsis ... and space after each, and then the
# word is pronounced with a question mark ?.
"""
def stutter(word):
    if len(word) < 2:
        return "Word must be at least two characters long."
    stuttered_word = f"{word[:2]}... {word[:2]}... {word}?"
    return stuttered_word

# Test cases
print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))
"""

# case 87 Create a function that takes an angle in radians and returns the corresponding angle
# in degrees rounded to one decimal place.
"""
import math

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)

# Test cases
print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))
"""

# case 88 In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2
# elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a
# Curzon number.
# Given a non-negative integer num, implement a function that returns True if num is a
# Curzon number, or False otherwise.
"""
def is_curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0

# Test cases
print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))
"""

# case 89 Given the side length x find the area of a hexagon.
"""
import math

def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x ** 2) / 2
    return round(area, 1)


#Example usage:
print(area_of_hexagon(1))
print(area_of_hexagon(2))
print(area_of_hexagon(3))
"""

# case 90 This function converts a base-10 (decimal) number, given as a string, into its base-2 (binary) representation.
"""
def binary(decimal):
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str += str(remainder) + binary_str
        decimal = decimal // 2
    return binary_str if binary_str else "0"


print(binary(1))
print(binary(5))
print(binary(10))
"""

# case 91 Create a function that takes three arguments a, b, c and returns the sum of the
# numbers that are evenly divided by c from the range a, b inclusive.
"""
def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b + 1):
        if num % c == 0:
            total += num
    return total

print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))
"""

# case 92 Create a function that returns True if a given inequality expression is correct and
# False otherwise.
"""
def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return False

print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 < 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))
"""

# case 93 Create a function that replaces all the vowels in a string with a specified character.
"""
def replace_vowels(string, char):
    vowels = "AEIOUaeiou"  # List of vowels to be replaced
    for vowel in vowels:
        string = string.replace(vowel, char)
    return string

print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))
"""

# case 94 Write a function that calculates the factorial of a number recursively.
"""
def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))
"""

# case 95 Hamming distance is the number of characters that differ between two strings
"""
def hamming_distance(str1, str2):
    # Check if the strings have the same length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")
    # Initialize a counter to keep track of differences
    distance = 0
    # Iterate through the characters of both strings
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1 # Increment the counter for differences

    return distance

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
"""

# case 96 Create a function that takes a list of non-negative integers and strings and return a
# new list without the strings.
"""
def filter_list(lst):
    # Initialize an empty list to store non-string elements
    result = []

    # Iterate through the elements in the input list
    for element in lst:
        # Check if the element is a non-negative integer (not a string)
        if isinstance(element, int) and element >= 0:
            result.append(element)

    return result

print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
"""

# case 97 The "Reverser" takes a string as input and returns that string in reverse order, with
# the opposite case.
"""
def reverse(input_str):
    # Reverse the string and swap the case of characters
    reversed_str = input_str[::-1].swapcase()
    return reversed_str

print(reverse("Hello World"))
print(reverse("ReVeRsE"))
print(reverse("Radar"))
"""

# case 98 Write a function that moves all elements of one type to the end of the list.
"""
def move_to_end(lst, element):
    # Initialize a count for the specified element
    count = lst.count(element)

    # Remove all occurrences of the element from the list
    lst = [x for x in lst if x != element]

    # Append the element to the end of the list count times
    lst.extend([element] * count)

    return lst

print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))
"""

# case 99 Create a function that takes a string and returns a string in which each character is
# repeated once.
"""
def double_char(input_str):
    doubled_str = ""
    for char in input_str:
        doubled_str += char * 2

    return doubled_str

print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234!_ "))
"""

# case 100 Create a function that reverses a boolean value and returns the string "boolean
# expected" if another variable type is given.
"""
def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"

print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))
"""

# case 101 Create a function that returns the thickness (in meters) of a piece of paper after
# folding it n number of times. The paper starts off with a thickness of 0.5mm.
"""
def num_layers(n):
    initial_thickness_mm = 0.5  # Initial thickness in millimeters
    final_thickness_mm = initial_thickness_mm * (2 ** n)
    final_thickness_m = final_thickness_mm / 1000
    return f"{final_thickness_m:.3f}m"

print(num_layers(1))
print(num_layers(4))
print(num_layers(21))
"""

# case 102 Create a function that takes a single string as argument and returns an ordered list
# containing the indices of all capital letters in the string.
"""
def index_of_caps(word):
    # Use list comprehension to find indices of capital letters
    return [i for i, char in enumerate(word) if char.isupper()]

print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))
"""

# case 103 Using list comprehensions, create a function that finds all even numbers from 1 to
# the given number.
"""
def find_even_nums(num):
    # Use a list comprehension to generate even numbers from 1 to num
    return [x for x in range(1, num + 1) if x % 2 == 0]

print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))
"""

# case 104 Create a function that takes a list of strings and integers, and filters out the list so
# that it returns a list of integers only.
"""
def filter_list(lst):
    # Use a list comprehension to filter out integers
    return [x for x in lst if isinstance(x, int)]

print(filter_list([1, 2, 3, "a", "b", 4]))
print(filter_list(["A", 0, "Edabit", 1729, "Python", 1729]))
print(filter_list(["Nothing", "here"]))
"""

# case 105 Given a list of numbers, create a function which returns the list but with each
# element's index in the list added to itself
"""
def add_indexes(lst):
    # Use list comprehension to add index to each element
    return [i + val for i, val in enumerate(lst)]

print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))
"""

# case 106 Create a function that takes the height and radius of a cone as arguments and returns
# the volume of the cone rounded to the nearest hundredth.
"""
import math

def cone_volume(height, radius):
    if radius == 0:
        return 0
    volume = (1 / 3) * math.pi * (radius ** 2) * height
    return round(volume, 2)

print(cone_volume(3, 2))
print(cone_volume(15, 6))
print(cone_volume(18, 0))
"""

# case 107 Create a function that takes a list of numbers between 1 and 10 (excluding one
# number) and returns the missing number.
"""
def missing_num(lst):
    total_sum = sum(range(1, 11)) # Sum of numbers from 1 to 10
    given_sum = sum(lst) # Sum of the given list of numbers
    missing = total_sum - given_sum
    return missing

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))
"""

# case 108 Write a function that takes a list and a number as arguments. Add the number to the
# end of the list, then remove the first element of the list. The function should then
# return the updated list.
"""
def next_in_line(lst, num):
    if lst:
        lst.pop(0)  # Remove the first element
        lst.append(num) # Add the number to the end
        return lst
    else:
        return "No list has been selected"

print(next_in_line([5, 6, 7, 8, 9], 1) )
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42 ], 6))
print(next_in_line([], 6))
"""

# case 109 Create the function that takes a list of dictionaries and returns the sum of people's
# budgets.
"""
def get_budgets(lst):
    total_budget = sum(person['budget'] for person in lst)
    return total_budget

# Test cases
budgets1 = [
    {'name': 'John', 'age': 21, 'budget': 23000},
    {'name': 'Steve', 'age': 32, 'budget': 40000},
    {'name': 'Martin', 'age': 16, 'budget': 2700}
]

budgets2 = [
    {'name': 'John', 'age': 21, 'budget': 29000},
    {'name': 'Steve', 'age': 32, 'budget': 32000},
    {'name': 'Martin', 'age': 16, 'budget': 1600}
]

print(get_budgets(budgets1))
print(get_budgets(budgets2))
"""

# case 110 Create a function that takes a string and returns a string with its letters in
# alphabetical order.
"""
def alphabet_soup(txt):
    return ''.join(sorted(txt))

print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))
print(alphabet_soup("hacker"))
print(alphabet_soup("geek"))
print(alphabet_soup("javascript"))
"""

# case 111 Write a function that takes a list of elements and returns only the integers
"""
def return_only_integer(lst):
    # Use list comprehension to filter out integers
    return [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]


print(return_only_integer([9, 2, "space", "car", "lion", 16]))
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
print(return_only_integer(["String", True, 3.3, 1]))
"""

# case 112 Create a function that takes three parameters where:
# - x is the start of the range (inclusive).
# - y is the end of the range (inclusive).
# - n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third
# parameter n.
"""
def list_operation(x, y, n):
    # Use list comprehension to generate the list of numbers divisible
    return [num for num in range(x, y + 1) if num % n == 0]

print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7))
"""

# case 113 Create a function that takes in two lists and returns True if the second list follows the
# first list by one element, and False otherwise. In other words, determine if the second
# list is the first list shifted to the right by 1.
"""
def simon_says(list1, list2):
    return list1[:-1] == list2[1:]

print(simon_says([1, 2], [5, 1]))
print(simon_says([1, 2], [5, 5]))
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))
"""

# case 114 An isogram is a word that has no duplicate letters. Create a function that takes a
# string and returns either True or False depending on whether or not it's an "isogram".
"""
def is_isogram(word):
    word = word.lower()

    # Create a set to store unique letters in the word
    unique_letters = set()

    for letter in word:
        # If the letter is already in the set, it's not an isogram
        if letter in unique_letters:
            return False
        unique_letters.add(letter)

    return True

print(is_isogram("Algorism"))
print(is_isogram("PasSword"))
print(is_isogram("Consecutive"))
"""

# case 115 Create a function that takes a string and returns True or False, depending on whether
# the characters are in order or not.
"""
def is_in_order(s):
    return s == ''.join(sorted(s))

print(is_in_order("abc"))
print(is_in_order("edabit"))
print(is_in_order("123"))
print(is_in_order("xyzz"))
"""


# case 116 Create a function that takes a number as an argument and returns True or False
# depending on whether the number is symmetrical or not. A number is symmetrical
# when it is the same as its reverse.
"""
def is_symmetrical(num):
    # Convert the number to a string
    num_str = str(num)

    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

print(is_symmetrical(7227))
print(is_symmetrical(12567))
print(is_symmetrical(44444444))
print(is_symmetrical(44444444))
print(is_symmetrical(1112111))
"""

# case 117 A group of friends have decided to start a secret society. The name will be the first
# letter of each of their names, sorted in alphabetical order. Create a function that takes
# in a list of names and returns the name of the secret society.
"""
def society_name(names):
    secret_name = ''.join(sorted([name[0] for name in names]))
    return secret_name


print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
"""

# case 118 Given a string of numbers separated by a comma and space, return the product of
# the numbers.
"""
def multiply_nums(nums_str):
    # Split the input string by comma and space, then convert to integer
    nums = [int(num) for num in nums_str.split(", ")]

    # Initialize the result with 1
    result = 1

    # Multiply all the numbers together
    for num in nums:
        result *= num

    return result

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))
"""

# case 119 Create a function that squares every digit of a number.
"""
def square_digits(n):
    # Convert the number to a string to iterate through its digits
    num_str = str(n)

    # Initialize an empty string to store the squared digits
    result_str = ""

    # Iterate through the digits
    for digit in num_str:
        # Square the digit and convert it back to an integer
        squared_digit = int(digit) ** 2

        # Append the squared digit to the result string
        result_str += str(squared_digit)

    return int(result_str)

print(square_digits(9119))
print(square_digits(2483))
print(square_digits(3212))
"""

# case 120 Create a function that sorts a list and removes all duplicate items from it.
"""
def setify(lst):
    unique_set = set(sorted(lst))
    # Convert the set back to a list and return it
    return list(unique_set)

print(setify([1, 3, 3, 5, 5]))
print(setify([4, 4, 4, 4]))
print(setify([5, 7, 8, 9, 10, 15]))
print(setify([3, 3, 3, 2, 1]))
"""


















































