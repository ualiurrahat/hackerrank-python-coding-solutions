# =============================================================================
# Problem  : Arithmetic Operators
# Domain   : Python
# Sub-Domain: Introduction
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
#
# Problem Statement:
#   Given two integers a and b, print three lines:
#     - Line 1: Sum of a and b        (a + b)
#     - Line 2: Difference of a and b (a - b)
#     - Line 3: Product of a and b    (a * b)
#
# Input Format : Two lines, each containing one integer (a, then b).
#
# Constraints  : 1 ≤ a ≤ 10^10, 1 ≤ b ≤ 10^10
#
# Output Format: Print the sum, difference, and product on separate lines.
#
# Example:
#   Input  → a = 3, b = 5
#   Output →
#     8       (3 + 5)
#    -2       (3 - 5)
#    15       (3 * 5)
#
# Sample Input 0 : a = 3, b = 2
# Sample Output 0:
#   5
#   1
#   6
#
# Approach:
#   Read two integers from stdin, then apply Python's basic arithmetic
#   operators (+, -, *) and print each result on a separate line.
#   All logic is properly enclosed within the __name__ guard.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-16
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
# See: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Read the first integer from stdin.
    # input() reads a line as a string; int() converts it to an integer.
    a = int(input())

    # Read the second integer from stdin.
    b = int(input())

    # ------------------------------------------------------------------
    # Arithmetic Operations
    # ------------------------------------------------------------------

    # Line 1: Addition — calculates the total of a and b.
    # The + operator adds two numeric values together.
    print(a + b)

    # Line 2: Subtraction — calculates how much larger a is than b.
    # The - operator subtracts the right operand from the left.
    # Result can be negative if b > a.
    print(a - b)

    # Line 3: Multiplication — calculates the product of a and b.
    # The * operator multiplies two numeric values.
    print(a * b)


# =============================================================================
# Key Concepts Covered:
#   - Arithmetic operators : + (add), - (subtract), * (multiply)
#   - int(input())         : Standard pattern to read an integer from stdin
#   - __name__ guard       : Ensures code runs only on direct execution,
#                            not on import — always wrap your logic inside it
#   - print()              : Each call prints on a new line by default
#                            due to the built-in end='\n' parameter
#
# Python Arithmetic Operators (Quick Reference):
#   a + b   → Addition
#   a - b   → Subtraction
#   a * b   → Multiplication
#   a / b   → Division (returns float)
#   a // b  → Floor Division (returns integer, discards remainder)
#   a % b   → Modulo (returns remainder)
#   a ** b  → Exponentiation (a raised to the power of b)
#
# Common Mistake (avoid this):
#   Placing print() statements OUTSIDE the `if __name__ == '__main__':` block.
#   Variables like `a` and `b` are defined inside the block, so referencing
#   them outside would raise a NameError in strict or imported contexts.
# =============================================================================