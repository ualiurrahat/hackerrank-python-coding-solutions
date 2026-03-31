# =============================================================================
# Problem  : Tuples
# Domain   : Python
# Sub-Domain: Basic Data Types
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
#
# Problem Statement:
#   Given an integer n and n space-separated integers, create a tuple of
#   those integers and print the result of hash(tuple).
#
# Input Format:
#   - First line  : An integer n (number of elements).
#   - Second line : n space-separated integers.
#
# Output Format:
#   Print the hash value of the tuple.
#
# Sample Input 0:       Sample Output 0:
#   2                     3713081631934410656
#   1 2
#
# Note on Language Choice — Python 2:
#   This solution is intentionally written in Python 2 due to a known
#   HackerRank platform issue with this specific problem in Python 3.
#   In Python 3, hash() uses a randomised seed (hash randomisation) by
#   default, meaning the hash value changes on every run. This causes
#   the output to differ from the expected value, failing the test cases.
#   In Python 2, hash() produces a deterministic (fixed) result for the
#   same input, which is why the platform's expected output matches only
#   the Python 2 submission. This is a known HackerRank issue and not a
#   flaw in the solution logic itself.
#
# Approach:
#   Read n integers, convert them into a tuple using tuple() and map(),
#   then pass the tuple to hash() and print the result.
#   Tuples are hashable in Python (unlike lists) because they are
#   immutable — their contents cannot change after creation.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-31
# =============================================================================

#!/bin/python


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the number of elements.
    # raw_input() is the Python 2 equivalent of Python 3's input().
    # In Python 2, input() evaluates the expression, while raw_input()
    # safely reads it as a plain string — raw_input() is always preferred.
    n = int(raw_input())

    # Read all integers in one line, split by whitespace, convert each to
    # int using map(), and wrap the result in tuple() to create a tuple.
    # tuple(map(int, ...)) → immutable sequence of integers.
    # e.g. "1 2" → ("1","2") → (1, 2)
    integer_list = tuple(map(int, raw_input().split()))

    # Compute and print the hash of the tuple.
    # hash() is a built-in function — no import needed.
    # It returns a fixed-size integer that uniquely represents the object.
    # Only IMMUTABLE objects (like tuples, strings, ints) are hashable.
    # Lists are NOT hashable because they are mutable (can be changed).
    # In Python 2, hash() is deterministic — same input always gives
    # the same output, which is why this problem requires Python 2.
    print hash(integer_list)


# =============================================================================
# Key Concepts Covered:
#   - tuple()          : Creates an immutable ordered sequence.
#                        Unlike lists, tuples cannot be modified after creation.
#                        Syntax: tuple(iterable) or (e1, e2, e3)
#   - Immutability     : Tuples are immutable — elements cannot be added,
#                        removed, or changed. This makes them hashable.
#   - hash()           : Built-in function that returns an integer hash value
#                        for a given object. Only immutable objects are hashable.
#                        Lists → NOT hashable (mutable)
#                        Tuples → hashable (immutable) ✅
#   - raw_input()      : Python 2's safe way to read a line from stdin as a
#                        plain string. Replaced by input() in Python 3.
#   - Hash randomisation: In Python 3, hash() uses a random seed by default
#                        (set at interpreter startup) for security reasons.
#                        This means hash values differ between runs in Python 3,
#                        making it unsuitable for this specific problem.
#                        Python 2 uses a fixed seed → deterministic hash values.
#
# Tuple vs List — Quick Comparison:
#   Feature         | List          | Tuple
#   ----------------|---------------|------------------
#   Syntax          | [1, 2, 3]     | (1, 2, 3)
#   Mutable         | ✅ Yes        | ❌ No
#   Hashable        | ❌ No         | ✅ Yes
#   Performance     | Slightly slow | Slightly faster
#   Use case        | Dynamic data  | Fixed/constant data
#
# Python 2 vs Python 3 — Key Differences in this problem:
#   Python 2: raw_input() → reads string | input() → evaluates expression
#   Python 3: input()     → reads string | no raw_input()
#   Python 2: print x          (statement, no parentheses needed)
#   Python 3: print(x)         (function, parentheses required)
#   Python 2: hash() is deterministic  → same input = same hash always
#   Python 3: hash() is randomised     → same input = different hash each run
# =============================================================================