
"""Text helpers. The worked example every contribution is modelled on."""

import string


def word_count(text):
    """Count whitespace-separated words."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix

def clean_whitespace(text):
    """Remove extra whitespace and normalize it to single spaces."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())


def remove_punctuation(text):
    """Remove all punctuation characters from text.

    >>> remove_punctuation("Hello, world!")
    'Hello world'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.translate(str.maketrans("", "", string.punctuation))


def capitalize_words(text):
    """Capitalize the first letter of every word.

    >>> capitalize_words("hello world")
    'Hello World'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.title()

