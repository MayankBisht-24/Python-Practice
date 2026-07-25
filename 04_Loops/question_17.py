"""
Question 17

Title:
Find the Least Common Multiple (LCM)

Problem Statement:
Write a Python program to find the LCM of two numbers.

Expected Output:
Enter first number: 6
Enter second number: 8

LCM = 24

Difficulty:
Intermediate

Concepts:
- while loop
- Arithmetic Operators
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest = max(num1, num2)

while True:
    if largest % num1 == 0 and largest % num2 == 0:
        print("LCM =", largest)
        break
    largest += 1