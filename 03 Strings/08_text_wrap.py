# =============================================================================
# Problem  : Text Wrap
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
#
# Problem Statement:
#   You are given a string and a width. Your task is to wrap the string
#   into a paragraph of the given width.
#   Complete the wrap function that takes:
#     - string  : a long string to be wrapped
#     - max_width : the maximum number of characters per line
#   The function returns a single string with newline characters ('\n')
#   inserted at the correct positions.
#
# Input Format:
#   The first line contains the string.
#   The second line contains an integer, max_width.
#
# Constraints:
#   - 0 < len(string) < 1000
#   - 0 < max_width < len(string)
#
# Output Format:
#   Print the wrapped paragraph as described above.
#
# Sample Input:
#   ABCDEFGHIJKLIMNOQRSTUVWXYZ
#   4
#
# Sample Output:
#   ABCD
#   EFGH
#   IJKL
#   IMNO
#   QRST
#   UVWX
#   YZ
#
# Approach:
#   Three solutions are presented, from manual to pythonic:
#     1. Manual loop approach   — builds result character by character
#     2. Slice + join approach  — uses range step-slicing and str.join()
#     3. textwrap.fill approach — uses Python's standard library directly
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-08
# =============================================================================

#!/bin/python3

import textwrap


# =============================================================================
# Solution 1: Manual Loop Approach (Original / Brute)
# =============================================================================
# Strategy:
#   Iterate through each character in the string, accumulating them into
#   a temporary `word` buffer. Once the buffer reaches max_width characters,
#   append it to the result with a newline and reset the buffer.
#   After the loop, if any remaining characters exist in `word`, append them
#   without a trailing newline.
#
# This mirrors how the problem is solved in languages like C — it is clear
# and explicit, but requires manual boundary tracking.
#
# Time Complexity : O(n) — each character is visited exactly once.
# Space Complexity: O(n) — result and word buffer together hold all characters.
# =============================================================================

def wrapManual(string, max_width):

    # -------------------------------------------------------------------------
    # Step 1: Initialize result string and a temporary chunk buffer.
    # -------------------------------------------------------------------------
    result = ""
    word = ""

    # -------------------------------------------------------------------------
    # Step 2: Accumulate characters one by one into the buffer.
    #         When the buffer hits max_width, flush it into result with '\n'.
    # -------------------------------------------------------------------------
    for char in string:
        word += char

        # When the current chunk is exactly max_width characters long,
        # it is complete — add it to the result followed by a newline,
        # then reset the buffer for the next chunk.
        if len(word) == max_width:
            result += word + '\n'
            word = ""

    # -------------------------------------------------------------------------
    # Step 3: Handle the last chunk (if it didn't fill up to max_width).
    #         It must be added WITHOUT a trailing newline.
    # -------------------------------------------------------------------------
    if len(word):
        result += word

    return result


# =============================================================================
# Solution 2: Pythonic Slice + Join Approach (Recommended)
# =============================================================================
# Strategy:
#   Use range() with a step of max_width to generate the start index of
#   every chunk. Slice the string at each index to extract a chunk of
#   exactly max_width characters (Python handles the final short chunk
#   automatically — no boundary check needed). Join all chunks with '\n'.
#
# Key Python concepts demonstrated:
#   - range(start, stop, step) : generates indices 0, max_width, 2*max_width…
#   - string[i : i+max_width]  : extracts a slice of up to max_width chars
#   - '\n'.join(iterable)      : joins items with newlines, no trailing '\n'
#   - Generator expression     : memory-efficient — chunks are produced lazily
#
# This is the idiomatic Python pattern for splitting any sequence into
# fixed-size chunks (strings, lists, binary data, API batches, etc.).
#
# Time Complexity : O(n) — each character is sliced and joined exactly once.
# Space Complexity: O(n) — generator produces chunks on demand; join is O(n).
# =============================================================================

def wrapSlice(string, max_width):

    # -------------------------------------------------------------------------
    # range(0, len(string), max_width) yields: 0, max_width, 2*max_width, ...
    # string[i : i+max_width] slices exactly max_width chars starting at i.
    # For the last chunk, Python clips the slice at the end of the string,
    # so no IndexError or manual remainder handling is needed.
    # '\n'.join(...) stitches all chunks together with newlines between them,
    # producing no trailing newline — exactly what the problem expects.
    # -------------------------------------------------------------------------
    return '\n'.join(string[i : i + max_width] for i in range(0, len(string), max_width))


# =============================================================================
# Solution 3: Standard Library Approach — textwrap.fill()
# =============================================================================
# Strategy:
#   Python's built-in textwrap module provides fill(), which wraps a string
#   to a given width and returns it as a single string with '\n' line breaks.
#   The module is imported at the top of the file.
#
# When to use this:
#   In production code or tooling, always prefer textwrap — it handles
#   edge cases like whitespace, hyphenation, and long words by default.
#   For competitive programming, it's the fastest to write.
#
# textwrap.fill(text, width):
#   Wraps the single paragraph in `text` so that every line is at most
#   `width` characters long, and returns a single string.
#
# Time Complexity : O(n) — internally iterates over the string once.
# Space Complexity: O(n) — builds and returns the wrapped result string.
# =============================================================================

def wrapLibrary(string, max_width):

    # textwrap.fill() wraps the string and joins lines with '\n' internally.
    # This is a one-liner that replaces all manual chunking logic above.
    return textwrap.fill(string, max_width)


# =============================================================================
# Main Guard
# =============================================================================
# The HackerRank judge calls the `wrap` function directly.
# We alias it to our recommended Solution 2 (slice + join).
# All input reading and output printing happens here.
# =============================================================================

def wrap(string, max_width):
    # -----------------------------------------------------------------------
    # Active solution: Solution 2 — Pythonic slice + join.
    # Swap the call below to wrapManual() or wrapLibrary() to test others.
    # -----------------------------------------------------------------------
    return wrapSlice(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# =============================================================================
# Key Concepts Covered:
#   - Manual loop        : Character-by-character accumulation with a buffer.
#                          Explicit boundary tracking — clear but verbose.
#   - range(0, n, step)  : Generates start indices with a custom step size.
#                          Core tool for fixed-size chunking in Python.
#   - String slicing     : string[i : i+w] extracts a substring of width w.
#                          Python clips gracefully at the end of the string.
#   - Generator expression: (expr for x in iterable) — lazy, memory-efficient
#                          sequence production without building a full list.
#   - str.join(iterable) : Concatenates items with a separator between each.
#                          '\n'.join([...]) produces no leading/trailing '\n'.
#   - textwrap.fill()    : Standard library one-liner for text wrapping.
#                          Handles edge cases automatically in real projects.
#
# Solution Comparison:
#   ┌─────────────────────┬───────────────────────────────────────────────┐
#   │ Solution            │ Key Technique                                 │
#   ├─────────────────────┼───────────────────────────────────────────────┤
#   │ wrapManual()        │ Manual loop + buffer — explicit, C-style      │
#   │ wrapSlice()         │ range step + slice + join — idiomatic Python  │
#   │ wrapLibrary()       │ textwrap.fill() — standard library shortcut   │
#   └─────────────────────┴───────────────────────────────────────────────┘
#
# Chunking Pattern (universal):
#   [seq[i : i+w] for i in range(0, len(seq), w)]
#   Works for strings, lists, bytes — any subscriptable sequence.
# =============================================================================