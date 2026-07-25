"""
Question 19

Title:
Check Strong Number

Problem Statement:
Write a Python program to check whether a number is a Strong Number.

A Strong Number is a number whose sum of the factorials of its digits equals the number itself.

Example:
145 = 1! + 4! + 5! = 145

Expected Output:
Enter a number: 145

145 is a Strong Number.

Difficulty:
Intermediate

Concepts:
- while loop
- Nested loops
- Factorial
"""

# Solution starts here

number = int(input("Enter a number: "))

original = number
total = 0

while number > 0:
    digit = number % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    total += factorial
    number //= 10

if total == original:
    print(original, "is a Strong Number.")
else:
    print(original, "is not a Strong Number.")