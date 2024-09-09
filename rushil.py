"""
This module provides a simple function to add two numbers
and display the result.
"""

def subtract_numbers(num1, num2):
    """
    Subtract two numbers and return the sum.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.

    Returns:
    float: The diff of num1 and num2.
    """
    >return num1 - num2

# Input: Getting numbers from user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Output: Displaying the sum
diff_of_numbers = subtract_numbers(number1, number2)
print(f"The diff of {number1} and {number2} is: {diff_of_numbers}")
