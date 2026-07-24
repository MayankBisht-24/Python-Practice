"""
Question 15

Title:
Print Fibonacci Series

Problem Statement:
Write a Python program to print the Fibonacci series up to N terms.

Expected Output:
Enter number of terms: 7

0
1
1
2
3
5
8

Difficulty:
Intermediate

Concepts:
- for loop
- Variables
"""

# Solution starts here

terms = int(input("Enter number of terms: "))

first = 0
second = 1

for i in range(terms):
    print(first)

    next_number = first + second
    first = second
    second = next_number