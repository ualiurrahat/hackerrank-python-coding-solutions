# =============================================================================
# Problem  : What's Your Name?
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
#
# Problem Statement:
#   Given a person's first name and last name on two separate lines,
#   print the following greeting:
#   "Hello firstname lastname! You just delved into python."
#
# Input Format:
#   - First line  : The first name (string).
#   - Second line : The last name (string).
#
# Constraints:
#   - The length of the first and last names are each ≤ 1000.
#
# Output Format:
#   Print the greeting string with the first and last name inserted.
#
# Sample Input 0:
#   Ross
#   Taylor
#
# Sample Output 0:
#   Hello Ross Taylor! You just delved into python.
#
# Approach:
#   Read the first and last name from stdin, then use an f-string to
#   embed both names directly into the greeting template and print it.
#   f-strings are the most readable and efficient way to format strings
#   in modern Python (3.6+).
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-02
# =============================================================================

#!/bin/python3


# -----------------------------------------------------------------------------
# Function Definition
# -----------------------------------------------------------------------------

def print_full_name(first, last):
    """
    Print a greeting message using the given first and last name.

    Args:
        first (str): The person's first name.
        last  (str): The person's last name.

    Prints:
        str: A greeting in the format:
             "Hello firstname lastname! You just delved into python."
    """

    # Use an f-string to embed the first and last name into the greeting.
    # f-strings (formatted string literals) allow variables or expressions
    # to be inserted directly inside curly braces {} within the string.
    # They are concise, readable, and faster than older formatting methods.
    # e.g. f"Hello {first} {last}!" with first="Ross", last="Taylor"
    #      → "Hello Ross Taylor!"
    print(f"Hello {first} {last}! You just delved into python.")


# -----------------------------------------------------------------------------
# Main Guard — Input Handling
# -----------------------------------------------------------------------------

# All input reading and output logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the first name from stdin.
    first_name = input()

    # Read the last name from stdin.
    last_name = input()

    # Call print_full_name() with both names.
    # The function handles printing internally — no return value needed.
    print_full_name(first_name, last_name)


# =============================================================================
# Key Concepts Covered:
#   - f-string         : A formatted string literal introduced in Python 3.6.
#                        Prefix the string with `f` and embed variables or
#                        expressions inside curly braces {}.
#                        e.g. f"Hello {name}!" → "Hello Ross!"
#                        Faster and more readable than older alternatives.
#   - print() in func  : This function uses print() directly instead of
#                        returning a string. The problem specifies "Prints"
#                        rather than "Returns", so this is intentional.
#   - input()          : Reads a single line from stdin as a string.
#                        Each call reads one line — called twice here to
#                        read the first and last names separately.
#
# String Formatting Methods — Comparison:
#   Method             Example                          Output
#   -----------------------------------------------------------------------
#   f-string (3.6+)  : f"Hello {first} {last}!"      → "Hello Ross Taylor!"
#   .format()        : "Hello {} {}!".format(a, b)   → "Hello Ross Taylor!"
#   % formatting     : "Hello %s %s!" % (a, b)       → "Hello Ross Taylor!"
#   Concatenation    : "Hello " + a + " " + b + "!"  → "Hello Ross Taylor!"
#
#   ✅ f-strings are the preferred, modern approach — use them by default.
#      They are more readable, support expressions, and are the fastest
#      of the four methods at runtime.
#
# f-string Expression Support (bonus):
#   f-strings can evaluate expressions directly inside {}:
#   f"{2 + 2}"              → "4"
#   f"{first.upper()}"      → "ROSS"
#   f"{len(first)}"         → "4"
#   f"{first!r}"            → "'Ross'"   (repr format)
# =============================================================================