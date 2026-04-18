# =============================================================================
# Problem  : Collections.Counter()
# Domain   : Python
# Sub-Domain: Collections
# Difficulty: Easy
# Score    : 10 points
#
# Problem Link:
#   https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
#
# Problem Statement:
#   A shoe shop owner has x shoes of various sizes. Given n customers, each
#   willing to pay a certain price for a specific shoe size, compute the
#   total amount of money earned. Each shoe can only be sold once.
#
# Input Format:
#   - First line  : Integer x — the number of shoes in the shop.
#   - Second line : x space-separated integers — the size of each shoe.
#   - Third line  : Integer n — the number of customers.
#   - Next n lines: Two space-separated values per line:
#                   desired shoe size and the price the customer will pay.
#
# Constraints:
#   - 0 < x ≤ 10^3
#   - 0 < n ≤ 10^3
#   - 0 < price ≤ 100
#   - 0 < size ≤ 100
#
# Output Format:
#   Print the total amount of money earned.
#
# Sample Input:
#   10
#   2 3 4 5 6 8 7 6 5 18
#   6
#   6 55
#   6 45
#   6 55
#   4 40
#   18 60
#   10 50
#
# Sample Output:
#   200
#
# Explanation:
#   Customer 1: Buys size 6 for $55  → earned $55,  size 6 count: 2→1
#   Customer 2: Buys size 6 for $45  → earned $45,  size 6 count: 1→0
#   Customer 3: Size 6 unavailable   → no sale
#   Customer 4: Buys size 4 for $40  → earned $40,  size 4 count: 1→0
#   Customer 5: Buys size 18 for $60 → earned $60,  size 18 count: 1→0
#   Customer 6: Size 10 not in shop  → no sale
#   Total = 55 + 45 + 40 + 60 = $200
#
# Approach:
#   Use collections.Counter() to build a frequency map of shoe sizes.
#   For each customer, check if their desired size is available (count > 0).
#   If available, add the price to the total and decrement the shoe count
#   to reflect that one shoe of that size has been sold.
#
# Author  : Md. Ualiur Rahman Rahat
# GitHub  : https://github.com/ualiurrahat/hackerrank-python-coding-solutions
# Date    : 2026-04-18
# =============================================================================

#!/bin/python3

# Import Counter from the collections module.
# Counter is a specialized dictionary subclass designed for counting
# hashable objects. It maps each element to its frequency (count).
from collections import Counter


# -----------------------------------------------------------------------------
# Main Guard
# -----------------------------------------------------------------------------

# All input reading and solution logic lives inside this block.
# This ensures the code only executes when the script is run directly,
# not when it is imported as a module by another script or the judge system.
if __name__ == '__main__':

    # Read the total number of shoes in the shop.
    x = int(input())

    # Read all shoe sizes into a list.
    # map(int, input().split()) converts each space-separated token to int.
    shoe_sizes = list(map(int, input().split()))

    # Build a frequency counter for shoe sizes using Counter().
    # Counter maps each unique size to the number of times it appears.
    # e.g. [2,3,4,5,6,8,7,6,5,18] → Counter({6:2, 5:2, 2:1, 3:1, 4:1, ...})
    # This allows O(1) lookup of how many shoes of a given size are available.
    shoe_count = Counter(shoe_sizes)

    # Read the number of customers.
    n = int(input())

    # Initialize total earnings to zero.
    total_amount = 0

    # ------------------------------------------------------------------
    # Process Each Customer
    # ------------------------------------------------------------------

    for _ in range(n):

        # Read the customer's desired shoe size and their offered price.
        # input().split() splits the line into two string tokens.
        info = input().split()
        desired_size = int(info[0])   # the shoe size the customer wants
        price        = int(info[1])   # the price the customer will pay

        # Check if the desired shoe size is still in stock.
        # Counter returns 0 for any key not present — no KeyError raised.
        # This means shoe_count[desired_size] safely returns 0 for sizes
        # not in the shop, without needing an explicit existence check.
        if shoe_count[desired_size] > 0:

            # Sale made — add the customer's price to total earnings.
            total_amount += price

            # Decrement the stock count for this size by 1 to reflect
            # that one shoe has been sold and is no longer available.
            shoe_count[desired_size] -= 1

    # ------------------------------------------------------------------
    # Print Total Earnings
    # ------------------------------------------------------------------

    print(total_amount)


# =============================================================================
# Key Concepts Covered:
#   - Counter()        : A dict subclass from the collections module that
#                        counts hashable objects. Each element maps to its
#                        frequency (how many times it appears).
#                        e.g. Counter([1,1,2,3]) → Counter({1:2, 2:1, 3:1})
#   - Counter default  : Accessing a missing key in a Counter returns 0
#                        instead of raising a KeyError — safe for lookups.
#                        e.g. Counter({1:2})[99] → 0 (no error)
#   - Counter as dict  : Counter supports all standard dict operations —
#                        you can increment, decrement, and access counts
#                        using standard key indexing (counter[key]).
#   - Frequency map    : Counter is the Pythonic way to build a frequency
#                        map — replacing manual dict-based counting loops.
#
# Counter() vs Manual Dictionary Counting:
#   Manual approach:
#     freq = {}
#     for size in shoe_sizes:
#         freq[size] = freq.get(size, 0) + 1
#   Counter approach:
#     freq = Counter(shoe_sizes)    ← one line, same result ✅
#   Counter is always preferred — concise, readable, and purpose-built.
#
# Useful Counter Methods Quick Reference:
#   Counter(iterable)        → build frequency map from any iterable
#   counter[key]             → get count of key (0 if missing, no error)
#   counter.most_common(n)   → list of n most common (element, count) pairs
#   counter.elements()       → iterator over elements repeated by count
#   counter.update(iter)     → add counts from another iterable or counter
#   counter.subtract(iter)   → subtract counts (can go negative)
#   sum(counter.values())    → total count of all elements
# =============================================================================