"""
Question 08

Title:
Count the Digits in a Number

Problem Statement:
Write a Python program to count the total number of digits in a given number.

Expected Output:
Enter a number: 45892

Total Digits = 5

Difficulty:
Beginner

Concepts:
- while loop
- Integer Division
"""

# Solution starts here

number = int(input("Enter a number: "))

count = 0

while number > 0:
    number //= 10
    count += 1

print("Total Digits =", count)