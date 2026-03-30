# =============================================================================
# Problem  : Finding the Percentage
# Domain   : Python
# Sub-Domain: Basic Data Types
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
#
# Problem Statement:
#   Given a dictionary of students and their marks, print the average of
#   the marks for a queried student, rounded to 2 decimal places.
#
# Input Format:
#   - First line       : An integer n (number of students).
#   - Next n lines     : Each line contains a student's name followed by
#                        their space-separated marks.
#   - Last line        : query_name — the student whose average to compute.
#
# Constraints:
#   - 2 ≤ n ≤ 10
#   - 0 ≤ marks ≤ 100
#   - Marks may be floats.
#
# Output Format:
#   Print the average marks of the queried student to exactly 2 decimal places.
#
# Sample Input 0:              Sample Output 0:
#   3                            56.00
#   Krishna 67 68 69
#   Arjun 70 98 63
#   Malika 52 56 60
#   Malika
#
# Explanation:
#   Malika's marks are [52, 56, 60].
#   Average = (52 + 56 + 60) / 3 = 56.00
#
# Sample Input 1:              Sample Output 1:
#   2                            26.50
#   Harsh 25 26.5 28
#   Anurag 26 28 30
#   Harsh
#
# Approach:
#   Read each student's name and marks into a dictionary where the key is
#   the student's name and the value is a list of float marks.
#   Use the starred assignment (*line) to unpack the name from the marks
#   in a single line. Then compute the average for the queried student
#   and format the output to exactly 2 decimal places using an f-string.
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

    # Read the number of students from stdin.
    n = int(input())

    # Initialize an empty dictionary to store student records.
    # Key   → student name (string)
    # Value → list of marks (list of floats)
    student_marks = {}

    for _ in range(n):

        # Unpack the input line using starred assignment:
        # `name` captures the first token (the student's name).
        # `*line` captures ALL remaining tokens as a list of strings.
        # e.g. "Malika 52 56 60".split() → ["Malika", "52", "56", "60"]
        #       name = "Malika", line = ["52", "56", "60"]
        name, *line = input().split()

        # Convert the list of string marks to a list of floats.
        # float() is used (instead of int()) to handle decimal marks like 26.5.
        scores = list(map(float, line))

        # Store the student's marks list in the dictionary under their name.
        student_marks[name] = scores

    # Read the name of the student to query.
    query_name = input()

    # ------------------------------------------------------------------
    # Approach 1: Manual Loop (explicit, beginner-friendly)
    # ------------------------------------------------------------------
    # Iterate over the queried student's marks manually, accumulating
    # the total marks and counting the number of subjects.

    # total_marks = 0    # accumulator for the sum of all marks
    # total_sub = 0      # counter for the number of subjects

    # for mark in student_marks[query_name]:
    #     total_marks += mark   # add each mark to the running total
    #     total_sub += 1        # increment subject count

    # average_mark = total_marks / total_sub
    # print(f"{average_mark:.2f}")

    # ------------------------------------------------------------------
    # Approach 2: Using sum() and len() (Pythonic, concise) ✅
    # ------------------------------------------------------------------
    # sum() returns the total of all elements in the list.
    # len() returns the number of elements in the list.
    # Dividing the two gives the arithmetic mean (average).
    # This replaces the manual loop above with two built-in functions.

    average_mark = sum(student_marks[query_name]) / len(student_marks[query_name])

    # Format the output to exactly 2 decimal places using an f-string.
    # :.2f → format specifier meaning "fixed-point float with 2 decimals".
    # e.g. 56.0 → "56.00",  26.5 → "26.50",  37.2133 → "37.21"
    print(f"{average_mark:.2f}")


# =============================================================================
# Key Concepts Covered:
#   - Dictionary       : A key-value data structure. Here, student names
#                        map to their list of marks.
#                        Syntax: {key: value}
#                        Access: dict[key] → returns the value for that key.
#   - Starred assignment: `name, *line = iterable` unpacks the first element
#                        into `name` and ALL remaining elements into `line`.
#                        A clean Pythonic way to split a head from a tail.
#   - map(float, list) : Applies float() to every element of a list.
#                        Returns a lazy iterator — wrap in list() to evaluate.
#   - sum(list)        : Returns the sum of all numeric elements in a list.
#   - len(list)        : Returns the number of elements in a list.
#   - f-string         : A formatted string literal. Syntax: f"...{value}..."
#                        :.2f inside braces formats a float to 2 decimal places.
#
# Approach 1 vs Approach 2 — Comparison:
#   Approach 1 (manual loop):
#     + Explicit and easy to follow for beginners.
#     - Verbose — requires extra variables and a loop.
#   Approach 2 (sum + len):
#     + Concise, readable, and Pythonic.
#     + Uses built-in functions optimised at the interpreter level.
#     ✅ Preferred in professional Python code.
#
# f-string Format Specifiers Quick Reference:
#   f"{value:.2f}"   → 2 decimal places     e.g. 56.0    → "56.00"
#   f"{value:.4f}"   → 4 decimal places     e.g. 3.14159 → "3.1416"
#   f"{value:10.2f}" → width 10, 2 decimals e.g. 56.0    → "     56.00"
#   f"{value:,}"     → thousand separator   e.g. 10000   → "10,000"
# =============================================================================