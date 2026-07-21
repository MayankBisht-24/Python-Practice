"""
Question 17

Title:
Check Largest of Four Numbers

Problem Statement:
Write a Python program to find the largest among four numbers.

Expected Output:
Enter first number: 20
Enter second number: 45
Enter third number: 12
Enter fourth number: 30

Largest Number = 45

Difficulty:
Intermediate

Concepts:
- if
- elif
- Logical Operator (and)
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print("Largest Number =", num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print("Largest Number =", num2)
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print("Largest Number =", num3)
else:
    print("Largest Number =", num4)