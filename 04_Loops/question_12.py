"""
Question 12

Title:
Check Armstrong Number

Problem Statement:
Write a Python program to check whether a given 3-digit number is an Armstrong number.

Expected Output:
Enter a number: 153

153 is an Armstrong Number.

Difficulty:
Intermediate

Concepts:
- while loop
- Exponent (**)
"""

# Solution starts here

number = int(input("Enter a number: "))

original_number = number
armstrong_sum = 0

while number > 0:
    digit = number % 10
    armstrong_sum += digit ** 3
    number //= 10

if original_number == armstrong_sum:
    print(original_number, "is an Armstrong Number.")
else:
    print(original_number, "is not an Armstrong Number.")