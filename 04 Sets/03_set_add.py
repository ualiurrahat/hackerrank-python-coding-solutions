# =============================================================================
# Problem  : Set .add()
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
#
# Problem Statement:
#   Given n country stamps (with possible duplicates), find the total number
#   of distinct country stamps using the set .add() operation.
#
# Input Format:
#   - First line    : An integer n — the total number of stamps.
#   - Next n lines  : The name of the country for each stamp.
#
# Constraints:
#   - 0 < n ≤ 1000
#
# Output Format:
#   Print the total number of distinct country stamps on a single line.
#
# Sample Input:
#   7
#   UK
#   China
#   USA
#   France
#   New Zealand
#   UK
#   France
#
# Sample Output:
#   5
#
# Explanation:
#   UK and France each appear twice — duplicates are ignored by the set.
#   Distinct stamps → {UK, China, USA, France, New Zealand} → count = 5
#
# Approach:
#   Initialize an empty set and use set.add() to insert each country name
#   one by one. Since sets automatically reject duplicates, only unique
#   country names are retained. The final count is given by len(set).
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

    # Read the total number of stamps from stdin.
    n = int(input())

    # Initialize an empty set to store unique country names.
    # A set is chosen here because it automatically handles duplicates —
    # adding an already-existing element leaves the set unchanged.
    my_set = set()

    # ------------------------------------------------------------------
    # Read Each Stamp and Add to Set
    # ------------------------------------------------------------------

    # The _ is a throwaway variable — we only need the iteration count,
    # not the loop index value itself.
    for _ in range(n):

        # Read one country name per line and add it to the set.
        # set.add(element) inserts the element if it doesn't exist yet.
        # If the element already exists, the set is unchanged and None
        # is returned — no error, no duplicate stored.
        # e.g. adding 'UK' twice → set stores 'UK' only once.
        my_set.add(input())

    # ------------------------------------------------------------------
    # Print the Count of Distinct Stamps
    # ------------------------------------------------------------------

    # len(set) returns the number of unique elements currently in the set.
    # Since duplicates were never stored, this gives the distinct count.
    print(len(my_set))


# =============================================================================
# Key Concepts Covered:
#   - set.add(e)     : Adds element e to the set if not already present.
#                      If e already exists, the set is unchanged.
#                      Always returns None — do not assign its result.
#                      e.g. s.add('UK') on {'UK'} → {'UK'} (unchanged)
#   - set()          : Initializes an empty set. Note: {} creates an empty
#                      DICT, not a set — always use set() for an empty set.
#   - len(set)       : Returns the number of unique elements in the set.
#   - _ (throwaway)  : Convention for an unused loop variable. Used when
#                      only the iteration count matters, not the index.
#
# Important — Empty Set vs Empty Dict:
#   my_set  = set()   → empty SET   ✅ correct
#   my_dict = {}      → empty DICT  ❌ NOT a set
#   Always use set() to initialize an empty set — never use {}.
#
# set.add() vs set.update() — Key Difference:
#   set.add(e)          → adds a SINGLE element to the set.
#                         e.g. s.add('UK')         → adds the string 'UK'
#                         e.g. s.add(['UK','USA'])  → TypeError! lists are
#                              unhashable and cannot be added as a single element.
#   set.update(iter)    → adds ALL elements from an iterable to the set.
#                         e.g. s.update(['UK','USA']) → adds 'UK' and 'USA'
#                              as separate elements.
#
# Alternative Solution (one-liner using set comprehension):
#   stamps = {input() for _ in range(n)}
#   print(len(stamps))
#   A set comprehension builds the set directly from the input loop —
#   concise and equally correct.
# =============================================================================