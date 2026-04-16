# =============================================================================
# Problem  : Check Subset
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
#
# Problem Statement:
#   Given t test cases, each containing two sets A and B, determine whether
#   set A is a subset of set B. Print True if it is, otherwise print False.
#   A set A is a subset of B if every element of A also exists in B.
#
# Input Format:
#   - First line       : Integer t — the number of test cases.
#   - For each test case:
#       - First line   : Integer a — number of elements in set A.
#       - Second line  : a space-separated integers — elements of set A.
#       - Third line   : Integer b — number of elements in set B.
#       - Fourth line  : b space-separated integers — elements of set B.
#
# Constraints:
#   - 0 < t ≤ 21
#   - 0 < a ≤ 100
#   - 0 < b ≤ 100
#
# Output Format:
#   Print True or False for each test case on a separate line.
#
# Sample Input:
#   3
#   5
#   1 2 3 5 6
#   9
#   9 8 5 6 3 2 1 4 7
#   1
#   2
#   5
#   3 6 5 4 1
#   7
#   1 2 3 5 6 8 9
#   3
#   9 8 2
#
# Sample Output:
#   True
#   False
#   False
#
# Explanation:
#   Test Case 1: A = {1,2,3,5,6}, B = {9,8,5,6,3,2,1,4,7}
#                All elements of A exist in B → True
#   Test Case 2: A = {2}, B = {3,6,5,4,1}
#                2 is not in B → False
#   Test Case 3: A = {1,2,3,5,6,8,9}, B = {9,8,2}
#                1, 3, 5, 6 are not in B → False
#
# Approach:
#   For each test case, read both sets and use set.issubset() to check
#   whether every element of set A exists in set B. Print the result
#   directly as a string "True" or "False".
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-16
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the number of test cases.
    t = int(input())

    # ------------------------------------------------------------------
    # Process Each Test Case
    # ------------------------------------------------------------------

    for _ in range(t):

        # Read the number of elements in set A (used for context;
        # set() handles sizing automatically).
        a = int(input())

        # Read space-separated integers and build set A.
        # map(int, input().split()) converts each token to an integer.
        set_a = set(map(int, input().split()))

        # Read the number of elements in set B.
        b = int(input())

        # Read space-separated integers and build set B.
        set_b = set(map(int, input().split()))

        # --------------------------------------------------------------
        # Check Subset and Print Result
        # --------------------------------------------------------------

        # set.issubset(other) returns True if every element of the calling
        # set exists in `other`. Returns False if even one element is missing.
        # e.g. {1,2,3}.issubset({1,2,3,4,5}) → True
        #      {1,2,6}.issubset({1,2,3,4,5}) → False (6 not in other)
        #
        # Equivalent to the <= operator: set_a <= set_b
        if set_a.issubset(set_b):
            print("True")
        else:
            print("False")


# =============================================================================
# Key Concepts Covered:
#   - set.issubset(s)   : Returns True if every element of the calling set
#                         exists in set s. Returns False otherwise.
#                         Equivalent to the <= operator.
#                         e.g. A.issubset(B)  ↔  A <= B
#   - set.issuperset(s) : The inverse — returns True if the calling set
#                         contains ALL elements of s.
#                         Equivalent to the >= operator.
#                         e.g. B.issuperset(A)  ↔  B >= A
#                         Note: A.issubset(B) == B.issuperset(A) → always True
#   - Multiple test cases: A common HackerRank pattern — read t first,
#                         then loop t times, reading fresh input each iteration.
#
# Subset vs Proper Subset:
#   A.issubset(B)   → True if A ⊆ B  (A is subset — A can equal B)
#   A < B           → True if A ⊂ B  (A is PROPER subset — A cannot equal B)
#   e.g. {1,2} <= {1,2}   → True   (subset, equal sets)
#        {1,2} <  {1,2}   → False  (NOT a proper subset — sets are equal)
#        {1,2} <  {1,2,3} → True   (proper subset — A is strictly smaller)
#
# Subset Operations — Operator Shorthand Quick Reference:
#   A.issubset(B)      ↔  A <= B   (A is subset of B)
#   A.issuperset(B)    ↔  A >= B   (A contains all of B)
#   A < B              →  A is a PROPER subset of B (A ⊆ B and A ≠ B)
#   A > B              →  A is a PROPER superset of B (A ⊇ B and A ≠ B)
#
# Alternative One-liner Solution:
#   print(set_a.issubset(set_b))
#   Python's bool True/False prints as "True"/"False" by default —
#   no if/else needed. Both approaches produce identical output.
# =============================================================================