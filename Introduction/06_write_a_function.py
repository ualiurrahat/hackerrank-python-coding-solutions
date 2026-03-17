# =============================================================================
# Problem  : Write a Function
# Domain   : Python
# Sub-Domain: Introduction
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
#
# Problem Statement:
#   Given a year, determine whether it is a leap year in the Gregorian calendar.
#   Return True if it is a leap year, otherwise return False.
#
#   Leap Year Rules (Gregorian Calendar):
#     1. If the year is divisible by 4    → it IS a leap year, UNLESS:
#     2. If the year is divisible by 100  → it is NOT a leap year, UNLESS:
#     3. If the year is divisible by 400  → it IS a leap year.
#
#   In plain English (priority order):
#     - Divisible by 400 → Leap year           ✅  (e.g. 2000, 2400)
#     - Divisible by 100 → NOT a leap year     ❌  (e.g. 1800, 1900, 2100)
#     - Divisible by 4   → Leap year           ✅  (e.g. 1996, 2024)
#     - None of the above → NOT a leap year    ❌  (e.g. 1990, 2019)
#
# Input Format : A single line containing a positive integer — the year.
#
# Constraints  : 1900 ≤ year ≤ 10^5
#
# Output Format: The function returns a Boolean (True or False).
#                Output is handled by the provided code stub.
#
# Sample Input 0 : 1990
# Sample Output 0: False
# Explanation    : 1990 is not divisible by 4, so it is not a leap year.
#
# Approach:
#   Use a boolean variable `leap` initialized to False.
#   Apply the Gregorian leap year rules as a single compound condition:
#     - (year % 4 == 0 and year % 100 != 0) → divisible by 4 but NOT by 100
#     - OR (year % 400 == 0)                → divisible by 400
#   If either condition is True, set leap = True and return it.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-16
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Function Definition
# -----------------------------------------------------------------------------

def is_leap(year):
    """
    Determine whether a given year is a leap year in the Gregorian calendar.

    Args:
        year (int): The year to evaluate.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """

    # Initialize the result as False.
    # We assume the year is NOT a leap year unless proven otherwise.
    leap = False

    # Apply the Gregorian leap year rules as a single compound condition.
    #
    # Condition A: (year % 4 == 0 and year % 100 != 0)
    #   → The year is divisible by 4 BUT not divisible by 100.
    #   → Covers most common leap years: 1996, 2004, 2008, 2024, etc.
    #
    # Condition B: (year % 400 == 0)
    #   → The year is divisible by 400.
    #   → Covers century leap years: 2000, 2400, etc.
    #
    # The `or` operator means: if EITHER condition A or condition B is True,
    # the entire expression evaluates to True → it is a leap year.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    # Return the boolean result — True for leap year, False otherwise.
    return leap


# -----------------------------------------------------------------------------
# Main Guard — Input Handling
# -----------------------------------------------------------------------------

# All input reading and output logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the year as an integer from stdin.
    year = int(input())

    # Call is_leap() with the given year and print the returned boolean.
    print(is_leap(year))


# =============================================================================
# Key Concepts Covered:
#   - def keyword       : Used to define a reusable function in Python.
#                         Syntax: `def function_name(parameters):`
#   - return statement  : Exits the function and sends a value back to the caller.
#                         Once return is hit, no further code in the function runs.
#   - bool (Boolean)    : A data type with only two values — True or False.
#                         `leap` is a boolean variable used to store the result.
#   - Modulo operator % : Returns the remainder of division.
#                         year % 4 == 0 means year is perfectly divisible by 4.
#   - Compound condition: Two or more conditions joined by `and` / `or`.
#                         `and` → both sides must be True.
#                         `or`  → at least one side must be True.
#   - Docstring         : The triple-quoted string right below the function
#                         definition documents its purpose, arguments, and return
#                         value. A professional Python best practice.
#   - __name__ guard    : Input reading and print() belong inside this block —
#                         not at the module level — to follow proper structure.
#
# Leap Year Test Cases (verify your logic):
#   2000 → True   (divisible by 400)
#   1900 → False  (divisible by 100, not 400)
#   2024 → True   (divisible by 4, not 100)
#   1990 → False  (not divisible by 4)
#
# Alternative Solution (if-elif-else chain):
#   if year % 400 == 0:
#       return True
#   elif year % 100 == 0:
#       return False
#   elif year % 4 == 0:
#       return True
#   else:
#       return False
#   This approach checks rules one at a time and is more readable for beginners.
#   Both solutions are equally correct — your compound condition is more concise.
# =============================================================================