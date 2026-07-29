"""
Question 18

Title:
Default Arguments

Problem Statement:
Write a function that greets a user.
If no name is provided, greet "Guest".

Expected Output:
Hello, Guest!

Difficulty:
Intermediate

Concepts:
- Default Arguments
"""

# Solution starts here

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()