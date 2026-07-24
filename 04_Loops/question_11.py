"""
Question 11

Title:
Check Palindrome Number

Problem Statement:
Write a Python program to check whether a given number is a palindrome.

Expected Output:
Enter a number: 121

121 is a Palindrome Number.

Difficulty:
Intermediate

Concepts:
- while loop
- Modulus (%)
- Integer Division (//)
"""

# Solution starts here

number = int(input("Enter a number: "))

original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

if original_number == reversed_number:
    print(original_number, "is a Palindrome Number.")
else:
    print(original_number, "is not a Palindrome Number.")