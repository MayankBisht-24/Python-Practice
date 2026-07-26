"""
Question 04

Title:
Function to Add Two Numbers

Problem Statement:
Write a function that accepts two numbers and prints their sum.

Expected Output:
Enter first number: 15
Enter second number: 20

Sum = 35

Difficulty:
Beginner

Concepts:
- Parameters
- Function
"""

# Solution starts here

def add(num1, num2):
    print("Sum =", num1 + num2)

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

add(first, second)