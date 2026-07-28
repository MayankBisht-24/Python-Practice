"""
Question 13

Title:
Return the Largest of Two Numbers

Problem Statement:
Write a Python function that returns the larger of two numbers.

Expected Output:
Enter first number: 25
Enter second number: 40

Largest Number = 40

Difficulty:
Beginner

Concepts:
- return
- if-else
"""

# Solution starts here

def largest(num1, num2):
    if num1 > num2:
        return num1
    return num2

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

result = largest(first, second)

print("Largest Number =", result)