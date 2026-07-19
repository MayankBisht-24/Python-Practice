"""
Question 08

Title:
Find the Largest of Three Numbers

Problem Statement:
Write a Python program to find the largest among three numbers.

Expected Output:
Enter first number: 15
Enter second number: 40
Enter third number: 25

Largest Number = 40

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

if num1 >= num2 and num1 >= num3:
    print("Largest Number =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest Number =", num2)
else:
    print("Largest Number =", num3)