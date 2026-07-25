"""
Question 20

Title:
Check Spy Number

Problem Statement:
Write a Python program to check whether a number is a Spy Number.

A Spy Number is a number in which the sum of digits equals the product of digits.

Example:
123
Sum = 1 + 2 + 3 = 6
Product = 1 × 2 × 3 = 6

Expected Output:
Enter a number: 123

123 is a Spy Number.

Difficulty:
Intermediate

Concepts:
- while loop
- Sum and Product of digits
"""

# Solution starts here

number = int(input("Enter a number: "))

original = number
digit_sum = 0
digit_product = 1

while number > 0:
    digit = number % 10
    digit_sum += digit
    digit_product *= digit
    number //= 10

if digit_sum == digit_product:
    print(original, "is a Spy Number.")
else:
    print(original, "is not a Spy Number.")