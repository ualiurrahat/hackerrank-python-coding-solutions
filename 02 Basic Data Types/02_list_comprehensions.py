# =============================================================================
# Problem  : List Comprehensions
# Domain   : Python
# Sub-Domain: Basic Data Types
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
#
# Problem Statement:
#   Given three integers x, y, z (cuboid dimensions) and an integer n,
#   print a list of all possible 3D coordinates [i, j, k] where:
#     - 0 ≤ i ≤ x
#     - 0 ≤ j ≤ y
#     - 0 ≤ k ≤ z
#     - i + j + k ≠ n
#   The result must be printed in lexicographic increasing order.
#   Use list comprehensions rather than multiple loops.
#
# Input Format:
#   Four separate lines containing integers x, y, z, and n respectively.
#
# Constraints:
#   Print the list in lexicographic increasing order.
#
# Sample Input 0:        Sample Output 0:
#   x = 1                [[0, 0, 0], [0, 0, 1], [0, 1, 0],
#   y = 1                 [1, 0, 0], [1, 1, 1]]
#   z = 1
#   n = 2
#
# Explanation:
#   All permutations of [i, j, k] where 0 ≤ i,j,k ≤ 1 are generated.
#   Any combination where i + j + k == 2 is excluded (e.g. [0,1,1],
#   [1,0,1], [1,1,0]). The remaining valid coordinates are printed.
#
# Approach:
#   Use a single list comprehension with three nested range() iterators
#   and a conditional filter (if i+j+k != n) to generate all valid
#   coordinates in one concise, readable expression.
#   Since range() iterates in ascending order, the output is naturally
#   in lexicographic (dictionary) order — no sorting needed.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-19
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the three cuboid dimension limits and the filter value n.
    # Each value is on a separate line in stdin.
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # ------------------------------------------------------------------
    # Brute Force Approach (for understanding — using nested loops)
    # ------------------------------------------------------------------
    # The logic below shows how the problem would be solved step-by-step
    # using traditional nested for loops. This is the foundation that
    # the list comprehension below is built upon.
    #
    # values = []
    # for i in range(0, x+1):         # iterate i from 0 to x (inclusive)
    #     for j in range(0, y+1):     # iterate j from 0 to y (inclusive)
    #         for k in range(0, z+1): # iterate k from 0 to z (inclusive)
    #             if i + j + k != n:  # filter out coordinates summing to n
    #                 values.append([i, j, k])  # add valid coordinate
    # print(values)

    # ------------------------------------------------------------------
    # Optimised Approach: List Comprehension (Pythonic)
    # ------------------------------------------------------------------

    # A list comprehension condenses the three nested loops and the
    # conditional filter into a single, readable line.
    #
    # Structure breakdown:
    #   [  expression  |  for loop 1  |  for loop 2  |  for loop 3  |  condition  ]
    #   [ [i, j, k]    | for i in ... | for j in ... | for k in ... | if i+j+k!=n ]
    #
    # - range(x+1) generates integers 0, 1, ..., x (inclusive of x).
    # - The three `for` clauses mirror the three nested loops above.
    # - The `if` clause at the end filters out unwanted coordinates.
    # - Since range() is naturally ascending, output is lexicographically
    #   ordered without any need for an explicit sort.
    values = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    # Print the final list of valid coordinates.
    # Python's default list print format matches the expected output exactly.
    print(values)


# =============================================================================
# Key Concepts Covered:
#   - List comprehension : A concise way to build a list using a single
#                          expression. Syntax:
#                          [expression for var in iterable if condition]
#                          Equivalent to a for loop + append, but faster
#                          and more Pythonic.
#   - Nested comprehension: Multiple `for` clauses in one comprehension
#                          mimic nested loops. Order matters — outer loop
#                          comes first, just like in nested for loops.
#   - Conditional filter : The `if` clause at the end of a comprehension
#                          acts as a filter — only elements satisfying the
#                          condition are included in the result list.
#   - range(x+1)         : Generates [0, 1, ..., x] — note x+1 is needed
#                          to include x, since range() is right-exclusive.
#   - Lexicographic order: Since range() iterates in ascending order,
#                          the output list is naturally sorted — no
#                          explicit sorting step needed.
#
# List Comprehension vs Nested Loop — Performance:
#   List comprehensions are generally faster than equivalent for loops
#   because they are optimised at the CPython interpreter level.
#   They also produce more readable, concise code — a hallmark of
#   idiomatic Python that is widely used in professional codebases.
#
# List Comprehension Quick Reference:
#   [x for x in range(5)]              → [0, 1, 2, 3, 4]
#   [x*2 for x in range(5)]            → [0, 2, 4, 6, 8]
#   [x for x in range(5) if x % 2==0]  → [0, 2, 4]   (filter evens)
#   [[i,j] for i in range(2)
#          for j in range(2)]          → [[0,0],[0,1],[1,0],[1,1]]
# =============================================================================