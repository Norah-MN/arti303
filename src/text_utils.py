"""TODO: describe this module."""
"""This module provides text utility functions."""

def clean_name(raw):
    """Clean and format a person's name."""
    # TODO: collapse whitespace, then title-case
    cleaned = " ".join(raw.split()) 
    return cleaned.title()
    pass
