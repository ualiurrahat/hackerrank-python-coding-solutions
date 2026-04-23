# =============================================================================
# Problem  : eval() Built-in
# Domain   : Python
# Sub-Domain: Built-ins
# Difficulty: Easy
# Score    : 20 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-eval/problem?isFullScreen=true
#
# Problem Statement:
#   You are given an expression in a line. Read that line as a string
#   variable and print the result using eval().
#
# Input Format:
#   A single line containing a valid Python expression or statement.
#
# Constraints:
#   - Input string length < 100 characters.
#
# Output Format:
#   The result of evaluating the input expression using eval().
#
# Sample Input : print(2 + 3)
# Sample Output: 5
#
# Approach:
#   Read the input line as a raw string, then pass it directly to eval().
#   eval() parses and executes the expression within the current scope,
#   producing the same result as if the expression were written in code.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-23
# =============================================================================

#!/bin/python3


# =============================================================================
# Solution: eval() Built-in
# =============================================================================
# Core Concept — eval():
#   eval(expression) takes a string, parses it as a Python expression, and
#   executes it in the current scope. It has access to all variables,
#   functions, and keywords defined at the point of the call.
#
#   eval("9 + 5")       → 14         (arithmetic expression)
#   eval("print(2+3)")  → prints 5   (function call as a string)
#   eval("len")         → <built-in function len>
#
#   This is fundamentally different from simply storing "len" as a string —
#   eval() resolves the name against the actual Python runtime environment.
#
# Why input() here returns the expression as a raw string:
#   input() always returns a string, so typing  print(2 + 3)  at stdin
#   gives the string  'print(2 + 3)'  — it is NOT executed yet.
#   Passing that string to eval() then executes it, producing the output 5.
#
# Time Complexity : O(n) — proportional to the length of the input expression.
# Space Complexity: O(n) — the input string and evaluated result are O(n).
# =============================================================================


# -----------------------------------------------------------------------------
# Step 1: Read the input line as a raw string.
# input() returns whatever the user types as a plain string — it does not
# execute or interpret the content. The expression is stored, not run yet.
# -----------------------------------------------------------------------------
request = input()

# -----------------------------------------------------------------------------
# Step 2: Evaluate the string expression using eval().
# eval() parses the string as Python code and executes it in the current
# scope. For a statement like 'print(2 + 3)', eval() calls print() directly,
# which outputs the result to stdout — no explicit print() needed here.
# -----------------------------------------------------------------------------
eval(request)


# =============================================================================
# Key Concepts Covered:
#   - eval(expr)         : Parses and executes a string as a Python expression
#                          in the current scope. Has access to all defined
#                          variables, functions, and built-ins at call time.
#                          Returns the result of the expression if it produces
#                          a value, or None if the expression is a statement.
#
#   - input()            : Always returns user input as a raw string.
#                          Does NOT interpret or execute the content.
#                          eval(input()) is the pattern for executing
#                          a user-supplied expression at runtime.
#
# eval() vs type("len") — Key Distinction:
#   eval("len")   → <built-in function len>   (resolved against runtime)
#   type("len")   → <class 'str'>             (just a plain string)
#   eval() bridges the gap between string data and live Python objects.
#
# eval() Scope Awareness:
#   x = 10
#   eval("x + 5")   → 15   (eval() sees x in the current local scope)
#   eval() uses the calling frame's globals and locals by default, so it
#   has full access to variables defined before the eval() call.
#
# Caution with eval():
#   eval() executes arbitrary code, so it should never be used on untrusted
#   or unsanitized input in production applications. For this problem, the
#   input is controlled and safe, so eval() is the intended solution.
# =============================================================================s