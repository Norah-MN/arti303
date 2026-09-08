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
