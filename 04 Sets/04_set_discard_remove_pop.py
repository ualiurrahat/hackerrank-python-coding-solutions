# =============================================================================
# Problem  : Set .discard(), .remove() & .pop()
# Domain   : Python
# Sub-Domain: Sets
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
#
# Problem Statement:
#   Given a non-empty set s and N commands (pop, remove, discard),
#   execute each command on the set in order and print the sum of the
#   remaining elements after all commands are applied.
#
# Input Format:
#   - First line  : Integer n — the number of elements in the set.
#   - Second line : n space-separated non-negative integers — elements of s.
#   - Third line  : Integer N — the number of commands.
#   - Next N lines: A command (pop / remove / discard) optionally followed
#                   by a value (remove and discard require a value; pop does not).
#
# Constraints:
#   - 0 < n ≤ 100
#   - 0 < N ≤ 100
#   - All elements are non-negative integers ≤ 9.
#
# Output Format:
#   Print the sum of the remaining elements of the set after all commands.
#
# Sample Input:
#   9
#   1 2 3 4 5 6 7 8 9
#   10
#   pop
#   remove 9
#   discard 9
#   discard 8
#   remove 7
#   pop
#   discard 6
#   remove 5
#   pop
#   discard 5
#
# Sample Output:
#   4
#
# Explanation:
#   After executing all commands, the remaining set is {4}.
#   Sum = 4.
#
# Approach:
#   Read the set and commands from stdin. For each command, dispatch the
#   correct set operation using an if/elif chain. After all commands are
#   processed, compute and print the sum of the remaining elements.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-15
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the number of elements and build the set.
    # map(int, input().split()) converts each space-separated token to int.
    n = int(input())
    s = set(map(int, input().split()))

    # Read the number of commands to execute.
    N = int(input())

    # ------------------------------------------------------------------
    # Process Each Command
    # ------------------------------------------------------------------

    for _ in range(N):

        # Split the input line into tokens.
        # For "pop"        → parts = ["pop"]
        # For "remove 9"   → parts = ["remove", "9"]
        # For "discard 8"  → parts = ["discard", "8"]
        parts = input().split()
        command = parts[0]    # first token is always the command name

        if command == "pop":
            # set.pop() removes and returns an ARBITRARY element from the set.
            # Since sets are unordered, there is no guarantee which element
            # is removed — it is implementation-dependent.
            # Raises KeyError if the set is empty.
            s.pop()

        elif command == "remove":
            # set.remove(x) removes element x from the set.
            # Raises KeyError if x is NOT found in the set.
            # int() converts the string argument to an integer.
            digit = int(parts[1])
            s.remove(digit)

        elif command == "discard":
            # set.discard(x) removes element x from the set.
            # If x is NOT found, it does NOTHING — no KeyError raised.
            # Safer than remove() when the element may not exist in the set.
            digit = int(parts[1])
            s.discard(digit)

    # ------------------------------------------------------------------
    # Print the Sum of Remaining Elements
    # ------------------------------------------------------------------

    # sum() computes the total of all remaining elements in the set.
    total = sum(s)
    print(total)


# =============================================================================
# Key Concepts Covered:
#   - set.pop()      : Removes and returns an ARBITRARY element from the set.
#                      No argument is taken — the element chosen is random.
#                      Raises KeyError if the set is empty.
#   - set.remove(x)  : Removes element x from the set.
#                      Raises KeyError if x does NOT exist in the set.
#                      Use when you are CERTAIN the element exists.
#   - set.discard(x) : Removes element x from the set.
#                      Does NOTHING if x does not exist — no error raised.
#                      Use when the element MAY or MAY NOT be in the set.
#   - sum(set)       : Returns the sum of all numeric elements in the set.
#
# remove() vs discard() — When to Use Which:
#   set.remove(x)  → Use when x MUST exist. Raises KeyError if missing.
#                    Good for catching bugs — forces you to verify the element.
#   set.discard(x) → Use when x MAY or MAY NOT exist. Silent if missing.
#                    Safer for optional cleanup operations.
#
# All Three Removal Methods — Quick Comparison:
#   Method          Argument   Removes         Error if missing?
#   ─────────────────────────────────────────────────────────────
#   set.pop()       none       arbitrary elem  KeyError if set is empty
#   set.remove(x)   value x    specific elem   KeyError if x not found
#   set.discard(x)  value x    specific elem   No error (silent)
#   ─────────────────────────────────────────────────────────────
#
# Note on set.pop() ordering:
#   Since sets are unordered, pop() does not remove the "first" or "last"
#   element — it removes an arbitrary one chosen by the interpreter.
#   Never rely on pop() to remove a specific element from a set.
# =============================================================================