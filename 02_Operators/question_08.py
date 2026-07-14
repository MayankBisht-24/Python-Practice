"""
Question 08

Title:
Calculate Average of Two Numbers

Problem Statement:
Write a Python program to take two numbers as input and calculate their average.

Expected Output:
Enter first number: 10
Enter second number: 20
Average = 15.0

Difficulty:
Beginner

Concepts:
- Variables
- input()
- int()
- Arithmetic Operators
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

average = (num1 + num2) / 2

print("Average =", average)