"""
This module provides a simple function to add two numbers
and display the result.
"""

def add_numbers(num1, num2):
    """
    Add two numbers and return the sum.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.

    Returns:
    float: The sum of num1 and num2.
    """
    return num1 + num2

# Input: Getting numbers from user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Output: Displaying the sum
sum_of_numbers = add_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is: {sum_of_numbers}")


