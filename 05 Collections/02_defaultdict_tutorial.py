# =============================================================================
# Problem  : DefaultDict Tutorial
# Domain   : Python
# Sub-Domain: Collections
# Difficulty: Easy
# Score    : 20 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
#
# Problem Statement:
#   Given n words in group A and m words in group B, for each word in group B,
#   print the 1-indexed positions where that word appears in group A.
#   If the word does not appear in group A, print -1.
#
# Input Format:
#   - First line    : Two integers n and m separated by a space.
#   - Next n lines  : One word per line — the words of group A.
#   - Next m lines  : One word per line — the words of group B.
#
# Constraints:
#   - 1 ≤ n ≤ 100
#   - 1 ≤ m ≤ 100
#
# Output Format:
#   Print m lines. Each line contains the 1-indexed positions (space-separated)
#   where the group B word appears in group A, or -1 if it does not appear.
#
# Sample Input:
#   5 2
#   a
#   a
#   b
#   a
#   b
#   a
#   b
#
# Sample Output:
#   1 2 4
#   3 5
#
# Explanation:
#   Group A: ['a', 'a', 'b', 'a', 'b'] (1-indexed positions 1 to 5)
#   Group B: ['a', 'b']
#   'a' appears at positions 1, 2, 4 → print "1 2 4"
#   'b' appears at positions 3, 5   → print "3 5"
#   If a word like 'c' appeared in B but not A → print "-1"
#
# Approach:
#   Use defaultdict(list) to map each word in group A to a list of all
#   1-indexed positions where it appears. For each word in group B,
#   look it up in the defaultdict — if found, print its positions using
#   the * unpacking operator; if not found, print -1.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-18
# =============================================================================

#!/bin/python3

# Import defaultdict from the collections module.
# defaultdict is a dict subclass that automatically assigns a default value
# to any key that is accessed but does not yet exist in the dictionary.
# defaultdict(list) means any missing key gets an empty list [] by default.
from collections import defaultdict


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read n (group A size) and m (group B size) from the first line.
    # map(int, input().split()) unpacks both integers in one expression.
    n, m = map(int, input().split())

    # ------------------------------------------------------------------
    # Build the Position Index for Group A
    # ------------------------------------------------------------------

    # Initialize a defaultdict with list as the default factory.
    # When a new key is accessed, it automatically gets an empty list [].
    # This avoids manual key existence checks before appending.
    # e.g. d['a'].append(1) works even if 'a' has never been added before.
    d = defaultdict(list)

    # Read each word in group A and record its 1-indexed position.
    # range(1, n+1) starts at 1 to produce 1-based indices directly.
    for i in range(1, n + 1):
        word = input()

        # Append the current 1-indexed position to this word's list.
        # If the word is new, defaultdict creates an empty list first,
        # then appends — no KeyError, no manual initialization needed.
        # e.g. after reading 'a' at positions 1, 2, 4:
        #      d['a'] = [1, 2, 4]
        d[word].append(i)

    # ------------------------------------------------------------------
    # Query Each Word in Group B
    # ------------------------------------------------------------------

    for _ in range(m):
        word = input()

        # Check if the word from group B exists in the index built from A.
        if word in d:
            # * (unpacking operator) expands the list into separate arguments
            # for print(), which then prints them space-separated on one line.
            # e.g. print(*[1, 2, 4]) → "1 2 4"
            # This is cleaner than " ".join(map(str, d[word])).
            print(*d[word])
        else:
            # Word not found in group A — print -1 as specified.
            print(-1)


# =============================================================================
# Key Concepts Covered:
#   - defaultdict(list): A dict subclass that returns an empty list []
#                        for any missing key instead of raising a KeyError.
#                        The argument (list, int, set, etc.) is the
#                        "default factory" — called with no args to produce
#                        the default value for new keys.
#   - Default factory  : defaultdict(list)  → missing key gets []
#                        defaultdict(int)   → missing key gets 0
#                        defaultdict(set)   → missing key gets set()
#                        defaultdict(str)   → missing key gets ""
#   - * unpacking      : print(*iterable) expands the iterable into
#                        separate positional arguments for print().
#                        e.g. print(*[1,2,4]) → prints "1 2 4"
#                        Equivalent to print(1, 2, 4).
#   - 1-based indexing : range(1, n+1) generates 1 to n inclusive —
#                        used here to store positions as the problem
#                        requires 1-indexed output, not 0-indexed.
#   - `in` operator    : `word in d` checks if the key exists in the
#                        defaultdict WITHOUT creating a default entry.
#                        This is important — using d[word] directly on
#                        a missing key would create an empty list entry.
#
# defaultdict vs Regular dict — Key Difference:
#   Regular dict:
#     d = {}
#     d['a'].append(1)   → KeyError: 'a' (key doesn't exist yet)
#     d.setdefault('a', []).append(1)  → works, but verbose
#   defaultdict:
#     d = defaultdict(list)
#     d['a'].append(1)   → works instantly, no check needed ✅
#
# Important — Avoid Accidental Key Creation:
#   Accessing a missing key in a defaultdict CREATES that key with the
#   default value. Use `key in d` to check existence WITHOUT creating it.
#   e.g. d['missing']      → creates d['missing'] = []  ⚠️
#        'missing' in d    → returns False, no side effect ✅
# =============================================================================