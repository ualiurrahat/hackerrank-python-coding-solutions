# =============================================================================
# Problem  : String Validators
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
#
# Problem Statement:
#   Given a string s, check whether it contains at least one character of
#   each of the following types and print True or False for each:
#     1. Alphanumeric character (a-z, A-Z, 0-9)
#     2. Alphabetical character (a-z, A-Z)
#     3. Digit                  (0-9)
#     4. Lowercase character    (a-z)
#     5. Uppercase character    (A-Z)
#
# Input Format:
#   A single line containing a string s.
#
# Constraints:
#   - 0 < len(s) ≤ 1000
#
# Output Format:
#   Print five lines — each containing True or False — in the order listed
#   above.
#
# Sample Input:
#   qA2
#
# Sample Output:
#   True
#   True
#   True
#   True
#   True
#
# Explanation:
#   'qA2' contains:
#   - Alphanumeric chars → 'q', 'A', '2'  → True
#   - Alphabetical chars → 'q', 'A'       → True
#   - Digits             → '2'            → True
#   - Lowercase chars    → 'q'            → True
#   - Uppercase chars    → 'A'            → True
#
# Approach:
#   Two approaches are implemented:
#   - Approach 1: Manual loop with boolean flags — explicit and beginner-friendly.
#   - Approach 2: any() with generator expressions — concise and Pythonic. ✅
#   any() returns True if at least one element in the iterable is True,
#   making it a perfect fit for "does the string contain at least one X" checks.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-05
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the input string from stdin.
    s = input()

    # ------------------------------------------------------------------
    # Approach 1: Manual Loop with Boolean Flags (beginner-friendly)
    # ------------------------------------------------------------------
    # Initialize all flags as False — assume no character type is present
    # until proven otherwise by iterating through the string.

    # has_alpha_num = False
    # has_alpha_bet = False
    # has_digit     = False
    # has_lowercase = False
    # has_uppercase = False

    # for char in s:
    #     # Check if the current character is alphanumeric (a-z, A-Z, 0-9).
    #     if char.isalnum():
    #         has_alpha_num = True
    #
    #     # Check if the current character is alphabetical (a-z, A-Z).
    #     if char.isalpha():
    #         has_alpha_bet = True
    #
    #     # Check if the current character is a digit (0-9).
    #     if char.isdigit():
    #         has_digit = True
    #
    #     # Check if the current character is lowercase (a-z).
    #     if char.islower():
    #         has_lowercase = True
    #
    #     # Check if the current character is uppercase (A-Z).
    #     if char.isupper():
    #         has_uppercase = True

    # print(has_alpha_num)
    # print(has_alpha_bet)
    # print(has_digit)
    # print(has_lowercase)
    # print(has_uppercase)

    # ------------------------------------------------------------------
    # Approach 2: any() with Generator Expressions (Pythonic) ✅
    # ------------------------------------------------------------------
    # any(iterable) returns True if AT LEAST ONE element in the iterable
    # evaluates to True — otherwise returns False.
    #
    # A generator expression `func(char) for char in s` produces a sequence
    # of True/False values by applying the validation method to each character.
    # any() short-circuits — it stops as soon as it finds the first True,
    # making it more efficient than iterating the entire string every time.
    #
    # e.g. any(char.isdigit() for char in "qA2")
    #      → checks 'q' (False), 'A' (False), '2' (True) → stops → True

    # Line 1: Does s contain at least one alphanumeric character?
    print(any(char.isalnum() for char in s))

    # Line 2: Does s contain at least one alphabetical character?
    print(any(char.isalpha() for char in s))

    # Line 3: Does s contain at least one digit?
    print(any(char.isdigit() for char in s))

    # Line 4: Does s contain at least one lowercase character?
    print(any(char.islower() for char in s))

    # Line 5: Does s contain at least one uppercase character?
    print(any(char.isupper() for char in s))


# =============================================================================
# Key Concepts Covered:
#   - str.isalnum()  : Returns True if ALL characters are alphanumeric (a-z,
#                      A-Z, 0-9) and the string is not empty. False otherwise.
#   - str.isalpha()  : Returns True if ALL characters are alphabetical (a-z,
#                      A-Z) and the string is not empty. False otherwise.
#   - str.isdigit()  : Returns True if ALL characters are digits (0-9) and
#                      the string is not empty. False otherwise.
#   - str.islower()  : Returns True if ALL cased characters are lowercase and
#                      there is at least one cased character. False otherwise.
#   - str.isupper()  : Returns True if ALL cased characters are uppercase and
#                      there is at least one cased character. False otherwise.
#   - any(iterable)  : Returns True if at least one element in the iterable
#                      is True. Short-circuits on the first True found.
#                      Returns False if the iterable is empty.
#   - all(iterable)  : Counterpart to any(). Returns True only if ALL elements
#                      are True. Short-circuits on the first False found.
#   - Generator expr : `expression for var in iterable` produces values
#                      lazily one at a time — more memory-efficient than
#                      building a full list before passing to any().
#
# any() vs all() — Quick Comparison:
#   any(char.isdigit() for char in "ab1") → True  (at least one digit)
#   all(char.isdigit() for char in "ab1") → False (not all are digits)
#   any(char.isdigit() for char in "abc") → False (no digits at all)
#   all(char.isdigit() for char in "123") → True  (all are digits)
#
# String Validator Methods Quick Reference:
#   s.isalnum()   → True if all chars are alphanumeric (a-z, A-Z, 0-9)
#   s.isalpha()   → True if all chars are alphabetical (a-z, A-Z)
#   s.isdigit()   → True if all chars are digits (0-9)
#   s.islower()   → True if all cased chars are lowercase
#   s.isupper()   → True if all cased chars are uppercase
#   s.isspace()   → True if all chars are whitespace
#   s.istitle()   → True if string is title-cased (e.g. "Hello World")
# =============================================================================