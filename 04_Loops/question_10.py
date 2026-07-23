"""
Question 10

Title:
Reverse a Number

Problem Statement:
Write a Python program to reverse the digits of a given number.

Expected Output:
Enter a number: 12345

Reversed Number = 54321

Difficulty:
Beginner

Concepts:
- while loop
- Modulus Operator
- Integer Division
"""

# Solution starts here

number = int(input("Enter a number: "))

reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print("Reversed Number =", reversed_number)