# =============================================================================
# Problem  : sWAP cASE
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
#
# Problem Statement:
#   Given a string, swap the case of every character — convert all uppercase
#   letters to lowercase and all lowercase letters to uppercase.
#   Non-alphabetic characters (digits, punctuation, spaces) remain unchanged.
#
# Input Format:
#   A single line containing a string s.
#
# Constraints:
#   - 0 < len(s) ≤ 1000
#
# Output Format:
#   Print the case-swapped version of the string.
#
# Example:
#   "Www.HackerRank.com"  →  "wWW.hACKERrANK.COM"
#   "Pythonist 2"         →  "pYTHONIST 2"
#
# Sample Input 0:
#   HackerRank.com presents "Pythonist 2".
#
# Sample Output 0:
#   hACKERrANK.COM PRESENTS "pYTHONIST 2"
#
# Approach:
#   Use Python's built-in str.swapcase() method, which handles the entire
#   case-swapping logic internally in a single call — no manual iteration
#   or conditional checking needed. Non-alphabetic characters are unaffected.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-02
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Function Definition
# -----------------------------------------------------------------------------

def swap_case(s):
    """
    Swap the case of every character in the given string.

    Args:
        s (str): The input string to modify.

    Returns:
        str: The string with all uppercase letters converted to lowercase
             and all lowercase letters converted to uppercase.
    """

    # str.swapcase() is a built-in Python string method that swaps the case
    # of every alphabetic character in the string in a single operation.
    # Uppercase → lowercase, lowercase → uppercase.
    # Digits, spaces, and punctuation are left completely unchanged.
    # e.g. "HackerRank.com" → "hACKERrANK.COM"
    return s.swapcase()


# -----------------------------------------------------------------------------
# Main Guard — Input Handling
# -----------------------------------------------------------------------------

# All input reading and output logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the input string from stdin.
    s = input()

    # Call swap_case() and store the returned modified string.
    result = swap_case(s)

    # Print the final case-swapped string.
    print(result)


# =============================================================================
# Key Concepts Covered:
#   - str.swapcase()   : Built-in method that swaps the case of every
#                        alphabetic character in a string. Returns a NEW
#                        string — the original is not modified (strings are
#                        immutable in Python).
#   - String immutability: Strings in Python cannot be changed in-place.
#                        All string methods return a NEW modified string.
#   - str methods      : Python strings come with a rich set of built-in
#                        methods. No imports are needed to use them.
#
# Common String Case Methods Quick Reference:
#   s.swapcase()  → Swap uppercase ↔ lowercase
#   s.upper()     → Convert all characters to uppercase
#   s.lower()     → Convert all characters to lowercase
#   s.capitalize()→ Capitalize only the first character
#   s.title()     → Capitalize the first letter of every word
#
# Alternative Solution (manual iteration — for learning purposes):
#   result = ""
#   for char in s:
#       if char.isupper():
#           result += char.lower()
#       elif char.islower():
#           result += char.upper()
#       else:
#           result += char        # digits, spaces, punctuation unchanged
#   return result
#   swapcase() does all of this internally in one call — always prefer it.
# =============================================================================