"""Validate strings for our models."""
from django.core.exceptions import ValidationError

NAUGHTY_WORDS = {"frick"}


def no_naughty_words(word:str)->None:
    """Filter out all badwords. """
    print(type(NAUGHTY_WORDS))
    if word in NAUGHTY_WORDS:
        raise ValidationError(f"{word} is a bad word! Shame on you!")