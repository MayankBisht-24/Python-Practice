"""
Question 05

Title:
Count Vowels in a String

Problem Statement:
Write a Python program to count the total number of vowels in a string.

Expected Output:
Enter a string: Education

Total Vowels = 5

Difficulty:
Beginner

Concepts:
- for loop
- if statement
- Strings
"""

# Solution starts here

text = input("Enter a string: ").lower()

count = 0

for character in text:
    if character in "aeiou":
        count += 1

print("Total Vowels =", count)