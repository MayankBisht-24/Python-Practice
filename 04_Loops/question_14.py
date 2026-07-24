"""
Question 14

Title:
Print Prime Numbers from 1 to N

Problem Statement:
Write a Python program to print all prime numbers from 1 to N.

Expected Output:
Enter N: 20

2
3
5
7
11
13
17
19

Difficulty:
Intermediate

Concepts:
- Nested for loops
"""

# Solution starts here

n = int(input("Enter N: "))

for number in range(2, n + 1):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)