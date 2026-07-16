"""
Question 18

Title:
Calculate Simple Interest

Problem Statement:
Write a Python program to calculate Simple Interest.

Expected Output:
Enter Principal: 10000
Enter Rate: 8
Enter Time: 2

Simple Interest = 1600.0

Difficulty:
Beginner

Concepts:
- Variables
- input()
- float()
- Arithmetic Operators
"""

# Solution starts here

principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

si = (principal * rate * time) / 100

print("\nSimple Interest =", si)