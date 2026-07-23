"""
Question 07

Title:
Print Multiplication Table

Problem Statement:
Write a Python program to print the multiplication table of a given number up to 10.

Expected Output:
Enter a number: 7

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

Difficulty:
Beginner

Concepts:
- for loop
- Multiplication
"""

# Solution starts here

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")