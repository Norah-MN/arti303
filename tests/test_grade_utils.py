"""Tests for src/grade_utils.py"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import grade_utils


def test_letter_grade_boundaries():
    """Each boundary value should fall into the higher grade."""
    assert grade_utils.letter_grade(4.50) == "A"
    assert grade_utils.letter_grade(3.50) == "B"
    assert grade_utils.letter_grade(2.50) == "C"
    assert grade_utils.letter_grade(1.50) == "D"


def test_letter_grade_typical():
    assert grade_utils.letter_grade(5.00) == "A"
    assert grade_utils.letter_grade(3.90) == "B"
    assert grade_utils.letter_grade(0.00) == "F"


def test_dean_list():
    assert grade_utils.is_dean_list(4.50) is True
    assert grade_utils.is_dean_list(4.49) is False
