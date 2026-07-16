"""
Question 19

Title:
Calculate Percentage

Problem Statement:
Write a Python program to calculate percentage from obtained marks and total marks.

Expected Output:
Enter obtained marks: 420
Enter total marks: 500

Percentage = 84.0 %

Difficulty:
Beginner

Concepts:
- Variables
- input()
- float()
- Arithmetic Operators
"""

# Solution starts here

obtained = float(input("Enter obtained marks: "))
total = float(input("Enter total marks: "))

percentage = (obtained / total) * 100

print("\nPercentage =", percentage, "%")