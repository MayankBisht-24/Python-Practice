"""
Question 10

Title:
Function to Print Multiplication Table

Problem Statement:
Write a Python function that accepts a number and prints its multiplication table up to 10.

Expected Output:
Enter a number: 5

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

Difficulty:
Beginner

Concepts:
- Function
- for loop
- Parameters
"""

# Solution starts here

def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number: "))

multiplication_table(num)