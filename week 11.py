1.Problem Description:

Write a Python program that asks the user for their age and prints a message based on the age. Ensure that the program handles cases where the input is not a valid integer.



Input Format:

A single line input representing the user's age.



Output Format:

Print a message based on the age or an error if the input is invalid.

try:
    a=input()
    if len(a)==0:
        print("Error: Please enter a valid age.")
    elif a.isnumeric():
        print(f"You are {a} years old.")
    else:
        print("Error: Please enter a valid age.")
except:
    print("Error: Please enter a valid age.")

2.Write a Python program that performs division and modulo operations on two numbers provided by the user. Handle division by zero and non-numeric inputs.

Input Format:

Two lines of input, each containing a number.

Output Format:

Print the result of division and modulo operation, or an error message if an exception occurs.
try:
    d=int(input())
    m=int(input())
    dr=d/m
    mr=d%m
    print("Division result:",dr)
    print("Modulo result:",mr)
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except:
    print("Error: Non-numeric input provided.")

3.Problem Description:

Develop a Python program that safely calculates the square root of a number provided by the user. Handle exceptions for negative inputs and non-numeric inputs.

Input Format:

User inputs a number.

Output Format:

Print the square root of the number or an error message if an exception occurs.

import math

try:
    a=float(input())
    if (a<0):
        print("Error: Cannot calculate the square root of a negative number.")
    elif (0<=a):
        b= math.sqrt(a)
        print(f"The square root of {a} is {b:.2f}")

except ValueError:
    print("Error: could not convert string to float")

4.Write a Python program that asks the user for their age and prints a message based on the age. Ensure that the program handles cases where the input is not a valid integer.

Input Format: A single line input representing the user's age.

Output Format: Print a message based on the age or an error if the input is invalid.

try:
    a=input()
    if len(a)==0:
        print("Error: Please enter a valid age.")
    elif a.isnumeric():
        print(f"You are {a} years old.")
    else:
        print("Error: Please enter a valid age.")
except:
    print("Error: Please enter a valid age.")

5.Develop a Python program that safely performs division between two numbers provided by the user. Handle exceptions like division by zero and non-numeric inputs.

Input Format: Two lines of input, each containing a number.

Output Format: Print the result of the division or an error message if an exception occurs.

try:
    a=float(input())
    b=float(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except ValueError:
    print("Error: Non-numeric input provided.")
