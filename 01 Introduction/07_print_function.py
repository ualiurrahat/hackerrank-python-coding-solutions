# =============================================================================
# Problem  : Print Function
# Domain   : Python
# Sub-Domain: Introduction
# Difficulty: Easy
# Score    : 20 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
#
# Problem Statement:
#   Given an integer n, print all integers from 1 through n as a single
#   concatenated string with no spaces — without using any string methods.
#
#   Example:
#     n = 3 → print "123"
#     n = 5 → print "12345"
#
# Input Format : A single line containing a positive integer, n.
#
# Constraints  : 1 ≤ n ≤ 150
#
# Output Format: Print the integers from 1 to n as one continuous string,
#                with no spaces or separators.
#
# Sample Input 0 : 3
# Sample Output 0: 123
#
# Approach:
#   Use range(1, n+1) to generate integers from 1 to n (inclusive).
#   Convert each integer to a string with str(), collect them, and join
#   them into a single string using "".join() — which concatenates all
#   elements with no separator between them.
#   This avoids repeated string concatenation (+=) in a loop, which
#   creates a new string object on every iteration and is inefficient.
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

    # Read a single integer n from stdin.
    n = int(input())

    # ------------------------------------------------------------------
    # Build and Print the Concatenated String
    # ------------------------------------------------------------------

    # Step 1: range(1, n+1) generates integers from 1 to n inclusive.
    #         Note: range(1, n+1) is used because range() excludes the
    #         stop value — so to include n, we pass n+1 as the stop.

    # Step 2: str(i) converts each integer i into its string equivalent.
    #         e.g. 1 → "1", 2 → "2", 3 → "3"
    #         This is necessary because you cannot join integers directly —
    #         join() requires all elements to be strings.

    # Step 3: "".join(...) concatenates all string elements into one
    #         single string with no separator (empty string "").
    #         e.g. ["1", "2", "3"] → "123"

    # All three steps are combined into one clean, efficient expression:
    print("".join(str(i) for i in range(1, n+1)))


# =============================================================================
# Key Concepts Covered:
#   - range(1, n+1)  : Generates integers from 1 to n inclusive.
#                      range() is right-exclusive, so n+1 is needed to include n.
#   - str(i)         : Converts an integer to its string representation.
#                      Required because join() only works with strings.
#   - "".join(...)   : Concatenates an iterable of strings into one string.
#                      The string before .join() acts as the separator.
#                      "" means no separator — elements are joined directly.
#                      e.g. "-".join(["a","b","c"]) → "a-b-c"
#                           "".join(["1","2","3"])  → "123"
#   - Generator expr : `str(i) for i in range(1, n+1)` is a generator
#                      expression — a memory-efficient way to produce values
#                      one at a time without building a full list in memory.
#
# Why NOT use string concatenation (+=) in a loop?
#   digitStr = ""
#   for i in range(1, n+1):
#       digitStr += str(i)       ← Creates a NEW string object every iteration
#   This approach works but is inefficient. Each += discards the old string
#   and allocates a new one in memory. For large n, this becomes very slow.
#   "".join() builds the final string in one efficient operation — always
#   prefer join() over += when concatenating strings in a loop.
#
# join() Separator Quick Reference:
#   "".join(["1","2","3"])   → "123"       (no separator)
#   " ".join(["1","2","3"])  → "1 2 3"     (space separator)
#   "-".join(["1","2","3"])  → "1-2-3"     (dash separator)
#   ", ".join(["1","2","3"]) → "1, 2, 3"   (comma-space separator)
# =============================================================================