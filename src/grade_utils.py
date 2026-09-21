"""Grade helpers for the 5.00 GPA scale."""

DEANS_LIST_MIN = 4.50


def letter_grade(gpa):
    """Convert a GPA out of 5.00 into a letter grade."""
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"


def is_dean_list(gpa):
    """Return True if this GPA meets the Dean's List threshold."""
    return gpa >= DEANS_LIST_MIN
