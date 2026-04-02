# =============================================================================
# Problem  : String Split and Join
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
#
# Problem Statement:
#   Given a string of space-separated words, split the string on a space
#   delimiter and then join the resulting list using a hyphen (-).
#
# Input Format:
#   A single line containing a string of space-separated words.
#
# Output Format:
#   Print the string with spaces replaced by hyphens.
#
# Example:
#   "this is a string"  →  "this-is-a-string"
#
# Sample Input 0:
#   this is a string
#
# Sample Output 0:
#   this-is-a-string
#
# Approach:
#   Use str.split(" ") to break the string into a list of words on every
#   space delimiter, then use "-".join() to concatenate the list back into
#   a single string with hyphens as the separator between each word.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-02
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Function Definition
# -----------------------------------------------------------------------------

def split_and_join(line):
    """
    Split a string on spaces and rejoin it using hyphens.

    Args:
        line (str): A string of space-separated words.

    Returns:
        str: The resulting string with spaces replaced by hyphens.
    """

    # Step 1: Split the string on every space character.
    # str.split(" ") breaks the string at each space and returns a list
    # of substrings (words). The space itself is discarded.
    # e.g. "this is a string" → ["this", "is", "a", "string"]
    line = line.split(" ")

    # Step 2: Join the list back into a single string using "-" as separator.
    # "-".join(iterable) places a hyphen between every adjacent pair of
    # elements in the list, producing one continuous string.
    # e.g. ["this", "is", "a", "string"] → "this-is-a-string"
    line = "-".join(line)

    # Return the final hyphen-separated string.
    return line


# -----------------------------------------------------------------------------
# Main Guard — Input Handling
# -----------------------------------------------------------------------------

# All input reading and output logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the input string from stdin.
    line = input()

    # Call split_and_join() and store the returned result.
    result = split_and_join(line)

    # Print the final hyphen-separated string.
    print(result)


# =============================================================================
# Key Concepts Covered:
#   - str.split(sep)   : Splits a string at every occurrence of the separator
#                        `sep` and returns a list of substrings.
#                        The separator itself is NOT included in the results.
#                        e.g. "a b c".split(" ") → ["a", "b", "c"]
#                        If no separator is given, splits on any whitespace
#                        and removes empty strings from the result.
#   - sep.join(iter)   : Concatenates all elements of an iterable into a
#                        single string, placing `sep` between each element.
#                        e.g. "-".join(["a","b","c"]) → "a-b-c"
#                        All elements in the iterable must be strings.
#   - String immutability: Strings cannot be modified in-place. split() and
#                        join() both return NEW string/list objects — the
#                        original string is never changed.
#
# split() vs split(" ") — Important Difference:
#   "a  b".split()    → ["a", "b"]      (splits on ANY whitespace, ignores extras)
#   "a  b".split(" ") → ["a", "", "b"]  (splits strictly on single space,
#                                         empty string included for double space)
#   For this problem, split(" ") is used as specified to split on a single space.
#
# join() Separator Quick Reference:
#   " ".join(["a","b","c"])  → "a b c"      (space)
#   "-".join(["a","b","c"])  → "a-b-c"      (hyphen)
#   "".join(["a","b","c"])   → "abc"         (no separator)
#   ", ".join(["a","b","c"]) → "a, b, c"    (comma-space)
#   "/".join(["a","b","c"])  → "a/b/c"      (slash — useful for paths)
#
# One-liner Alternative:
#   return "-".join(line.split(" "))
#   Both steps combined into a single chained expression.
#   Equally correct — the two-step version above is preferred for clarity.
# =============================================================================