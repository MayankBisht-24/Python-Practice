"""
Question 03

Title:
Function with One Parameter

Problem Statement:
Write a function named greet(name) that greets the user.

Expected Output:
Enter your name: Rahul

Hello Rahul!

Difficulty:
Beginner

Concepts:
- Parameters
- Arguments
"""

# Solution starts here

def greet(name):
    print(f"Hello {name}!")

user_name = input("Enter your name: ")

greet(user_name)