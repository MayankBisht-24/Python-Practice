"""
Question 09

Title:
Count Words in a Sentence

Problem Statement:
Write a Python program to count the total number of words in a sentence.

Expected Output:
Enter a sentence:
Python is easy to learn

Total Words = 5

Difficulty:
Beginner

Concepts:
- split()
- len()
"""

# Solution starts here

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Total Words =", len(words))