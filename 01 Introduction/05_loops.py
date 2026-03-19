# =============================================================================
# Problem  : Loops
# Domain   : Python
# Sub-Domain: Introduction
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
#
# Problem Statement:
#   Given a non-negative integer n, for every integer i in range [0, n),
#   print the square of i on a separate line.
#   In other words, print i² for all i where 0 ≤ i < n.
#
# Input Format : A single line containing a non-negative integer, n.
#
# Constraints  : 1 ≤ n ≤ 20
#
# Output Format: Print n lines, each containing the square of i (i²),
#                starting from i = 0 up to i = n-1.
#
# Example:
#   Input  → n = 3
#   Output →
#     0       (0² = 0)
#     1       (1² = 1)
#     4       (2² = 4)
#
# Sample Input 0 : 5
# Sample Output 0:
#   0
#   1
#   4
#   9
#   16
#
# Approach:
#   Use a for loop with range(n) to iterate over all integers from 0 to n-1.
#   For each integer i, compute its square using i * i and print the result.
#   range(n) generates values [0, 1, 2, ..., n-1] — note that n itself
#   is excluded (range is right-exclusive).
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-17
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read a single integer n from stdin.
    # input() reads a line as a string; int() converts it to an integer.
    n = int(input())

    # ------------------------------------------------------------------
    # Loop and Print Squares
    # ------------------------------------------------------------------

    # range(n) generates a sequence of integers starting from 0
    # up to (but NOT including) n → [0, 1, 2, ..., n-1].
    # The for loop assigns each value in that sequence to i, one at a time.
    for i in range(n):

        # Compute and print the square of the current value of i.
        # i * i multiplies i by itself to get i².
        # Alternative: i ** 2 (exponentiation operator) produces the same result.
        print(i * i)


# =============================================================================
# Key Concepts Covered:
#   - for loop       : Iterates over a sequence, executing the body once
#                      per element. Syntax: `for variable in sequence:`
#   - range(n)       : Generates integers from 0 up to (not including) n.
#                      range(n)       → [0, 1, 2, ..., n-1]
#                      range(a, b)    → [a, a+1, ..., b-1]
#                      range(a, b, s) → [a, a+s, a+2s, ...] with step s
#   - i * i          : Multiplication to compute the square of i.
#   - i ** 2         : Exponentiation — alternative way to compute i squared.
#                      Both i * i and i ** 2 give identical results; i * i
#                      is marginally faster for squaring a single value.
#   - Zero-based loop: range(n) starts at 0, not 1. This is a fundamental
#                      Python (and programming) convention to be comfortable with.
#
# range() Quick Reference:
#   range(5)        → 0, 1, 2, 3, 4          (stop only)
#   range(2, 6)     → 2, 3, 4, 5             (start, stop)
#   range(0, 10, 2) → 0, 2, 4, 6, 8          (start, stop, step)
#   range(5, 0, -1) → 5, 4, 3, 2, 1          (countdown)
#
# Alternative Solution (using exponentiation operator):
#   for i in range(n):
#       print(i ** 2)
# =============================================================================