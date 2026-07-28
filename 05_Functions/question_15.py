"""
Question 15

Title:
Return the Factorial of a Number

Problem Statement:
Write a Python function that returns the factorial of a given number.

Expected Output:
Enter a number: 5

Factorial = 120

Difficulty:
Intermediate

Concepts:
- return
- for loop
"""

# Solution starts here

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

num = int(input("Enter a number: "))

print("Factorial =", factorial(num))