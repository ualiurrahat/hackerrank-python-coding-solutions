# =============================================================================
# Problem  : Set .difference() Operation
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
#
# Problem Statement:
#   Given two sets of student roll numbers — one for English newspaper
#   subscribers and one for French newspaper subscribers — find the total
#   number of students who have subscribed to the English newspaper ONLY.
#   Students who have subscribed to both newspapers must NOT be counted.
#
# Input Format:
#   Line 1: Integer n — number of English newspaper subscribers.
#   Line 2: n space-separated roll numbers (English subscribers).
#   Line 3: Integer m — number of French newspaper subscribers.
#   Line 4: m space-separated roll numbers (French subscribers).
#
# Constraints:
#   - 0 < Total number of students in English set <= 1000
#   - 0 < Total number of students in French  set <= 1000
#
# Output Format:
#   A single integer — the total number of students subscribed to the
#   English newspaper only (i.e. the size of english - french).
#
# Sample Input:
#   9
#   1 2 3 4 5 6 7 8 9
#   9
#   10 1 2 3 11 21 55 6 8
#
# Sample Output:
#   4
#
# Explanation:
#   English set     : {1, 2, 3, 4, 5, 6, 7, 8, 9}
#   French  set     : {10, 1, 2, 3, 11, 21, 55, 6, 8}
#   Intersection    : {1, 2, 3, 6, 8}  ← subscribed to both (excluded)
#   Difference      : {4, 5, 7, 9}     ← English only → size = 4
#
# Approach:
#   Convert both inputs into Python sets, then apply the - (difference)
#   operator. The result contains only elements present in english but
#   absent from french. The answer is the length of that difference set.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-16
# =============================================================================

#!/bin/python3


# =============================================================================
# Solution: Set Difference with - Operator
# =============================================================================
# Core Concept — Set Difference:
#   The difference of set A and set B (written A - B) is the set of all
#   elements that belong to A but do NOT belong to B. Elements shared
#   between A and B are stripped away from the result.
#
#   Two equivalent ways to compute difference in Python:
#     A.difference(B)  — method form; B can be any iterable
#     A - B            — operator form; both operands must be sets
#
#   Important: difference is NOT symmetric.
#     A - B  gives elements in A but not B  (English only)
#     B - A  gives elements in B but not A  (French only)
#   The order of operands determines which set is being "subtracted from".
#
# Relationship to previous problems in this section:
#   Union        (A | B) → in English OR  French         (file 05)
#   Intersection (A & B) → in English AND French         (file 07)
#   Difference   (A - B) → in English but NOT in French  (this file)
#
# map(int, input().split()):
#   - input()        : reads the raw input line as a string
#   - .split()       : splits the string on whitespace → list of strings
#   - map(int, ...)  : lazily converts each string token to an integer
#   - set(...)       : collects all integers into a set, removing duplicates
#
# Time Complexity : O(n) — iterates over the english set and checks each
#                  element against the french set (O(1) hash lookup per check).
#                  Building each set is O(n) and O(m) respectively.
# Space Complexity: O(n) — the difference set is at most the size of english.
# =============================================================================


# -----------------------------------------------------------------------------
# Step 1: Read the count and roll numbers for English newspaper subscribers.
# The count n is read but not used directly — the set is built from the rolls.
# -----------------------------------------------------------------------------
n = int(input())

# Read n space-separated roll numbers, convert each to int, store as a set.
english = set(map(int, input().split()))

# -----------------------------------------------------------------------------
# Step 2: Read the count and roll numbers for French newspaper subscribers.
# -----------------------------------------------------------------------------
m = int(input())

# Same pattern — read, split, convert to int, store as a set.
french = set(map(int, input().split()))

# -----------------------------------------------------------------------------
# Step 3: Compute the difference and print its size.
# english - french returns a new set of roll numbers that exist in english
# but are absent from french — exactly the "English only" subscribers.
# len() gives the count of those students.
# -----------------------------------------------------------------------------
print(len(english - french))


# =============================================================================
# Key Concepts Covered:
#   - Set difference     : The set of elements in A that are not in B.
#                          Shared elements are removed from the result.
#                          A - B ≠ B - A (order matters).
#
#   - A - B              : Set difference operator. Returns a new set with
#                          elements found in A but not in B.
#                          Both A and B must be sets for - to work.
#
#   - A.difference(B)    : Method form of difference. More flexible than -
#                          because B can be any iterable (list, tuple, etc.),
#                          not just a set.
#                          e.g. {1,2,3}.difference([2,3,4]) → {1}
#
# Non-Symmetry of Difference — Critical Distinction:
#   english = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#   french  = {10, 1, 2, 3, 11, 21, 55, 6, 8}
#
#   english - french  → {4, 5, 7, 9}        English only subscribers
#   french  - english → {10, 11, 21, 55}     French  only subscribers
#
#   Swapping operands gives a completely different (and wrong) answer here.
#   Always verify which set is the "source" and which is being "subtracted".
#
# Set Operations — Full Reference (built across files 05, 07, 08):
#   Operation            │ Operator │ Method              │ Meaning
#   ─────────────────────┼──────────┼─────────────────────┼──────────────────
#   Union                │ A | B    │ A.union(B)          │ in A or B
#   Intersection         │ A & B    │ A.intersection(B)   │ in A and B
#   Difference           │ A - B    │ A.difference(B)     │ in A but not B
#   Symmetric Difference │ A ^ B    │ A.symmetric_diff(B) │ in A or B not both
#
# - vs .difference() — Key Difference:
#   Expression              │ B type allowed  │ Example
#   ────────────────────────┼─────────────────┼──────────────────────────────
#   A - B                   │ set only        │ {1,2,3} - {2,3,4} → {1}
#   A.difference(B)         │ any iterable    │ {1,2,3}.difference([2,3,4])
#   A.difference(B, C)      │ any iterables   │ supports multiple arguments
#
# Reading Space-Separated Integers — Idiomatic Pattern:
#   set(map(int, input().split()))
#     input()        → '1 2 3 4 5'
#     .split()       → ['1', '2', '3', '4', '5']
#     map(int, ...)  → map object yielding 1, 2, 3, 4, 5
#     set(...)       → {1, 2, 3, 4, 5}
# =============================================================================