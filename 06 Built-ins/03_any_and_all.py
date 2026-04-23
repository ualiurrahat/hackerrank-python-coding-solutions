# =============================================================================
# Problem  : any() and all()
# Domain   : Python
# Sub-Domain: Built-ins
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
#
# Problem Statement:
#   Given a space separated list of integers, check two conditions:
#     1. All integers in the list are positive.
#     2. At least one integer in the list is a palindromic integer.
#   Print True if both conditions are satisfied. Otherwise, print False.
#
# Input Format:
#   Line 1: Integer n — total number of integers in the list.
#   Line 2: n space-separated integers.
#
# Constraints:
#   - 0 < n < 100
#
# Output Format:
#   Print True if all integers are positive AND any integer is a palindrome.
#   Otherwise, print False.
#
# Sample Input:
#   5
#   12 9 61 5 14
#
# Sample Output:
#   True
#
# Explanation:
#   Condition 1: 12, 9, 61, 5, 14 — all are positive.              ✅
#   Condition 2: 9 → '9' == '9' ✅, 5 → '5' == '5' ✅ — palindromes exist.
#   Both conditions satisfied → True.
#
# Approach:
#   Two solutions are presented:
#     1. Explicit function approach — manually checks each condition with
#                                     a helper function for palindrome check
#     2. Pythonic one-liner        — combines all() and any() with generator
#                                    expressions and a reverse slice in one line
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-09
# =============================================================================

#!/bin/python3


# =============================================================================
# Solution 1: Explicit Function Approach
# =============================================================================
# Strategy:
#   Break the problem into two clearly named helper checks, then combine them.
#   This mirrors how you would approach it in C++ — explicit and readable.
#
# Palindrome check without a built-in:
#   Convert the integer to a string, then compare it to its own reverse.
#   str(x)[::-1] uses Python's reverse slice — [::-1] means "step through
#   the string backwards from end to start", producing the reversed string.
#   e.g. str(5)   = '5'   → reversed = '5'   → '5'   == '5'   → True
#   e.g. str(12)  = '12'  → reversed = '21'  → '12'  == '21'  → False
#   e.g. str(121) = '121' → reversed = '121' → '121' == '121' → True
#
# all() with a generator expression:
#   all(x > 0 for x in numbers) checks every element against x > 0.
#   Returns True only if the condition holds for ALL elements.
#   NOTE: all(numbers) > 0 is WRONG — all(numbers) returns a boolean,
#   and comparing a boolean to 0 does not check positivity.
#
# any() with a generator expression:
#   any(isPalindrome(x) for x in numbers) checks each element for palindrome.
#   Returns True as soon as ONE element satisfies the condition (short-circuit).
#   NOTE: any(numbers) == palindrome is WRONG — palindrome is undefined, and
#   any(numbers) returns a boolean, not a number to compare against.
#
# Time Complexity : O(n * d) — n elements, each palindrome check is O(d)
#                  where d is the number of digits in the integer.
# Space Complexity: O(d) — str(x) and its reverse are O(d) per element.
# =============================================================================

def isPalindrome(x):
    # Convert integer to string and compare it with its reverse.
    # [::-1] is the reverse slice — steps through the string backwards.
    # No built-in palindrome function exists; this is the pythonic idiom.
    return str(x) == str(x)[::-1]

def solveExplicit(n, numbers):
    # Condition 1: every element in the list must be strictly positive.
    # Using a generator expression inside all() — checks x > 0 for each x.
    allPositive = all(x > 0 for x in numbers)

    # Condition 2: at least one element must be a palindromic integer.
    # Using a generator expression inside any() — short-circuits on first True.
    anyPalindrome = any(isPalindrome(x) for x in numbers)

    # Both conditions must be True for the final answer to be True.
    return allPositive and anyPalindrome


# =============================================================================
# Solution 2: Pythonic One-Liner (Recommended)
# =============================================================================
# Strategy:
#   Collapse both conditions into a single print() statement using generator
#   expressions directly inside all() and any(). The and operator provides
#   short-circuit evaluation — if all() is False, any() is never executed.
#
# Key techniques:
#   - all(x > 0 for x in numbers)              : True if every x is positive
#   - str(x) == str(x)[::-1]                   : True if x is a palindrome
#   - any(str(x)==str(x)[::-1] for x in numbers): True if any x is palindrome
#   - and                                        : both must be True
#
# The challenge asks for a solution in 3 lines or less — this does it in 1.
#
# Time Complexity : O(n * d) — same as Solution 1.
# Space Complexity: O(d)     — same as Solution 1.
# =============================================================================

def solvePythonic(n, numbers):
    # One line: check all positive AND any palindrome using generator expressions.
    # str(x)[::-1] reverses the string representation of x for palindrome check.
    print(all(x > 0 for x in numbers) and any(str(x) == str(x)[::-1] for x in numbers))


# =============================================================================
# Main Guard
# =============================================================================

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))

    # -----------------------------------------------------------------------
    # Active solution: Solution 2 — Pythonic one-liner.
    # Swap the call below to solveExplicit() to test Solution 1.
    # -----------------------------------------------------------------------
    solvePythonic(n, numbers)


# =============================================================================
# Key Concepts Covered:
#   - all(iterable)      : Returns True if every element of the iterable is
#                          truthy. Returns True for an empty iterable.
#                          e.g. all([1>0, 2>0, 3>0]) → True
#
#   - any(iterable)      : Returns True if at least one element is truthy.
#                          Returns False for an empty iterable.
#                          e.g. any([False, False, True]) → True
#
#   - Generator expression: (expr for x in iterable) passed directly into
#                          all() or any() — evaluated lazily, one element
#                          at a time, without building a full list in memory.
#
#   - str(x)[::-1]       : The idiomatic Python palindrome check.
#                          Converts x to a string, then reverses it using
#                          a slice with step -1. No built-in palindrome exists.
#                          e.g. str(121)[::-1] → '121' → palindrome ✅
#                          e.g. str(12)[::-1]  → '21'  → not palindrome ❌
#
#   - Short-circuit eval : In A and B, if A is False, B is never evaluated.
#                          all() and any() also short-circuit internally:
#                          all() stops at the first False element.
#                          any() stops at the first True element.
#
# Common Mistakes — What NOT to do:
#   all(numbers) > 0              ❌  compares a boolean to 0, not positivity
#   all(numbers > 0)              ❌  can't apply > to a list directly
#   any(numbers) == palindrome    ❌  palindrome is undefined; any() is boolean
#   all(x > 0 for x in numbers)  ✅  correct: generator inside all()
#
# Palindrome Check — Quick Reference:
#   str(x) == str(x)[::-1]
#   x=5   → '5'   == '5'   → True   ✅
#   x=9   → '9'   == '9'   → True   ✅
#   x=12  → '12'  == '21'  → False  ❌
#   x=121 → '121' == '121' → True   ✅
# =============================================================================