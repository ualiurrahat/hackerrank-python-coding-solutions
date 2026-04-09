# =============================================================================
# Problem  : String Formatting
# Domain   : Python
# Sub-Domain: Strings
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
#
# Problem Statement:
#   Given an integer N, for each integer i from 1 to N, print the following
#   four representations on a single line, separated by a single space:
#     1. Decimal
#     2. Octal
#     3. Hexadecimal (uppercase letters)
#     4. Binary
#   Each value must be right-aligned (space-padded on the left) to match
#   the width of N expressed in binary.
#
# Input Format:
#   A single integer N.
#
# Constraints:
#   - 1 <= N <= 99
#
# Output Format:
#   N lines, each containing the four representations of i (1 to N),
#   right-aligned to the binary width of N, separated by a single space.
#
# Sample Input : 17
# Sample Output:
#     1     1     1     1
#     2     2     2    10
#     ...
#    17    21    11 10001
#
# Approach:
#   Use Python's built-in format(value, spec) function with a dynamic
#   width derived from the binary representation of N. A single format
#   specifier combines both the base conversion and the padding in one call.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-09
# =============================================================================

#!/bin/python3


# =============================================================================
# Solution: Pythonic format() with Dynamic Width Specifier
# =============================================================================
# Core Concepts:
#
#   format(value, spec) — Python's built-in base conversion + alignment tool.
#   The format spec string controls both the base and the field width:
#
#     format(i, 'd')  → decimal         e.g. format(17, 'd')  → '17'
#     format(i, 'o')  → octal           e.g. format(17, 'o')  → '21'
#     format(i, 'X')  → hex (uppercase) e.g. format(17, 'X')  → '11'
#     format(i, 'b')  → binary          e.g. format(17, 'b')  → '10001'
#
#   Width can be embedded directly in the spec for right-alignment:
#     format(i, '5d') → decimal in a field of width 5, padded left with spaces
#     format(i, '5o') → octal   in a field of width 5, padded left with spaces
#
#   Using an f-string to make the width dynamic:
#     format(i, f'{width}d') → decimal right-aligned in `width` characters
#
#   This replaces the C++ approach of computing each base via division/modulo
#   loops and manually tracking string widths — Python handles it in one call.
#
# Width Calculation:
#   The required column width equals the number of digits in N's binary form.
#   Binary always produces the longest representation, so it sets the width:
#     width = len(format(number, 'b'))
#   e.g. for N=17 → format(17, 'b') = '10001' → width = 5
#
# Time Complexity : O(N log N) — for each of N integers, format() runs in
#                  O(log i) time proportional to the number of digits.
# Space Complexity: O(log N) — only one formatted row string is held at a time.
# =============================================================================

def print_formatted(number):

    # -------------------------------------------------------------------------
    # Step 1: Calculate the column width.
    # The binary representation of `number` is always the widest of the four
    # bases, so its length defines the padding width for all columns.
    # e.g. number=17 → binary '10001' → width=5
    # -------------------------------------------------------------------------
    width = len(format(number, 'b'))

    # -------------------------------------------------------------------------
    # Step 2: Iterate from 1 to number (inclusive) and print each row.
    # For each integer i, format all four representations with the same width
    # so that every column is right-aligned and space-padded on the left.
    #
    # f'{width}d' is a dynamic format spec:
    #   - `width` is the field width (number of characters, padded with spaces)
    #   - 'd' = decimal, 'o' = octal, 'X' = hex uppercase, 'b' = binary
    #
    # The four formatted values are joined by a single space using print().
    # -------------------------------------------------------------------------
    for i in range(1, number + 1):

        # Decimal: base 10, right-aligned in `width` chars
        decimal     = format(i, f'{width}d')

        # Octal: base 8, right-aligned in `width` chars
        octal       = format(i, f'{width}o')

        # Hexadecimal: base 16, uppercase letters (A-F), right-aligned
        # Note: lowercase 'x' would give 'a'-'f'; uppercase 'X' gives 'A'-'F'
        hexadecimal = format(i, f'{width}X')

        # Binary: base 2, right-aligned in `width` chars
        binary      = format(i, f'{width}b')

        # Print all four on one line, separated by a single space
        print(decimal, octal, hexadecimal, binary)


# =============================================================================
# Main Guard
# =============================================================================

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# =============================================================================
# Key Concepts Covered:
#   - format(value, spec)  : Converts an integer to a string in the specified
#                            base. The spec character controls the base:
#                              'd' → decimal (base 10)
#                              'o' → octal   (base  8)
#                              'X' → hex     (base 16, uppercase A-F)
#                              'x' → hex     (base 16, lowercase a-f)
#                              'b' → binary  (base  2)
#
#   - Width in format spec : Prepend an integer to the spec to set field width.
#                              format(7, '5d') → '    7'  (right-aligned)
#                              format(7, '5b') → '  111'  (right-aligned)
#
#   - Dynamic spec via f-string: f'{width}d' builds the spec string at runtime,
#                            allowing the column width to adapt to any input N.
#
#   - len(format(n, 'b'))  : Computes the number of binary digits in n.
#                            Used to set the uniform column width for all bases.
#                            Binary is always the widest, so it drives the width.
#
#   - print(*args)         : Prints multiple values separated by a space by
#                            default (sep=' '), with a newline at the end.
#
# Alternative Built-ins (awareness):
#   Python also provides bin(), oct(), and hex() for quick conversions:
#     bin(17) → '0b10001'   (includes '0b' prefix — needs stripping)
#     oct(17) → '0o21'      (includes '0o' prefix — needs stripping)
#     hex(17) → '0x11'      (includes '0x' prefix, lowercase — needs stripping)
#   format() is preferred here because it gives cleaner output with no prefix
#   and supports width/alignment in a single call.
#
# Format Spec Quick Reference:
#   format(n, 'd')      → decimal,          no padding
#   format(n, 'o')      → octal,            no padding
#   format(n, 'X')      → hex uppercase,    no padding
#   format(n, 'b')      → binary,           no padding
#   format(n, '10d')    → decimal,          right-aligned in width 10
#   format(n, f'{w}b')  → binary,           right-aligned in dynamic width w
# =============================================================================