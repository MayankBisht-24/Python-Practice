"""
Question 16

Title:
Function to Check Prime Number

Problem Statement:
Write a Python function that returns True if a number is prime,
otherwise False.

Expected Output:
Enter a number: 17

True

Difficulty:
Intermediate

Concepts:
- return
- Boolean
- for loop
"""

# Solution starts here

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

print(is_prime(num))