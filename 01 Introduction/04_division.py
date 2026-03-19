# =============================================================================
# Problem  : Division
# Domain   : Python
# Sub-Domain: Introduction
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
#
# Problem Statement:
#   Given two integers a and b, print two lines:
#     - Line 1: Result of integer division  (a // b)
#     - Line 2: Result of float division    (a / b)
#   No rounding or formatting is necessary.
#
# Input Format : Two lines, each containing one integer (a, then b).
#
# Output Format: Print integer division result, then float division result
#                on separate lines.
#
# Example:
#   Input  → a = 3, b = 5
#   Output →
#     0           (3 // 5 → integer division, discards remainder)
#     0.6         (3 / 5  → float division, keeps decimal precision)
#
# Sample Input 0 : a = 4, b = 3
# Sample Output 0:
#   1
#   1.33333333333
#
# Approach:
#   Read two integers from stdin, then apply Python's two division operators:
#     - // (floor division) → returns an integer, discards the remainder
#     -  / (true division)  → returns a float, preserves decimal precision
#   Print each result on a separate line with no formatting needed.
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
if __name__ == '__main__':

    # Read the first integer from stdin.
    # input() reads a line as a string; int() converts it to an integer.
    a = int(input())

    # Read the second integer from stdin.
    b = int(input())

    # ------------------------------------------------------------------
    # Division Operations
    # ------------------------------------------------------------------

    # Line 1: Integer Division (Floor Division)
    # The // operator divides a by b and returns the largest integer
    # less than or equal to the result — effectively discarding any remainder.
    # Example: 4 // 3 → 1  (not 1.333...)
    # Example: 3 // 5 → 0  (not 0.6)
    print(a // b)

    # Line 2: Float Division (True Division)
    # The / operator divides a by b and returns a float (decimal) result,
    # preserving full precision without rounding.
    # Example: 4 / 3 → 1.3333333333333333
    # Example: 3 / 5 → 0.6
    # Note: In Python 3, / always returns a float even if both operands
    # are integers. This behavior was different in Python 2.
    print(a / b)


# =============================================================================
# Key Concepts Covered:
#   - // (Floor Division) : Divides and returns an integer, drops the remainder.
#                           Result is always rounded DOWN toward negative infinity.
#                           Example: 7 // 2 → 3,  -7 // 2 → -4
#   - /  (True Division)  : Divides and returns a float with full precision.
#                           Example: 7 / 2 → 3.5
#   - Python 3 vs Python 2: In Python 2, `/` between two integers performed
#                           integer division. Python 3 fixed this — `/` always
#                           returns a float, making behavior more predictable.
#   - No formatting needed: Python's print() displays floats with their natural
#                           precision — no round() or format() required here.
#
# Division Operators Quick Reference:
#   a / b   → True (float) division       e.g. 4 / 3  = 1.3333333333333333
#   a // b  → Floor (integer) division    e.g. 4 // 3 = 1
#   a % b   → Modulo (remainder only)     e.g. 4 % 3  = 1
#   divmod(a, b) → Returns (quotient, remainder) as a tuple
#                                         e.g. divmod(4, 3) = (1, 1)
# =============================================================================