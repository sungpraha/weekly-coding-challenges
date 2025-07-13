#!/usr/bin/env python3
"""
Week 11 – Longest Consecutive Sequence
=====================================
A standalone script that exposes:
• `longest_consecutive(nums)`  – the O(n) solution function
• A CLI (`python consecutive_sequence.py 100 4 200 1 3 2`) that prints the
  length of the longest consecutive run in the numbers passed on the command line.
• A unit‑test suite runnable with `python consecutive_sequence.py --test` or
  with the standard test discovery `python -m unittest consecutive_sequence`.
The module has **zero external dependencies** – it only uses the Python ≥3.8
standard library.
"""
from __future__ import annotations
import argparse
import sys
import unittest
from typing import List, Set


def longest_consecutive(nums: List[int]) -> int:
    """Return the length of the longest run of consecutive integers in *nums*.
    
    Runs in average‑case **O(n)** time and **O(n)** extra space by storing the
    numbers in a set for *O(1)* membership checks, and only expanding a run
    from numbers that are the *start* of a sequence (i.e. ``num - 1`` is not in
    the set).
    """
    if not nums:
        return 0
    
    num_set: Set[int] = set(nums)
    longest: int = 0
    
    for num in num_set:
        # Only start a new sequence if *num* is the leftmost value in that run.
        if num - 1 not in num_set:
            current = num
            streak = 1
            
            # Extend streak to the right as far as possible.
            while current + 1 in num_set:
                current += 1
                streak += 1
            
            longest = max(longest, streak)
    
    return longest


class LongestConsecutiveTests(unittest.TestCase):
    """Unit‑tests covering typical, edge‑ and corner‑cases."""
    
    def test_example_1(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
    
    def test_example_2(self):
        self.assertEqual(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
    
    def test_empty(self):
        self.assertEqual(longest_consecutive([]), 0)
    
    def test_single(self):
        self.assertEqual(longest_consecutive([42]), 1)
    
    def test_duplicates(self):
        # Duplicates should not break the sequence length calculation
        self.assertEqual(longest_consecutive([1, 2, 2, 3]), 3)
    
    def test_negative_numbers(self):
        self.assertEqual(longest_consecutive([-3, -2, -1, 0, 1]), 5)


def run_cli(argv: List[str]) -> None:
    """Parse *argv* and either run the solver on provided numbers or the tests."""
    parser = argparse.ArgumentParser(description="Longest Consecutive Sequence")
    parser.add_argument(
        "numbers",
        metavar="N",
        type=int,
        nargs="*",
        help="Integers to analyse (omit to run the unit‑tests)",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the built‑in unittest suite and exit.",
    )
    
    args = parser.parse_args(argv)
    
    if args.test or not args.numbers:
        # If --test is supplied *or* no positional numbers are given, run tests.
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(LongestConsecutiveTests)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        # Exit with a non‑zero status code on failure so CI pipelines can fail.
        sys.exit(not result.wasSuccessful())
    
    length = longest_consecutive(args.numbers)
    print(length)


if __name__ == "__main__":
    run_cli(sys.argv[1:])