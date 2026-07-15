"""
Question 14

Title:
Convert Minutes into Hours

Problem Statement:
Write a Python program to convert minutes into hours and remaining minutes.

Expected Output:
Enter minutes: 135
Hours = 2
Minutes = 15

Difficulty:
Beginner

Concepts:
- Variables
- input()
- int()
- Floor Division (//)
- Modulus (%)
"""

# Solution starts here

minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours =", hours)
print("Minutes =", remaining_minutes)