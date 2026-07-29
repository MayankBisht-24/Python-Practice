"""
Question 19

Title:
Keyword Arguments

Problem Statement:
Write a function that displays a student's name and age.
Call it using keyword arguments.

Expected Output:
Name: Mayank
Age: 23

Difficulty:
Intermediate

Concepts:
- Keyword Arguments
"""

# Solution starts here

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student(age=23, name="Mayank")