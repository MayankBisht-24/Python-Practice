"""
Question 15

Title:
Calculate Grade

Problem Statement:
Write a Python program to calculate the grade based on marks.

Grade Criteria:
90-100 : A
80-89  : B
70-79  : C
60-69  : D
Below 60 : F

Expected Output:
Enter marks: 86

Grade = B

Difficulty:
Beginner

Concepts:
- if
- elif
- else
"""

# Solution starts here

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade = A")
elif marks >= 80:
    print("Grade = B")
elif marks >= 70:
    print("Grade = C")
elif marks >= 60:
    print("Grade = D")
else:
    print("Grade = F")