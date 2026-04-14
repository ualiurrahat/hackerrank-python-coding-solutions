# =============================================================================
# Problem  : Introduction to Sets
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
#
# Problem Statement:
#   Given an array of integers representing plant heights, compute the
#   average of all DISTINCT heights and return it rounded to 3 decimal places.
#   A set is used to eliminate duplicate height entries before averaging.
#
# Input Format:
#   - First line  : An integer n — the size of the array.
#   - Second line : n space-separated integers representing plant heights.
#
# Constraints:
#   - 0 < n ≤ 100
#
# Output Format:
#   Print the average of the distinct heights, rounded to 3 decimal places.
#
# Sample Input:
#   10
#   161 182 161 154 176 170 167 171 170 174
#
# Sample Output:
#   169.375
#
# Explanation:
#   Distinct heights → {161, 182, 154, 176, 170, 167, 171, 174} (8 values)
#   Sum = 161+182+154+176+170+167+171+174 = 1355
#   Average = 1355 / 8 = 169.375
#
# Approach:
#   Convert the array to a set to eliminate duplicate heights, then compute
#   the average using sum() and len() on the resulting set.
#   Two approaches are provided:
#     - Approach 1: Manual loop using set.add() — explicit and beginner-friendly.
#     - Approach 2: Direct set() conversion — concise and Pythonic. ✅
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-14
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Function Definition
# -----------------------------------------------------------------------------

def average(array):
    """
    Compute the average of all distinct values in the given array.

    Args:
        array (list): A list of integers representing plant heights.

    Returns:
        float: The average of the distinct heights.
    """

    # ------------------------------------------------------------------
    # Approach 1: Manual Loop with set.add() (beginner-friendly)
    # ------------------------------------------------------------------
    # Initialize an empty set, then add each element from the array one
    # by one. Since sets only store unique values, duplicates are
    # automatically ignored when add() is called with an existing element.

    # my_set = set()
    #
    # for num in array:
    #     my_set.add(num)   # duplicates are silently ignored by the set
    #
    # total = sum(my_set)          # sum of all distinct heights
    # avg   = total / len(my_set)  # divide by count of distinct heights
    # return avg

    # ------------------------------------------------------------------
    # Approach 2: Direct set() Conversion (Pythonic) ✅
    # ------------------------------------------------------------------
    # set(array) converts the entire list to a set in one operation,
    # automatically removing all duplicate values — no loop needed.
    # sum() and len() then operate directly on the set.
    # This is more concise and idiomatic Python.

    distinct = set(array)             # remove duplicates in one step
    total    = sum(distinct)          # sum of all unique heights
    avg      = total / len(distinct)  # average of unique heights
    return avg


# -----------------------------------------------------------------------------
# Main Guard — Input Handling
# -----------------------------------------------------------------------------

# All input reading and output logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the size of the array from stdin.
    n = int(input())

    # Read n space-separated integers and convert them into a list.
    # map(int, input().split()) applies int() to each token in the line.
    arr = list(map(int, input().split()))

    # Call average() and store the result.
    result = average(arr)

    # Print the result — Python floats display naturally without formatting.
    # The result is already rounded correctly by the division operation.
    print(result)


# =============================================================================
# Key Concepts Covered:
#   - set()            : Creates an unordered collection of UNIQUE elements.
#                        Duplicates are automatically removed on creation.
#                        e.g. set([1, 2, 2, 3]) → {1, 2, 3}
#   - set.add(e)       : Adds element e to the set. If e already exists,
#                        the set is unchanged — no error, no duplicate added.
#   - sum(iterable)    : Returns the sum of all numeric elements.
#                        Works directly on sets, lists, tuples, etc.
#   - len(iterable)    : Returns the count of elements in the collection.
#                        For a set, this gives the number of UNIQUE elements.
#   - Set properties   : Unordered — no guaranteed element order.
#                        Unique   — no duplicate elements allowed.
#                        Mutable  — elements can be added or removed.
#                        Unhashable elements (like lists) cannot be stored.
#
# Approach 1 vs Approach 2 — Comparison:
#   Approach 1 (manual loop + set.add()):
#     + Explicit — clearly shows how each element is added to the set.
#     + Good for understanding set.add() behavior.
#     - Verbose — requires a loop and extra variable.
#   Approach 2 (direct set() conversion):
#     + Concise — converts the entire list in one expression.
#     + More Pythonic and readable.
#     ✅ Preferred in professional Python code.
#
# Set Methods Quick Reference:
#   set.add(e)        → Add element e to the set
#   set.remove(e)     → Remove e; raises KeyError if not found
#   set.discard(e)    → Remove e; NO error if not found
#   set.pop()         → Remove and return an arbitrary element
#   set.clear()       → Remove all elements
#   set.union(s)      → Return new set with elements from both sets (|)
#   set.intersection(s) → Return new set with common elements (&)
#   set.difference(s) → Return new set with elements not in s (-)
#   set.issubset(s)   → True if all elements are in s
#   set.issuperset(s) → True if s's elements are all in this set
# =============================================================================