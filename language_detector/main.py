"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    for diction in languages:
        for word in diction['common_words']:
            for text_word in text.split():
                if word == text_word:
                    return diction['name']
    
    #return diction['name'] if word == text_word (for diction in languages) (for word in diction['common_words']) (for text_word in text.split()) 