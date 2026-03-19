# =============================================================================
# Problem  : Python If-Else
# Domain   : Python
# Sub-Domain: Introduction
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
#
# Problem Statement:
#   Given a positive integer n, apply the following conditional rules:
#     - If n is odd                              → print "Weird"
#     - If n is even and in range [2, 5]         → print "Not Weird"
#     - If n is even and in range [6, 20]        → print "Weird"
#     - If n is even and greater than 20         → print "Not Weird"
#
# Input Format : A single line containing a positive integer, n.
#
# Constraints  : 1 ≤ n ≤ 100
#
# Output Format: Print "Weird" if the number is weird, otherwise "Not Weird".
#
# Sample Input 0 : 3
# Sample Output 0: Weird
# Explanation    : 3 is odd → always Weird.
#
# Sample Input 1 : 24
# Sample Output 1: Not Weird
# Explanation    : 24 is even and greater than 20 → Not Weird.
#
# Approach:
#   Use a conditional if-elif-else chain to evaluate the value of n against
#   the given ranges. Python's chained comparison (e.g. 2 <= n <= 5) is used
#   for cleaner, more readable range checks — a Pythonic best practice.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-16
# =============================================================================

#!/bin/python3

# Standard library imports provided by HackerRank's default template.
# Not all are used in this problem, but kept for consistency with the platform.
import math
import os
import random
import re
import sys


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# `if __name__ == '__main__':` ensures this block only runs when the script
# is executed directly — not when it's imported as a module elsewhere.
# All input reading and solution logic must live INSIDE this block.
if __name__ == '__main__':

    # Read a single integer from stdin.
    # input()       → reads a line of text from the user
    # .strip()      → removes any leading/trailing whitespace or newline chars
    # int(...)      → converts the cleaned string to an integer
    n = int(input().strip())

    # ------------------------------------------------------------------
    # Conditional Logic
    # ------------------------------------------------------------------

    # Condition 1: Check if n is odd using the modulo operator (%).
    # n % 2 returns the remainder when n is divided by 2.
    # If remainder is 1, the number is odd → always "Weird".
    if n % 2 == 1:
        print("Weird")

    # Condition 2: n is even AND falls in the inclusive range [2, 5].
    # Python supports chained comparisons: `2 <= n <= 5` is equivalent to
    # `n >= 2 and n <= 5`, but is cleaner and more Pythonic.
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")

    # Condition 3: n is even AND falls in the inclusive range [6, 20].
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")

    # Condition 4: All remaining cases — n is even and greater than 20.
    # No explicit condition needed here since all other cases are already
    # handled above. The `else` acts as the default fallback.
    else:
        print("Not Weird")


# =============================================================================
# Key Concepts Covered:
#   - if / elif / else  : Conditional branching to handle multiple cases
#   - Modulo operator % : Returns remainder of division; used to check parity
#   - Chained comparison: Python allows `a <= x <= b` instead of
#                         `x >= a and x <= b` — cleaner and more readable
#   - __name__ guard    : Best practice to protect executable code from running
#                         on import; all logic should live inside this block
#   - input().strip()   : Safe way to read and clean user input from stdin
#   - int()             : Converts a string to an integer type
#
# Common Mistake (avoid this):
#   Placing the if/elif/else block OUTSIDE the `if __name__ == '__main__':` 
#   guard. While it may still run, it breaks program structure and is 
#   considered bad practice in professional Python code.
# =============================================================================