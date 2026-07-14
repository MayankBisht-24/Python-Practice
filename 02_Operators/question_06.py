"""
Question 06

Title:
Find the Quotient using Floor Division

Problem Statement:
Write a Python program to take two integers as input and print the floor division result.

Expected Output:
Enter first number: 17
Enter second number: 5
Floor Division = 3

Difficulty:
Beginner

Concepts:
- Variables
- input()
- int()
- Floor Division Operator (//)
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 // num2

print("Floor Division =", result)