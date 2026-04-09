# =============================================================================
# Problem  : Capitalize!
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 20 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
#
# Problem Statement:
#   Given a full name, capitalize the first letter of each word appropriately.
#   Only the very first character of each word should be capitalized.
#   If a word starts with a digit, nothing in that word gets capitalized.
#   Example: '12abc' when capitalized remains '12abc'.
#
# Input Format:
#   A single line containing the full name S.
#
# Constraints:
#   - 0 < len(S) < 1000
#   - The string consists of alphanumeric characters and spaces.
#
# Output Format:
#   Print the correctly capitalized string.
#
# Sample Input : chris alan
# Sample Output: Chris Alan
#
# Approach:
#   Two solutions are presented:
#     1. str.title() approach  — passes most cases but fails on words that
#                                start with digits (e.g. '2r' → '2R' wrongly)
#     2. str.capitalize() + join — correct pythonic solution that only ever
#                                touches the first character of each word
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-09
# =============================================================================

#!/bin/python3

import os


# =============================================================================
# Solution 1: str.title() — Fails Edge Case (Words Starting with Digits)
# =============================================================================
# Strategy:
#   str.title() capitalizes any character that immediately follows a non-letter
#   character (spaces, digits, punctuation). This works correctly for normal
#   words like 'chris' → 'Chris', but breaks for words that start with digits.
#
# Why it fails:
#   title() rule: "capitalize a character if the character before it is NOT
#   a letter." So in '2r', the 'r' comes after '2' (a non-letter) → 'r' gets
#   capitalized → '2R'. But the problem requires '2r' to stay as '2r'.
#
#   "1 2 w 2r 3g".title()  → '1 2 W 2R 3G'   ❌ (wrong for '2r' and '3g')
#   "chris alan".title()   → 'Chris Alan'     ✅ (correct for normal words)
#
# Verdict: Passes most test cases but fails any input containing words that
#          begin with a digit followed by a letter (e.g. '2r', '3g', '12abc').
#
# Time Complexity : O(n) — scans every character in the string once.
# Space Complexity: O(n) — returns a new string of the same length.
# =============================================================================

def solveTitle(s):

    # title() capitalizes after every non-letter — including digits.
    # This is incorrect behavior for words like '2r' → wrongly gives '2R'.
    return s.title()


# =============================================================================
# Solution 2: str.capitalize() + split/join — Correct Pythonic Solution
# =============================================================================
# Strategy:
#   Split the string into individual words, apply str.capitalize() to each
#   word separately, then rejoin them with a single space.
#
# Why str.capitalize() is correct here:
#   capitalize() only ever touches the FIRST character of the string it is
#   called on. If that first character is a letter → uppercase it. If it is
#   a digit or any non-letter → leave the entire word unchanged.
#
#   '2r'.capitalize()    → '2r'    ✅ (first char '2' is not a letter)
#   'chris'.capitalize() → 'Chris' ✅ (first char 'c' is a letter)
#   '12abc'.capitalize() → '12abc' ✅ (first char '1' is not a letter)
#
# Why split(' ') and NOT split():
#   s.split()    — splits on ANY whitespace and collapses multiple spaces.
#                  This would silently destroy extra spaces in the input.
#   s.split(' ') — splits on a SINGLE space character only, preserving the
#                  exact number of spaces as separate empty-string tokens.
#                  Rejoining with ' '.join() then restores the original spacing.
#
# ' '.join(word.capitalize() for word in s.split(' ')):
#   - s.split(' ')           : breaks the string into a list of words on spaces
#   - word.capitalize()      : capitalizes only the first char of each word
#   - generator expression   : lazily applies capitalize() to each word
#   - ' '.join(...)          : stitches the words back together with spaces
#
# Time Complexity : O(n) — split, capitalize, and join each traverse the string.
# Space Complexity: O(n) — the list of words and the result string are O(n).
# =============================================================================

def solve(s):

    # -------------------------------------------------------------------------
    # Split on explicit single space to preserve spacing between words.
    # Apply capitalize() to each word — only the first character is affected.
    # Rejoin with a single space to reconstruct the full name string.
    # -------------------------------------------------------------------------
    return ' '.join(word.capitalize() for word in s.split(' '))


# =============================================================================
# Main Guard
# =============================================================================
# The HackerRank judge writes output to a file path from the environment.
# solve() is the active solution — uses the correct capitalize() approach.
# =============================================================================

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# =============================================================================
# Key Concepts Covered:
#   - str.title()       : Capitalizes any character that follows a non-letter.
#                         Fails for words starting with digits (e.g. '2r'→'2R').
#                         Useful for purely alphabetic text only.
#
#   - str.capitalize()  : Capitalizes ONLY the very first character of the
#                         string. If the first char is not a letter, the entire
#                         string is returned unchanged. Correct for this problem.
#
#   - str.split(' ')    : Splits on a literal single space, preserving all
#                         spacing. Always prefer over split() when the input
#                         may contain multiple consecutive spaces.
#
#   - str.split()       : Splits on any whitespace and collapses multiple
#                         spaces — unsafe when spacing must be preserved.
#
#   - ' '.join(iter)    : Joins an iterable of strings with a space separator.
#                         Combined with a generator, it is memory-efficient.
#
#   - Generator expression: (expr for x in iterable) — applies a transformation
#                         lazily to each element without building a full list.
#
# title() vs capitalize() — Critical Difference:
#   Input     │ .title() │ .capitalize() │ Expected
#   ──────────┼──────────┼───────────────┼─────────
#   'chris'   │ 'Chris'  │ 'Chris'       │ 'Chris'  ✅ both correct
#   '2r'      │ '2R'     │ '2r'          │ '2r'     ❌ title / ✅ capitalize
#   '12abc'   │ '12Abc'  │ '12abc'       │ '12abc'  ❌ title / ✅ capitalize
#   'aBC'     │ 'Abc'    │ 'Abc'         │ 'Abc'    ✅ both correct
#
# split() vs split(' ') — Critical Difference:
#   Input          │ .split()           │ .split(' ')
#   ───────────────┼────────────────────┼──────────────────────
#   'a  b'         │ ['a', 'b']         │ ['a', '', 'b']
#   ' chris alan ' │ ['chris', 'alan']  │ ['', 'chris', 'alan', '']
#   Rejoin result  │ 'a b' (space lost) │ 'a  b' (space preserved)
# =============================================================================