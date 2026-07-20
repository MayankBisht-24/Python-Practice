"""
Question 13

Title:
Find the Smallest of Three Numbers

Problem Statement:
Write a Python program to find the smallest among three numbers.

Expected Output:
Enter first number: 15
Enter second number: 8
Enter third number: 20

Smallest Number = 8

Difficulty:
Beginner

Concepts:
- if
- elif
- else
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 <= num2 and num1 <= num3:
    print("Smallest Number =", num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest Number =", num2)
else:
    print("Smallest Number =", num3)