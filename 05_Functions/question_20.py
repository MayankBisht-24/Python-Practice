"""
Question 20

Title:
Variable Number of Arguments

Problem Statement:
Write a function that accepts any number of integers
and returns their sum.

Expected Output:
Total = 100

Difficulty:
Intermediate

Concepts:
- *args
"""

# Solution starts here

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Total =", add_numbers(10, 20, 30, 40))