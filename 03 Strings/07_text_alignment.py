# =============================================================================
# Problem  : Text Alignment
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
#
# Problem Statement:
#   Given a thickness value (odd number), generate the HackerRank logo
#   using string alignment methods: ljust(), rjust(), and center().
#   The logo consists of 5 sections:
#     1. Top Cone
#     2. Top Pillars
#     3. Middle Belt
#     4. Bottom Pillars
#     5. Bottom Cone
#
# Input Format:
#   A single line containing an odd integer — the thickness value.
#
# Constraints:
#   - thickness must be an odd number.
#
# Output Format:
#   Print the HackerRank logo pattern built using 'H' characters.
#
# Sample Input : 5
# Sample Output:
#     H
#    HHH
#   HHHHH
#  HHHHHHH
# HHHHHHHHH
#   HHHHH               HHHHH
#   ... (see problem link for full output)
#
# Approach:
#   Each section of the logo is constructed using Python's three string
#   alignment methods — rjust(), ljust(), and center() — combined with
#   string repetition (c * n) to produce rows of 'H' characters at the
#   correct width and alignment for each section.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-08
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the thickness value — must be an odd integer.
    # thickness controls the size of every section of the logo.
    thickness = int(input())

    # The character used to draw the entire logo.
    c = 'H'

    # ------------------------------------------------------------------
    # Section 1: Top Cone
    # ------------------------------------------------------------------
    # Builds a triangle pointing upward, growing from 1 'H' to
    # (2 * thickness - 1) 'H's, centered around the middle column.
    #
    # For each row i (0 to thickness-1):
    #   - Left side  : (c * i).rjust(thickness-1) → i H's right-aligned
    #                  in a field of (thickness-1) chars (left-padded with spaces)
    #   - Center     : c → always one 'H' at the tip/middle
    #   - Right side : (c * i).ljust(thickness-1) → i H's left-aligned
    #                  in a field of (thickness-1) chars (right-padded with spaces)
    # Row 0: "    H    " (just the tip)
    # Row 4: "HHHHHHHHH" (full base of cone)
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # ------------------------------------------------------------------
    # Section 2: Top Pillars
    # ------------------------------------------------------------------
    # Two vertical pillars of width `thickness`, separated by empty space.
    # Each pillar is centered within its allocated column width:
    #   - Left pillar  : (c * thickness).center(thickness * 2)
    #   - Right pillar : (c * thickness).center(thickness * 6)
    # Repeated (thickness + 1) times to form the pillar height.
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # ------------------------------------------------------------------
    # Section 3: Middle Belt
    # ------------------------------------------------------------------
    # A horizontal band of H's spanning the full width of both pillars,
    # forming the crossbar of the 'H' shape in the logo.
    # Width = thickness * 5, centered in a field of thickness * 6.
    # Repeated (thickness + 1) // 2 times for the belt height.
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # ------------------------------------------------------------------
    # Section 4: Bottom Pillars
    # ------------------------------------------------------------------
    # Identical to the top pillars — two vertical pillars below the belt.
    # Mirrors Section 2 exactly to complete the symmetric 'H' structure.
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # ------------------------------------------------------------------
    # Section 5: Bottom Cone
    # ------------------------------------------------------------------
    # Builds an inverted triangle pointing downward, shrinking from
    # (2 * thickness - 1) 'H's down to 1 'H', right-aligned to sit
    # under the right pillar.
    #
    # For each row i (0 to thickness-1):
    #   - (thickness - i - 1) gives the count of H's on each side,
    #     shrinking by 1 each row as the cone narrows downward.
    #   - The inner expression mirrors the Top Cone construction.
    #   - The outer .rjust(thickness * 6) shifts the entire row to the
    #     right to align with the right pillar of the logo.
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


# =============================================================================
# Key Concepts Covered:
#   - str.ljust(width)   : Returns the string left-aligned within a field
#                          of `width` characters, padded with spaces on the right.
#                          e.g. 'HH'.ljust(5)  → 'HH   '
#   - str.rjust(width)   : Returns the string right-aligned within a field
#                          of `width` characters, padded with spaces on the left.
#                          e.g. 'HH'.rjust(5)  → '   HH'
#   - str.center(width)  : Returns the string centered within a field of
#                          `width` characters, padded with spaces on both sides.
#                          e.g. 'HH'.center(6) → '  HH  '
#   - String repetition  : c * n repeats string c exactly n times.
#                          e.g. 'H' * 5 → 'HHHHH'
#   - String concatenation: Sections of each row are joined using + to
#                          combine left-aligned, centered, and right-aligned
#                          parts into a single output line.
#   - (thickness+1)//2   : Integer (floor) division used to calculate the
#                          middle belt height — ensures correct row count
#                          for both odd thickness values.
#
# Alignment Methods Quick Reference:
#   s.ljust(w)       → left-align  in width w  (pad right with spaces)
#   s.rjust(w)       → right-align in width w  (pad left with spaces)
#   s.center(w)      → center      in width w  (pad both sides)
#   s.ljust(w, '-')  → left-align  with custom fill character '-'
#   s.rjust(w, '-')  → right-align with custom fill character '-'
#   s.center(w, '-') → center      with custom fill character '-'
# =============================================================================