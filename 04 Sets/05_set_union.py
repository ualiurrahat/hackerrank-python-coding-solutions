# =============================================================================
# Problem  : Set .union() Operation
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
#
# Problem Statement:
#   Given two sets of student roll numbers — one for English newspaper
#   subscribers and one for French newspaper subscribers — find the total
#   number of students who have subscribed to at least one newspaper.
#   A student present in both sets must be counted only once.
#
# Input Format:
#   Line 1: Integer n — number of English newspaper subscribers.
#   Line 2: n space-separated roll numbers (English subscribers).
#   Line 3: Integer b — number of French newspaper subscribers.
#   Line 4: b space-separated roll numbers (French subscribers).
#
# Constraints:
#   - 0 < Total number of students in English set <= 1000
#   - 0 < Total number of students in French  set <= 1000
#
# Output Format:
#   A single integer — the total number of students with at least one
#   subscription (i.e. the size of the union of both sets).
#
# Sample Input:
#   9
#   1 2 3 4 5 6 7 8 9
#   9
#   10 1 2 3 11 21 55 6 8
#
# Sample Output:
#   13
#
# Explanation:
#   English set : {1, 2, 3, 4, 5, 6, 7, 8, 9}
#   French  set : {10, 1, 2, 3, 11, 21, 55, 6, 8}
#   Union       : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 55} → size = 13
#   Roll numbers 1, 2, 3, 6, 8 appear in both sets but are counted only once.
#
# Approach:
#   Convert both inputs into Python sets, then apply the | (union) operator.
#   Sets automatically eliminate duplicates, so students in both sets are
#   counted exactly once. The answer is simply the length of the union set.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-15
# =============================================================================

#!/bin/python3


# =============================================================================
# Solution: Set Union with | Operator
# =============================================================================
# Core Concept — Set Union:
#   The union of two sets A and B is the set of all elements that belong to
#   A, or B, or both. Duplicate elements are included only once.
#
#   Two equivalent ways to compute union in Python:
#     A.union(B)  — method form; also accepts any iterable (list, tuple, etc.)
#     A | B       — operator form; both operands must be sets
#
#   For this problem, both give the same result since our inputs are sets.
#   The | operator is used here for conciseness and readability.
#
# map(int, input().split()):
#   - input()        : reads the raw input line as a string
#   - .split()       : splits the string on whitespace → list of strings
#   - map(int, ...)  : lazily converts each string token to an integer
#   - set(...)       : collects all integers into a set, removing duplicates
#
#   This single expression replaces a manual loop + list + conversion step,
#   and is the idiomatic Python pattern for reading space-separated integers.
#
# Why sets and not lists?
#   Lists allow duplicates and require O(n) lookup. Sets use hash tables,
#   giving O(1) average lookup and automatic duplicate elimination — exactly
#   what "count each student only once" requires.
#
# Time Complexity : O(n + b) — building each set is O(n) and O(b); the union
#                  operation itself is O(n + b) in the worst case.
# Space Complexity: O(n + b) — both sets are stored; union is at most O(n + b).
# =============================================================================


# -----------------------------------------------------------------------------
# Step 1: Read the count and roll numbers for English newspaper subscribers.
# The count n is read but not used directly — the set is built from the rolls.
# -----------------------------------------------------------------------------
n = int(input())

# Read n space-separated roll numbers, convert each to int, store as a set.
# Using set() ensures any accidental duplicate roll numbers are removed upfront.
english = set(map(int, input().split()))

# -----------------------------------------------------------------------------
# Step 2: Read the count and roll numbers for French newspaper subscribers.
# -----------------------------------------------------------------------------
b = int(input())

# Same pattern as above — read, split, convert to int, store as a set.
french = set(map(int, input().split()))

# -----------------------------------------------------------------------------
# Step 3: Compute the union and print its size.
# The | operator returns a new set containing all unique elements from both
# sets. len() on the result gives the total number of unique students.
# -----------------------------------------------------------------------------
print(len(english | french))


# =============================================================================
# Key Concepts Covered:
#   - set()              : An unordered collection of unique elements.
#                          Automatically removes duplicates on insertion.
#                          Backed by a hash table — O(1) average lookup.
#
#   - A | B              : Set union operator. Returns a new set with all
#                          elements from A and B combined, each counted once.
#                          Both A and B must be sets for | to work.
#
#   - A.union(B)         : Method form of union. More flexible than | because
#                          B can be any iterable (list, tuple, string, etc.),
#                          not just a set.
#                          e.g. {1,2,3}.union([3,4,5]) → {1,2,3,4,5}
#
#   - map(int, iterable) : Lazily applies int() to every element of the
#                          iterable. Returns a map object (consumed once).
#                          Wrapping in set() collects and deduplicates results.
#
#   - input().split()    : Reads a line and splits on whitespace into a list
#                          of string tokens. The idiomatic way to read
#                          space-separated values from stdin in Python.
#
# Set Union vs | Operator:
#   Expression              │ B type allowed  │ Example
#   ────────────────────────┼─────────────────┼──────────────────────────
#   A | B                   │ set only        │ {1,2} | {2,3} → {1,2,3}
#   A.union(B)              │ any iterable    │ {1,2}.union([2,3]) → {1,2,3}
#   A.union(B, C, D)        │ any iterables   │ supports multiple arguments
#
# Reading Space-Separated Integers — Idiomatic Pattern:
#   set(map(int, input().split()))
#     input()        → '1 2 3 4 5'
#     .split()       → ['1', '2', '3', '4', '5']
#     map(int, ...)  → map object yielding 1, 2, 3, 4, 5
#     set(...)       → {1, 2, 3, 4, 5}
# =============================================================================