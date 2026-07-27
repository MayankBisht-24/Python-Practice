"""
Question 09

Title:
Function to Calculate Area of a Rectangle

Problem Statement:
Write a Python function that accepts length and width and prints the area.

Expected Output:
Enter length: 12
Enter width: 5

Area = 60

Difficulty:
Beginner

Concepts:
- Function
- Parameters
"""

# Solution starts here

def area_of_rectangle(length, width):
    print("Area =", length * width)

length = int(input("Enter length: "))
width = int(input("Enter width: "))

area_of_rectangle(length, width)