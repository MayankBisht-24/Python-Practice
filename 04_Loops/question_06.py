"""
Question 06

Title:
Calculate the Factorial of a Number

Problem Statement:
Write a Python program to calculate the factorial of a given number using a for loop.

Expected Output:
Enter a number: 5

Factorial = 120

Difficulty:
Beginner

Concepts:
- for loop
- Accumulator Variable
"""

# Solution starts here

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)