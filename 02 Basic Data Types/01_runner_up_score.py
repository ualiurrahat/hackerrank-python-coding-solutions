# =============================================================================
# Problem  : Find the Runner-Up Score
# Domain   : Python
# Sub-Domain: Basic Data Types
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
#
# Problem Statement:
#   Given a list of n scores, find and print the runner-up score —
#   i.e., the second highest unique score in the list.
#
# Input Format:
#   - First line  : An integer n (number of scores).
#   - Second line : n space-separated integers representing the scores.
#
# Constraints:
#   - 2 ≤ n ≤ 10
#   - -100 ≤ score ≤ 100
#
# Output Format: Print the runner-up (second maximum) score.
#
# Sample Input 0:
#   5
#   2 3 6 6 5
#
# Sample Output 0:
#   5
#
# Explanation:
#   The list is [2, 3, 6, 6, 5].
#   Maximum score is 6. After removing duplicates → {2, 3, 5, 6}.
#   Second maximum (runner-up) is 5.
#
# Approach:
#   1. Read n scores from stdin into a list.
#   2. Convert the list to a set to eliminate duplicate scores —
#      because runner-up means the second highest UNIQUE score.
#   3. Sort the unique scores in ascending order.
#   4. Access the second-to-last element (index -2) as the runner-up.
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

    # Read the number of scores from stdin.
    n = int(input())

    # Read all scores in a single line, split by spaces, and convert each
    # to an integer. list() is called immediately on map() to eagerly
    # evaluate the iterator into a usable list object.
    # map(int, input().split()) applies int() to every element produced
    # by split(), which breaks the input string into individual tokens.
    scores_list = list(map(int, input().split()))

    # ------------------------------------------------------------------
    # Find the Runner-Up Score
    # ------------------------------------------------------------------

    # Step 1: Convert the list to a set to remove duplicate scores.
    # A set only stores unique values, so repeated scores are eliminated.
    # e.g. [2, 3, 6, 6, 5] → {2, 3, 5, 6}
    unique_scores = set(scores_list)

    # Step 2: Sort the unique scores in ascending (low → high) order.
    # sorted() returns a new sorted list and does not modify the original.
    # e.g. {2, 3, 5, 6} → [2, 3, 5, 6]
    sorted_scores = sorted(unique_scores)

    # Step 3: Access the runner-up score using index -2.
    # Negative indexing in Python counts from the end of the list:
    #   index -1 → last element      (maximum score)
    #   index -2 → second-to-last    (runner-up score)
    # e.g. [2, 3, 5, 6][-2] → 5
    print(sorted_scores[-2])


# =============================================================================
# Key Concepts Covered:
#   - list()             : Converts an iterable (like map or set) into a list.
#   - map(func, iter)    : Applies a function to every element of an iterable.
#                          Returns a lazy iterator — wrap in list() to evaluate.
#                          e.g. map(int, ["1","2","3"]) → [1, 2, 3]
#   - input().split()    : Reads a line and splits it into a list of strings
#                          by whitespace. e.g. "2 3 6" → ["2", "3", "6"]
#   - set()              : An unordered collection of UNIQUE elements.
#                          Duplicates are automatically removed on creation.
#                          e.g. set([2, 3, 6, 6, 5]) → {2, 3, 5, 6}
#   - sorted()           : Returns a new sorted list from any iterable.
#                          Default order is ascending (low to high).
#                          Does NOT modify the original collection.
#   - Negative indexing  : Python allows indexing from the end of a list.
#                          list[-1] → last item
#                          list[-2] → second-to-last item
#
# Why convert to a set first?
#   Without removing duplicates, the runner-up of [2, 6, 6] would
#   incorrectly return 6 (the duplicate) instead of 2.
#   Converting to a set ensures we find the second highest UNIQUE score.
#
# Alternative Solution (using max() twice):
#   max_score = max(scores_list)
#   runner_up = max(score for score in scores_list if score != max_score)
#   print(runner_up)
#   This finds the maximum, then finds the highest score excluding it.
#   Both approaches are correct — the set+sorted approach is more concise.
# =============================================================================