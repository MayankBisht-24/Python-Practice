"""
Question 06

Title:
Count Consonants in a String

Problem Statement:
Write a Python program to count the total number of consonants in a string.

Expected Output:
Enter a string: Python

Total Consonants = 5

Difficulty:
Beginner

Concepts:
- Strings
- for loop
- if statement
"""

# Solution starts here

text = input("Enter a string: ").lower()

count = 0

for character in text:
    if character.isalpha() and character not in "aeiou":
        count += 1

print("Total Consonants =", count)