"""
Question 15

Title:
Convert Seconds into Hours, Minutes and Seconds

Problem Statement:
Write a Python program to convert seconds into hours, minutes and seconds.

Expected Output:
Enter seconds: 3665

Hours = 1
Minutes = 1
Seconds = 5

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

seconds = int(input("Enter seconds: "))

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("\nHours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)