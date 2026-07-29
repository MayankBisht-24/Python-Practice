"""
Question 17

Title:
Return Multiple Values

Problem Statement:
Write a function that accepts two numbers and returns
their sum and product.

Expected Output:
Enter first number: 5
Enter second number: 6

Sum = 11
Product = 30

Difficulty:
Intermediate

Concepts:
- Multiple Return Values
"""

# Solution starts here

def calculate(num1, num2):
    return num1 + num2, num1 * num2


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

sum_result, product_result = calculate(first, second)

print("Sum =", sum_result)
print("Product =", product_result)