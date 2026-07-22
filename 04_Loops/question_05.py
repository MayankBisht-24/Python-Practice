"""
Question 05

Title:
Calculate Sum from 1 to N

Problem Statement:
Write a Python program to calculate the sum of numbers from 1 to N.

Expected Output:
Enter N: 5

Sum = 15

Difficulty:
Beginner

Concepts:
- for loop
- Accumulator Variable
"""

# Solution starts here

n = int(input("Enter N: "))

total = 0

for number in range(1, n + 1):
    total += number

print("Sum =", total)