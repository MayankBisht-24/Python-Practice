"""
Question 18

Title:
Check Perfect Number

Problem Statement:
Write a Python program to check whether a number is a Perfect Number.

A Perfect Number is equal to the sum of its proper divisors.

Example:
6 → 1 + 2 + 3 = 6

Expected Output:
Enter a number: 28

28 is a Perfect Number.

Difficulty:
Intermediate

Concepts:
- for loop
- Factors
"""

# Solution starts here

number = int(input("Enter a number: "))

divisor_sum = 0

for i in range(1, number):
    if number % i == 0:
        divisor_sum += i

if divisor_sum == number:
    print(number, "is a Perfect Number.")
else:
    print(number, "is not a Perfect Number.")