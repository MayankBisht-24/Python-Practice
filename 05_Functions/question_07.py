"""
Question 07

Title:
Function to Check Even or Odd

Problem Statement:
Write a Python function that accepts a number and prints whether it is Even or Odd.

Expected Output:
Enter a number: 15

15 is Odd

Difficulty:
Beginner

Concepts:
- Function
- Parameters
- if-else
"""

# Solution starts here

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

num = int(input("Enter a number: "))

check_even_odd(num)