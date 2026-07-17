"""
Question 02

Title:
Check Even or Odd

Problem Statement:
Write a Python program to check whether a number is even or odd.

Expected Output:
Enter a number: 25

25 is Odd

Difficulty:
Beginner

Concepts:
- if
- else
- Modulus Operator (%)
"""

# Solution starts here

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")