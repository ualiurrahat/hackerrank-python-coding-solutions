# =============================================================================
# Problem  : Mutations
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
#
# Problem Statement:
#   Given an immutable string, replace the character at a given index
#   with a given character and return the modified string.
#
# Input Format:
#   - First line  : A string s.
#   - Second line : An integer position and a character c, separated by space.
#
# Output Format:
#   Print the modified string with the character at `position` replaced by `c`.
#
# Sample Input:
#   abracadabra
#   5 k
#
# Sample Output:
#   abrackdabra
#
# Approach:
#   Since strings are immutable in Python, direct index assignment like
#   string[5] = 'k' raises a TypeError. Two valid workarounds exist:
#     - Approach 1: String slicing — split the string around the target
#       index and concatenate with the new character in between.
#     - Approach 2: List conversion — convert the string to a mutable list,
#       update the character at the index, then join back into a string.
#   Both approaches are implemented below for comparison.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-02
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Approach 1: String Slicing ✅ (Active Solution)
# -----------------------------------------------------------------------------

def mutate_string(string, position, character):
    """
    Replace the character at the given position in the string.

    Args:
        string    (str): The original immutable string.
        position  (int): The index of the character to replace.
        character (str): The new character to insert at the given position.

    Returns:
        str: The modified string with the replacement applied.
    """

    # Strings in Python are immutable — they cannot be changed in-place.
    # Direct assignment like string[position] = character raises a TypeError.
    #
    # Slicing approach:
    #   string[:position]   → all characters BEFORE the target index
    #   character           → the new replacement character
    #   string[position+1:] → all characters AFTER the target index
    #
    # The three parts are concatenated to form the modified string.
    # e.g. "abracadabra", position=5, character='k'
    #       "abrac" + "k" + "dabra" → "abrackdabra"
    string = string[:position] + character + string[position + 1:]
    return string


# -----------------------------------------------------------------------------
# Approach 2: List Conversion (commented out — for learning purposes)
# -----------------------------------------------------------------------------

# def mutate_string(string, position, character):
#     """
#     Replace the character at the given position using list conversion.
#
#     Args:
#         string    (str): The original immutable string.
#         position  (int): The index of the character to replace.
#         character (str): The new character to insert at the given position.
#
#     Returns:
#         str: The modified string with the replacement applied.
#     """
#
#     # Convert the immutable string into a mutable list of characters.
#     # Each character in the string becomes a separate element in the list.
#     # e.g. "abracadabra" → ['a','b','r','a','c','a','d','a','b','r','a']
#     l = list(string)
#
#     # Directly assign the new character at the target index.
#     # Lists are mutable, so index assignment is allowed here.
#     l[position] = character
#
#     # Join the list of characters back into a single string.
#     # "".join(l) concatenates all elements with no separator.
#     # e.g. ['a','b','r','a','c','k','d','a','b','r','a'] → "abrackdabra"
#     string = "".join(l)
#     return string


# -----------------------------------------------------------------------------
# Main Guard — Input Handling
# -----------------------------------------------------------------------------

# All input reading and output logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the original string from stdin.
    s = input()

    # Read the position (index) and replacement character from stdin.
    # Both are on the same line, separated by a space.
    # i → index as string, c → replacement character
    i, c = input().split()

    # Call mutate_string() with the string, integer index, and character.
    # int(i) converts the index from string to integer for slicing/indexing.
    s_new = mutate_string(s, int(i), c)

    # Print the modified string.
    print(s_new)


# =============================================================================
# Key Concepts Covered:
#   - String immutability : Strings in Python CANNOT be changed in-place.
#                           string[i] = 'x' raises a TypeError.
#                           A new string must always be constructed.
#   - String slicing      : s[a:b] extracts characters from index a up to
#                           (but not including) index b.
#                           s[:b]  → from start up to index b (exclusive)
#                           s[a:]  → from index a to the end
#                           s[:]   → full copy of the string
#   - list(string)        : Converts a string into a list of individual
#                           characters. Lists ARE mutable — index assignment
#                           is allowed on lists but not on strings.
#   - "".join(list)       : Joins a list of characters back into a string
#                           with no separator between elements.
#   - tuple unpacking     : `i, c = input().split()` unpacks exactly two
#                           tokens from the input line into two variables
#                           in a single, clean expression.
#
# Approach 1 vs Approach 2 — Comparison:
#   Approach 1 (Slicing):
#     + Concise and readable — fits in one line.
#     + No intermediate data structure needed.
#     + Slightly faster for single character replacements.
#     ✅ Preferred for simple, one-off character replacements.
#   Approach 2 (List conversion):
#     + More intuitive for beginners — mirrors how arrays work in other languages.
#     + More flexible when multiple characters need to be replaced.
#     + Efficient when performing many mutations (avoids repeated slicing).
#
# String Slicing Quick Reference:
#   s[:]      → full copy of string
#   s[a:b]    → characters from index a to b-1
#   s[:b]     → characters from start to b-1
#   s[a:]     → characters from index a to end
#   s[::2]    → every 2nd character (step slicing)
#   s[::-1]   → reversed string
# =============================================================================