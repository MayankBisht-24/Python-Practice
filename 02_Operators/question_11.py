"""
Question 11

Title:
Check Even or Odd using Modulus Operator

Problem Statement:
Write a Python program to check whether a number is even or odd.

Expected Output:
Enter a number: 18
18 is Even

Difficulty:
Beginner

Concepts:
- Variables
- input()
- int()
- Modulus Operator (%)
"""

# Solution starts here

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")