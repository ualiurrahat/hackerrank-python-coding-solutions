# =============================================================================
# Problem  : Zipped!
# Domain   : Python
# Sub-Domain: Built-ins
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
#
# Problem Statement:
#   Given the marks of n students across x subjects, compute and print the
#   average score of each student. Averages must be correct to 1 decimal place.
#
# Input Format:
#   - First line    : Two integers n (students) and x (subjects), space-separated.
#   - Next x lines  : n space-separated float marks for each subject.
#
# Constraints:
#   - 0 < n ≤ 100
#   - 0 < x ≤ 100
#
# Output Format:
#   Print the average score of each student on a separate line,
#   correct to 1 decimal place.
#
# Sample Input:
#   5 3
#   89 90 78 93 80
#   90 91 85 88 86
#   91 92 83 89 90.5
#
# Sample Output:
#   90.0
#   91.0
#   82.0
#   90.0
#   85.5
#
# Explanation:
#   Subject marks matrix (rows = subjects, columns = students):
#     Subject 1: [89, 90, 78, 93, 80   ]
#     Subject 2: [90, 91, 85, 88, 86   ]
#     Subject 3: [91, 92, 83, 89, 90.5 ]
#   After zipping, each tuple contains one student's scores across all subjects:
#     Student 1: (89, 90, 91)   → avg = 90.0
#     Student 2: (90, 91, 92)   → avg = 91.0
#     Student 3: (78, 85, 83)   → avg = 82.0
#     Student 4: (93, 88, 89)   → avg = 90.0
#     Student 5: (80, 86, 90.5) → avg = 85.5
#
# Approach:
#   Read all subject mark rows into a 2D list (list of lists).
#   Use zip(*subject_marks) to transpose the matrix — converting rows of
#   subject scores into columns of per-student scores. Then compute the
#   average for each student's tuple and print it.
#
# Note on __name__ guard:
#   This file does not use `if __name__ == '__main__':` because the
#   HackerRank Online Judge for this problem runs the script directly
#   and does not require the guard. Its absence here is intentional —
#   not a structural error.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-18
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Input Reading
# -----------------------------------------------------------------------------

# Read n (number of students) and x (number of subjects) from the first line.
# userInput is a list of two string tokens — converted to int individually.
userInput = input().split()
n = int(userInput[0])    # total number of students
x = int(userInput[1])    # total number of subjects

# Initialize an empty list to hold the marks for each subject.
# Each element will be a list of n float scores for one subject.
subject_marks = []

# Read x lines of marks — one line per subject.
# map(float, ...) handles both integer and decimal mark values (e.g. 90.5).
for _ in range(x):
    marks = list(map(float, input().split()))
    subject_marks.append(marks)

# After this loop, subject_marks is a 2D list:
# [
#   [89, 90, 78, 93, 80   ],   ← Subject 1 scores for all 5 students
#   [90, 91, 85, 88, 86   ],   ← Subject 2 scores for all 5 students
#   [91, 92, 83, 89, 90.5 ]    ← Subject 3 scores for all 5 students
# ]


# -----------------------------------------------------------------------------
# Compute and Print Each Student's Average
# -----------------------------------------------------------------------------

# zip(*subject_marks) transposes the 2D list:
#   * (unpacking) expands subject_marks into separate arguments for zip().
#   zip() then groups the i-th element from each subject list together,
#   effectively converting rows (subjects) into columns (students).
#
# Before zip: rows = subjects, columns = students
# After zip:  each tuple = one student's scores across all subjects
#
# e.g. zip(*[[89,90,78], [90,91,85], [91,92,83]])
#      → (89,90,91), (90,91,92), (78,85,83)
#         student 1   student 2   student 3

for student_marks in zip(*subject_marks):

    # Compute the average: sum of all subject scores / number of subjects.
    # len(student_marks) == x (number of subjects) for every student.
    average = sum(student_marks) / len(student_marks)

    # Print the average — Python floats display one decimal place naturally
    # when the result is a whole number (e.g. 90.0) or has decimals (85.5).
    print(average)


# =============================================================================
# Key Concepts Covered:
#   - zip(*iterables)  : Aggregates elements from multiple iterables into
#                        tuples. The i-th tuple contains the i-th element
#                        from each iterable.
#                        If iterables have unequal lengths, zip() stops at
#                        the shortest one.
#                        e.g. zip([1,2,3], [4,5,6]) → (1,4), (2,5), (3,6)
#   - * unpacking      : zip(*matrix) unpacks a 2D list into separate
#                        arguments for zip(), effectively transposing the
#                        matrix (swapping rows and columns).
#   - Matrix transpose : Converting rows → columns and columns → rows.
#                        zip(*matrix) is the Pythonic one-liner for this.
#   - map(float, ...)  : Converts string tokens to floats — necessary here
#                        because marks can be decimals like 90.5.
#   - sum() / len()    : Standard average formula applied to each tuple.
#
# zip() Behavior Quick Reference:
#   zip([1,2,3], [4,5,6])          → (1,4), (2,5), (3,6)
#   zip([1,2,3], [4,5])            → (1,4), (2,5)        (truncates to shortest)
#   zip(*[[1,2],[3,4],[5,6]])       → (1,3,5), (2,4,6)   (matrix transpose)
#   list(zip("abc", [1,2,3]))       → [('a',1),('b',2),('c',3)]
#
# Matrix Transpose — zip() vs Manual Loop:
#   Manual:
#     transposed = []
#     for i in range(len(matrix[0])):
#         col = [row[i] for row in matrix]
#         transposed.append(col)
#   Using zip:
#     transposed = list(zip(*matrix))   ← one line, same result ✅
# =============================================================================