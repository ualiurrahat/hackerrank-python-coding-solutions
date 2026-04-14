# =============================================================================
# Problem  : Symmetric Difference
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
#
# Problem Statement:
#   Given two sets of integers a and b, print their symmetric difference
#   in ascending order, one value per line.
#   Symmetric difference contains values that exist in EITHER a or b,
#   but NOT in both.
#
# Input Format:
#   - First line  : Integer M — size of set a.
#   - Second line : M space-separated integers — elements of set a.
#   - Third line  : Integer N — size of set b.
#   - Fourth line : N space-separated integers — elements of set b.
#
# Constraints:
#   - 0 < M, N ≤ 100
#
# Output Format:
#   Print the symmetric difference integers in ascending order,
#   one per line.
#
# Sample Input:
#   4
#   2 4 5 9
#   4
#   2 4 11 12
#
# Sample Output:
#   5
#   9
#   11
#   12
#
# Explanation:
#   set a = {2, 4, 5, 9}
#   set b = {2, 4, 11, 12}
#   Common elements    → {2, 4}          (excluded from result)
#   Only in a          → {5, 9}          (included)
#   Only in b          → {11, 12}        (included)
#   Symmetric diff     → {5, 9, 11, 12}
#   Sorted ascending   → 5, 9, 11, 12
#
# Approach:
#   Read both sets from stdin using set(map(int, input().split())).
#   Use set.symmetric_difference() to compute the symmetric difference
#   in one built-in call, then sort the result and print each value.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-14
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # ------------------------------------------------------------------
    # Read Set A
    # ------------------------------------------------------------------

    # Read the size of set a (not strictly needed since set() handles
    # duplicates automatically, but provided as part of the input format).
    m = int(input())

    # Read M space-separated integers, convert each to int using map(),
    # and wrap directly in set() to create set a with unique values.
    # e.g. "2 4 5 9" → {2, 4, 5, 9}
    set1 = set(map(int, input().split()))

    # ------------------------------------------------------------------
    # Read Set B
    # ------------------------------------------------------------------

    # Read the size of set b.
    n = int(input())

    # Read N space-separated integers and create set b.
    # e.g. "2 4 11 12" → {2, 4, 11, 12}
    set2 = set(map(int, input().split()))

    # ------------------------------------------------------------------
    # Compute Symmetric Difference
    # ------------------------------------------------------------------

    # set.symmetric_difference(other) returns a NEW set containing all
    # elements that are in EITHER set1 or set2, but NOT in both.
    # This is equivalent to (set1 | set2) - (set1 & set2), or using
    # the ^ operator: set1 ^ set2.
    # e.g. {2,4,5,9}.symmetric_difference({2,4,11,12}) → {5, 9, 11, 12}
    #
    # sorted() converts the set to a sorted list in ascending order —
    # necessary because sets are unordered and have no guaranteed order.
    symm_diff = sorted(set1.symmetric_difference(set2))

    # ------------------------------------------------------------------
    # Print Each Value on a Separate Line
    # ------------------------------------------------------------------

    # Iterate over the sorted result and print each number individually.
    # This produces one value per line as required by the output format.
    for num in symm_diff:
        print(num)


# =============================================================================
# Key Concepts Covered:
#   - set.symmetric_difference(s): Returns a new set of elements that are
#                          in either set but NOT in both — the XOR of two sets.
#                          e.g. {1,2,3}.symmetric_difference({2,3,4}) → {1,4}
#   - ^ operator         : Shorthand for symmetric_difference().
#                          set1 ^ set2 produces the same result.
#   - sorted(set)        : Converts an unordered set into a sorted list.
#                          Required here since sets have no guaranteed order.
#   - set(map(int,...))  : Combines map() and set() to read, convert, and
#                          deduplicate integers from a single input line.
#
# Set Operations — Visual Summary:
#   Given: a = {2, 4, 5, 9}  |  b = {2, 4, 11, 12}
#   ─────────────────────────────────────────────────────────
#   a | b   → union()              → {2, 4, 5, 9, 11, 12}
#   a & b   → intersection()       → {2, 4}
#   a - b   → difference()         → {5, 9}
#   b - a   → difference()         → {11, 12}
#   a ^ b   → symmetric_difference → {5, 9, 11, 12}
#   ─────────────────────────────────────────────────────────
#
# Symmetry of Set Operations:
#   a | b  == b | a    → True   (union is symmetric)
#   a & b  == b & a    → True   (intersection is symmetric)
#   a - b  == b - a    → False  (difference is NOT symmetric)
#   a ^ b  == b ^ a    → True   (symmetric difference IS symmetric)
#
# Operator Shorthand Quick Reference:
#   a.union(b)                  ↔  a | b
#   a.intersection(b)           ↔  a & b
#   a.difference(b)             ↔  a - b
#   a.symmetric_difference(b)   ↔  a ^ b
#   a.issubset(b)               ↔  a <= b
#   a.issuperset(b)             ↔  a >= b
# =============================================================================