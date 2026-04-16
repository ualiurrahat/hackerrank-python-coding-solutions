# =============================================================================
# Problem  : Set .intersection() Operation
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
#
# Problem Statement:
#   Given two sets of student roll numbers — one for English newspaper
#   subscribers and one for French newspaper subscribers — find the total
#   number of students who have subscribed to BOTH newspapers.
#   Only students present in both sets should be counted.
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
#   A single integer — the total number of students subscribed to both
#   newspapers (i.e. the size of the intersection of both sets).
#
# Sample Input:
#   9
#   1 2 3 4 5 6 7 8 9
#   9
#   10 1 2 3 11 21 55 6 8
#
# Sample Output:
#   5
#
# Explanation:
#   English set     : {1, 2, 3, 4, 5, 6, 7, 8, 9}
#   French  set     : {10, 1, 2, 3, 11, 21, 55, 6, 8}
#   Intersection    : {1, 2, 3, 6, 8} → size = 5
#   Only roll numbers present in BOTH sets are included in the result.
#
# Approach:
#   Convert both inputs into Python sets, then apply the & (intersection)
#   operator. The resulting set contains only elements common to both sets.
#   The answer is the length of the intersection set.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-16
# =============================================================================

#!/bin/python3


# =============================================================================
# Solution: Set Intersection with & Operator
# =============================================================================
# Core Concept — Set Intersection:
#   The intersection of two sets A and B is the set of all elements that
#   belong to BOTH A and B simultaneously. Elements present in only one
#   set are excluded from the result.
#
#   Two equivalent ways to compute intersection in Python:
#     A.intersection(B)  — method form; B can be any iterable
#     A & B              — operator form; both operands must be sets
#
#   Contrast with union (A | B) which includes elements from either set —
#   intersection (A & B) is stricter: only shared elements survive.
#
# Relationship to the previous Union problem (file 05):
#   Union       (A | B) → students in English OR  French (at least one)
#   Intersection(A & B) → students in English AND French (both)
#   The input format is identical; only the set operation changes.
#
# map(int, input().split()):
#   - input()        : reads the raw input line as a string
#   - .split()       : splits the string on whitespace → list of strings
#   - map(int, ...)  : lazily converts each string token to an integer
#   - set(...)       : collects all integers into a set, removing duplicates
#
# Time Complexity : O(min(n, m)) — Python's set intersection iterates over
#                  the smaller set and checks membership in the larger one.
#                  Building each set is O(n) and O(m) respectively.
# Space Complexity: O(min(n, m)) — the intersection is at most the size of
#                  the smaller input set.
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
# Step 3: Compute the intersection and print its size.
# The & operator returns a new set containing only elements present in BOTH
# english and french. len() gives the count of those shared students.
# -----------------------------------------------------------------------------
print(len(english & french))


# =============================================================================
# Key Concepts Covered:
#   - Set intersection   : The set of elements common to two or more sets.
#                          Only elements present in ALL operand sets survive.
#
#   - A & B              : Set intersection operator. Returns a new set with
#                          only the elements found in both A and B.
#                          Both A and B must be sets for & to work.
#
#   - A.intersection(B)  : Method form of intersection. More flexible than &
#                          because B can be any iterable (list, tuple, etc.),
#                          not just a set.
#                          e.g. {1,2,3}.intersection([2,3,4]) → {2,3}
#
# Set Operations — Side-by-Side Comparison:
#   Operation            │ Operator │ Method              │ Meaning
#   ─────────────────────┼──────────┼─────────────────────┼──────────────────
#   Union                │ A | B    │ A.union(B)          │ in A or B
#   Intersection         │ A & B    │ A.intersection(B)   │ in A and B
#   Difference           │ A - B    │ A.difference(B)     │ in A but not B
#   Symmetric Difference │ A ^ B    │ A.symmetric_diff(B) │ in A or B, not both
#
# & vs .intersection() — Key Difference:
#   Expression              │ B type allowed  │ Example
#   ────────────────────────┼─────────────────┼──────────────────────────────
#   A & B                   │ set only        │ {1,2,3} & {2,3,4} → {2,3}
#   A.intersection(B)       │ any iterable    │ {1,2,3}.intersection([2,3,4])
#   A.intersection(B, C)    │ any iterables   │ supports multiple arguments
#
# Reading Space-Separated Integers — Idiomatic Pattern:
#   set(map(int, input().split()))
#     input()        → '1 2 3 4 5'
#     .split()       → ['1', '2', '3', '4', '5']
#     map(int, ...)  → map object yielding 1, 2, 3, 4, 5
#     set(...)       → {1, 2, 3, 4, 5}
# =============================================================================