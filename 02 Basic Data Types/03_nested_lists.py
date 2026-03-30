# =============================================================================
# Problem  : Nested Lists
# Domain   : Python
# Sub-Domain: Basic Data Types
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
#
# Problem Statement:
#   Given the names and grades of n students, store them in a nested list
#   and print the name(s) of any student(s) having the second lowest grade.
#   If multiple students share the second lowest grade, print their names
#   in alphabetical order, each on a new line.
#
# Input Format:
#   - First line       : An integer n (number of students).
#   - Next n × 2 lines : Each student's name on one line, grade on the next.
#
# Constraints:
#   - 2 ≤ n ≤ 5
#   - There will always be one or more students with the second lowest grade.
#
# Output Format:
#   Print the name(s) of student(s) with the second lowest grade.
#   If multiple, print each name alphabetically on a separate line.
#
# Sample Input 0:          Sample Output 0:
#   5                        Berry
#   Harry                    Harry
#   37.21
#   Berry
#   37.21
#   Tina
#   37.2
#   Akriti
#   41
#   Harsh
#   39
#
# Explanation:
#   students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
#               ['Akriti', 41], ['Harsh', 39]]
#   Lowest grade    → 37.2  (Tina)
#   2nd lowest grade → 37.21 (Harry and Berry)
#   Sorted alphabetically → Berry, Harry
#
# Approach:
#   1. Read each student's name and grade, storing them as (name, score)
#      tuples in a records list. Collect all scores separately.
#   2. Convert scores to a set to remove duplicates, then sort to get
#      unique grades in ascending order.
#   3. The second lowest grade is at index [1] of the sorted unique scores.
#   4. Filter records for students matching the second lowest grade,
#      collect their names, sort alphabetically, and print each one.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-03-30
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # ------------------------------------------------------------------
    # Step 1: Read and Store Student Records
    # ------------------------------------------------------------------

    records = []   # stores (name, score) tuples for all students
    scores = []    # stores only the score values for finding grade ranks

    # The underscore _ is a Python convention for a throwaway loop variable
    # — used when the loop counter itself is not needed, only the iteration.
    for _ in range(int(input())):

        name = input()           # read student name as a string
        score = float(input())   # read grade as a float (e.g. 37.21)

        # Store as a tuple (name, score) — tuples are ideal here because
        # each student record is a fixed pair of values that won't change.
        student = (name, score)
        records.append(student)  # add the student tuple to the records list
        scores.append(score)     # track score separately for grade analysis

    # ------------------------------------------------------------------
    # Step 2: Find the Second Lowest Unique Grade
    # ------------------------------------------------------------------

    # Convert scores list to a set to eliminate duplicate grade values,
    # then sort in ascending order to rank grades from lowest to highest.
    # e.g. [37.21, 37.21, 37.2, 41, 39] → sorted set → [37.2, 37.21, 39, 41]
    unique_scores = sorted(set(scores))

    # The second lowest grade is at index 1 of the sorted unique scores.
    # index 0 → lowest grade, index 1 → second lowest grade.
    second_lowest_grade = unique_scores[1]

    # ------------------------------------------------------------------
    # Step 3: Collect Names with the Second Lowest Grade
    # ------------------------------------------------------------------

    result = []   # will hold names of students with the second lowest grade

    for record in records:
        # record[0] → student name, record[1] → student score
        # Check if this student's score matches the second lowest grade.
        if record[1] == second_lowest_grade:
            result.append(record[0])   # collect the student's name

    # ------------------------------------------------------------------
    # Step 4: Sort Alphabetically and Print
    # ------------------------------------------------------------------

    # Sort the collected names in alphabetical (lexicographic) order.
    # list.sort() sorts the list in-place (modifies the original list).
    result.sort()

    # Print each qualifying student's name on a separate line.
    for student in result:
        print(student)


# =============================================================================
# Key Concepts Covered:
#   - Nested list      : A list that contains other lists (or tuples) as
#                        elements. e.g. [['Harry', 37.21], ['Tina', 37.2]]
#                        Used here to group each student's name and grade.
#   - tuple            : An immutable ordered collection. Used here for each
#                        student record (name, score) since the pair is fixed.
#   - float()          : Converts a string to a floating-point number.
#                        Used to handle decimal grades like 37.21.
#   - set()            : Removes duplicate values from a collection.
#                        Ensures each grade is counted only once when ranking.
#   - sorted()         : Returns a new sorted list. Does NOT modify the original.
#   - list.sort()      : Sorts a list in-place. MODIFIES the original list.
#                        Use sorted() when you need to keep the original intact.
#   - _ (throwaway)    : Convention for an unused loop variable. Signals to
#                        readers that the counter value is intentionally ignored.
#   - Indexing tuples  : record[0] accesses the first element (name),
#                        record[1] accesses the second element (score).
#
# sorted() vs list.sort() — Key Difference:
#   sorted(iterable) → returns a NEW sorted list, original unchanged.
#   list.sort()      → sorts IN-PLACE, modifies the original, returns None.
#   Use sorted() when you need to preserve the original order.
#   Use list.sort() when in-place modification is acceptable (saves memory).
#
# Alternative One-liner Solution:
#   second_lowest = sorted(set(scores))[1]
#   names = sorted(r[0] for r in records if r[1] == second_lowest)
#   print('\n'.join(names))
# =============================================================================