# =============================================================================
# Problem  : Lists
# Domain   : Python
# Sub-Domain: Basic Data Types
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
#
# Problem Statement:
#   Initialize an empty list and perform N commands on it in order.
#   Supported commands:
#     - insert i e : Insert integer e at position i.
#     - print      : Print the current list.
#     - remove e   : Remove the first occurrence of integer e.
#     - append e   : Append integer e to the end of the list.
#     - sort       : Sort the list in ascending order.
#     - pop        : Remove and discard the last element.
#     - reverse    : Reverse the list in place.
#
# Input Format:
#   - First line     : An integer N (number of commands).
#   - Next N lines   : Each line contains one of the commands listed above.
#
# Constraints:
#   - Elements added to the list must be integers.
#
# Output Format:
#   For each `print` command, print the current state of the list on a new line.
#
# Sample Input 0:       Sample Output 0:
#   12                    [6, 5, 10]
#   insert 0 5            [1, 5, 9, 10]
#   insert 1 10           [9, 5, 1]
#   insert 0 6
#   print
#   remove 6
#   append 9
#   append 1
#   sort
#   print
#   pop
#   reverse
#   print
#
# Approach:
#   Read each command and dispatch the appropriate list operation.
#   Two implementations are provided:
#     - Approach 1: if/elif/else chain — explicit and beginner-friendly.
#     - Approach 2: match/case statement — modern Python 3.10+ syntax,
#       cleaner and more scalable for multiple command dispatching.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-31
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the number of commands to process.
    N = int(input())

    # Initialize an empty list to perform all operations on.
    my_list = []

    # ------------------------------------------------------------------
    # Approach 1: if/elif/else Chain (explicit, beginner-friendly)
    # ------------------------------------------------------------------
    # Each command string is compared one by one using conditional branches.
    # parts[0] → command name
    # parts[1] → first argument (index or value, depending on command)
    # parts[2] → second argument (value for insert command only)

    # for _ in range(N):
    #     line = input()
    #     parts = line.split()      # split the line into tokens by whitespace
    #     command = parts[0]        # first token is always the command name
    #
    #     if command == "insert":
    #         index = int(parts[1])     # position to insert at
    #         value = int(parts[2])     # value to insert
    #         my_list.insert(index, value)
    #
    #     elif command == "print":
    #         print(my_list)            # print current state of the list
    #
    #     elif command == "remove":
    #         value = int(parts[1])
    #         my_list.remove(value)     # removes first occurrence of value
    #
    #     elif command == "append":
    #         value = int(parts[1])
    #         my_list.append(value)     # adds value to the end of the list
    #
    #     elif command == "sort":
    #         my_list.sort()            # sorts list in ascending order in-place
    #
    #     elif command == "pop":
    #         my_list.pop()             # removes and discards the last element
    #
    #     else:                         # only remaining command is "reverse"
    #         my_list.reverse()         # reverses the list in-place

    # ------------------------------------------------------------------
    # Approach 2: match/case Statement (Python 3.10+) ✅
    # ------------------------------------------------------------------
    # The match/case statement (introduced in Python 3.10) is Python's
    # version of a switch statement found in other languages like C++ or Java.
    # It matches the value of `command` against each `case` pattern and
    # executes the matching block. `case _:` is the wildcard/default case
    # — it matches anything not caught by the cases above it, equivalent
    # to the `else` branch in an if/elif/else chain.
    # This approach is cleaner, more readable, and scales better when
    # the number of commands grows.

    for _ in range(N):
        line = input()
        queries = line.split()    # split the input line into tokens
        command = queries[0]      # first token is always the command name

        match command:

            case "insert":
                # queries[1] → index, queries[2] → value to insert
                index = int(queries[1])
                value = int(queries[2])
                my_list.insert(index, value)

            case "print":
                # Print the current state of the list as-is.
                print(my_list)

            case "remove":
                # Remove the first occurrence of the given value.
                value = int(queries[1])
                my_list.remove(value)

            case "append":
                # Append the given value to the end of the list.
                value = int(queries[1])
                my_list.append(value)

            case "sort":
                # Sort the list in ascending order in-place.
                my_list.sort()

            case "pop":
                # Remove and discard the last element of the list.
                my_list.pop()

            case _:
                # Wildcard — matches any command not listed above.
                # The only remaining valid command is "reverse".
                my_list.reverse()


# =============================================================================
# Key Concepts Covered:
#   - list.insert(i, e) : Inserts element e at index i, shifting elements right.
#   - list.append(e)    : Adds element e to the END of the list. O(1) operation.
#   - list.remove(e)    : Removes the FIRST occurrence of e. Raises ValueError
#                         if e is not found.
#   - list.sort()       : Sorts the list IN-PLACE in ascending order.
#                         Returns None — do not assign its result to a variable.
#   - list.pop()        : Removes and returns the LAST element. O(1) operation.
#                         Can also pop at index: list.pop(i).
#   - list.reverse()    : Reverses the list IN-PLACE. Returns None.
#   - str.split()       : Splits a string by whitespace into a list of tokens.
#                         e.g. "insert 0 5".split() → ["insert", "0", "5"]
#   - match/case        : Python 3.10+ structural pattern matching.
#                         Cleaner alternative to long if/elif/else chains.
#                         `case _:` is the wildcard/default fallback case.
#
# Approach 1 vs Approach 2 — Comparison:
#   Approach 1 (if/elif/else):
#     + Works in all Python versions (3.x).
#     + Explicit and easy for beginners to follow.
#     - Gets verbose and harder to read with many conditions.
#   Approach 2 (match/case):
#     + Cleaner, more readable, and scalable.
#     + Industry-standard for command dispatching in modern Python.
#     - Requires Python 3.10 or higher.
#     ✅ Preferred in modern professional Python codebases.
#
# Python List Methods Quick Reference:
#   list.append(e)    → Add to end
#   list.insert(i, e) → Insert at index i
#   list.remove(e)    → Remove first occurrence of e
#   list.pop()        → Remove and return last element
#   list.pop(i)       → Remove and return element at index i
#   list.sort()       → Sort in-place (ascending)
#   list.reverse()    → Reverse in-place
#   list.index(e)     → Return index of first occurrence of e
#   list.count(e)     → Count occurrences of e
#   list.clear()      → Remove all elements
# =============================================================================