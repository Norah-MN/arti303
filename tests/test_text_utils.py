"""Tests for src/text_utils.py"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import text_utils


def test_clean_name_whitespace():
    # TODO
     assert text_utils.clean_name("  sara   ali  ") == "Sara Ali"


def test_clean_name_capitalisation():
    # TODO
    assert text_utils.clean_name("FAISAL ALHARBI") == "Faisal Alharbi"
    assert text_utils.clean_name("lama") == "Lama"
