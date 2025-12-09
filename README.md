"""
Python Console Calculator Program

Description:
This script provides a basic command-line interface (CLI) calculator.
It defines separate functions for the four core arithmetic operations
(addition, subtraction, multiplication, and division) and uses conditional
logic (if/elif/else) to execute the chosen operation based on user input.

The program prompts the user for the desired operation symbol (+, -, *, /)
and two numeric inputs (x and y).

Note: This version uses simple input conversion (int) and does not include
robust error handling for non-numeric input or division by zero, which is
recommended for professional production code.
"""

def sum(x, y):
    """
    Calculates the sum of two numbers.

    :param x: The first number.
    :param y: The second number.
    :return: The sum (x + y).
    """
    return x + y

def dif(x, y):
    """
    Calculates the difference between the first and second number.

    :param x: The first number (minuend).
    :param y: The second number (subtrahend).
    :return: The difference (x - y).
    """
    return x - y

def mul(x, y):
    """
    Calculates the product of two numbers.

    :param x: The first number.
    :param y: The second number.
    :return: The product (x * y).
    """
    return x * y

def div(x, y):
    """
    Calculates the quotient when dividing the first number by the second.

    :param x: The numerator (dividend).
    :param y: The denominator (divisor).
    :return: The quotient (x / y).
    """
    # Note: A simple division is performed here; division by zero is not handled.
    return x / y

# --- Main Program Execution ---

# 1. Get the operation choice from the user
z = input("enter the opeation you want to prform +,-,*,/:")

# 2. Get the first number (converted to an integer)
x = int(input("enter the first number:"))

# 3. Get the second number (converted to an integer)
y = int(input("enter the second number:"))

# 4. Use conditional statements to perform the selected operation
if z == "+":
    print('the sum is:', sum(x, y))
elif z == "-":
    print('the difference is:', dif(x, y))
elif z == "*":
    print('the product is:', mul(x, y))
elif z == "/":
    # Checks to prevent division by zero before calling the function
    if y != 0:
        print('the quotient:', div(x, y))
    else:
        print("Error: Cannot divide by zero.")
else:
    # Handles cases where the operation symbol is not recognized
    print("invalid operation")
