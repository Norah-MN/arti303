"""Student record utilities for ARTI 303.

Built incrementally in Lab 2: the Student class comes from the guided
walkthrough (README, Part A). Everything below the class is added
independently during Part B, one function per task.
"""


class Student:
    """A single student record."""

    def __init__(self, name, age, gpa, is_enrolled=True):
        if not (0.0 <= gpa <= 4.0):
            raise ValueError(f"gpa must be between 0.0 and 4.0, got {gpa}")
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_enrolled = is_enrolled

    def is_dean_list(self):
        """Return True if this student's GPA qualifies for the Dean's list."""
        return self.gpa >= 3.5

    def report_line(self):
        """Return a one-line, human-readable summary of this student."""
        status = "made the Dean's list" if self.is_dean_list() else "did not make the Dean's list"
        enrollment = "is enrolled" if self.is_enrolled else "is not enrolled"
        return f"{self.name} (age {self.age}, GPA {self.gpa:.2f}) {enrollment} and {status}."

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age}, gpa={self.gpa})"


def average_gpa(students):
    """Return the average GPA across a list of Student objects.

    Returns 0.0 for an empty list rather than raising an error.
    """
    if not students:
        return 0.0
    total = 0.0
    for s in students:
        total += s.gpa
    return total / len(students)


def dean_list_students(students):
    """Return a new list containing only students who made the Dean's list."""
    result = []
    for s in students:
        if s.is_dean_list():
            result.append(s)
    return result


def letter_grade(gpa):
    """Convert a numeric GPA to a simplified letter grade.

    A teaching illustration for practising if/elif/else — not the
    department's official grading scale.
    """
    if gpa >= 3.7:
        return "A"
    elif gpa >= 2.7:
        return "B"
    elif gpa >= 1.7:
        return "C"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"


def oldest_student(students):
    """Return the Student with the highest age.

    Raises ValueError if the list is empty.
    """
    if not students:
        raise ValueError("Cannot find the oldest student in an empty list.")
    oldest = students[0]
    for s in students[1:]:
        if s.age > oldest.age:
            oldest = s
    return oldest


def group_by_enrollment(students):
    """Split students into (enrolled, not_enrolled) lists."""
    enrolled = []
    not_enrolled = []
    for s in students:
        if s.is_enrolled:
            enrolled.append(s)
        else:
            not_enrolled.append(s)
    return enrolled, not_enrolled


def top_n_by_gpa(students, n):
    """Return the n students with the highest GPA, highest first.

    One possible answer to the open-ended Challenge task — sorts a copy
    so the caller's original list order isn't disturbed.
    """
    ranked = sorted(students, key=lambda s: s.gpa, reverse=True)
    return ranked[:n]
