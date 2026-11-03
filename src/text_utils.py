"""Helpers for cleaning up messy text fields."""


def clean_name(raw):
    """Strip, collapse inner whitespace, and title-case a name."""
    collapsed = " ".join(raw.split())
    return collapsed.title()
