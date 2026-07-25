"""
Question 16

Title:
Find the Greatest Common Divisor (GCD / HCF)

Problem Statement:
Write a Python program to find the GCD (HCF) of two numbers using a loop.

Expected Output:
Enter first number: 24
Enter second number: 36

GCD = 12

Difficulty:
Intermediate

Concepts:
- for loop
- if statement
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD =", gcd)