"""
Question 20

Title:
Calculate Body Mass Index (BMI)

Problem Statement:
Write a Python program to calculate BMI using weight and height.

Formula:
BMI = weight / (height × height)

Expected Output:
Enter weight (kg): 72
Enter height (m): 1.75

BMI = 23.51

Difficulty:
Beginner

Concepts:
- Variables
- input()
- float()
- Arithmetic Operators
"""

# Solution starts here

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("\nBMI =", round(bmi, 2))