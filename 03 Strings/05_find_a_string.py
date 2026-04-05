# =============================================================================
# Problem  : Find a String
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
#
# Problem Statement:
#   Given a string and a substring, count and print the number of times
#   the substring occurs in the string. Overlapping occurrences are counted.
#   String traversal goes from left to right. Letters are case-sensitive.
#
# Input Format:
#   - First line  : The original string.
#   - Second line : The substring to search for.
#
# Constraints:
#   - Each character in the string is an ASCII character.
#
# Output Format:
#   Print the total number of occurrences of the substring in the string.
#
# Sample Input:
#   ABCDCDC
#   CDC
#
# Sample Output:
#   2
#
# Explanation:
#   Searching "CDC" in "ABCDCDC":
#   - Index 2: "ABCDCDC"[2:5] = "CDC" ✅ → count = 1
#   - Index 4: "ABCDCDC"[4:7] = "CDC" ✅ → count = 2
#   The two occurrences overlap at index 4, which is correctly counted.
#
# Approach:
#   Use a sliding window of size len(sub_string) and slide it one character
#   at a time from left to right across the string. At each position i,
#   extract the slice string[i : i + len(sub_string)] and compare it to
#   the substring. If they match, increment the counter.
#   This approach correctly handles overlapping occurrences — something
#   Python's built-in str.count() does NOT handle.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-02
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Function Definition
# -----------------------------------------------------------------------------

def count_substring(string, sub_string):
    """
    Count the number of times sub_string occurs in string,
    including overlapping occurrences.

    Args:
        string     (str): The original string to search within.
        sub_string (str): The substring to search for.

    Returns:
        int: The total count of occurrences of sub_string in string.
    """

    # Initialize a counter to track the number of substring matches found.
    count = 0

    # Slide a window of size len(sub_string) across the entire string,
    # one character at a time, from index 0 to len(string) - 1.
    for i in range(0, len(string)):

        # Extract a slice of the string starting at index i with the same
        # length as sub_string:
        #   string[i : i + len(sub_string)]
        # e.g. string = "ABCDCDC", sub_string = "CDC", i = 2
        #      string[2 : 2+3] = string[2:5] = "CDC" ✅
        #
        # Note: len(sub_string) + i is equivalent to i + len(sub_string).
        # The order of addition does not affect the result.
        if string[i : len(sub_string) + i] == sub_string:
            count += 1    # match found — increment the counter

    return count


# -----------------------------------------------------------------------------
# Main Guard — Input Handling
# -----------------------------------------------------------------------------

# All input reading and output logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the original string from stdin.
    # .strip() removes any leading/trailing whitespace or newline characters.
    string = input().strip()

    # Read the substring to search for from stdin.
    sub_string = input().strip()

    # Call count_substring() and store the result.
    count = count_substring(string, sub_string)

    # Print the total number of occurrences found.
    print(count)


# =============================================================================
# Key Concepts Covered:
#   - Sliding window   : A technique where a fixed-size window moves across
#                        a sequence one step at a time. Here the window size
#                        is len(sub_string) and it slides one character at a
#                        time to check every possible position for a match.
#   - String slicing   : string[i:j] extracts characters from index i up to
#                        (but not including) index j. Used here to extract
#                        each window of characters for comparison.
#   - len()            : Returns the number of characters in a string or
#                        elements in any sequence.
#   - range(0, n)      : Generates integers from 0 to n-1. Used to iterate
#                        over every valid starting index in the string.
#   - Overlapping match: This sliding window approach counts overlapping
#                        occurrences correctly. e.g. "CDC" in "ABCDCDC"
#                        finds matches at index 2 AND index 4 (overlapping).
#
# Why NOT use str.count()?
#   Python's built-in str.count(sub) does NOT count overlapping occurrences.
#   e.g. "ABCDCDC".count("CDC") → 1  (misses the overlapping match at index 4)
#   The sliding window approach correctly returns 2 for the same input.
#   Always use the manual sliding window when overlapping matches matter.
#
# str.count() vs Sliding Window — Comparison:
#   Input: string = "ABCDCDC", sub_string = "CDC"
#   str.count()      → 1  ❌ (misses overlapping occurrence)
#   Sliding window   → 2  ✅ (correctly counts both occurrences)
#
# Alternative Built-in (only for non-overlapping cases):
#   count = string.count(sub_string)
#   Simple and concise but INCORRECT when overlapping matches exist.
# =============================================================================