"""
Question 09

Title:
Find the Sum of Digits

Problem Statement:
Write a Python program to calculate the sum of all digits of a given number.

Expected Output:
Enter a number: 1234

Sum of Digits = 10

Difficulty:
Beginner

Concepts:
- while loop
- Modulus Operator
"""

# Solution starts here

number = int(input("Enter a number: "))

digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

print("Sum of Digits =", digit_sum)