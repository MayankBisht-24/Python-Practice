"""
Question 13

Title:
Check Prime Number

Problem Statement:
Write a Python program to check whether a given number is prime.

Expected Output:
Enter a number: 17

17 is a Prime Number.

Difficulty:
Intermediate

Concepts:
- for loop
- if statement
"""

# Solution starts here

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a Prime Number.")
else:
    print(number, "is not a Prime Number.")