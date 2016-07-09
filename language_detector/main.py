"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    counter = {}
    for diction in languages:
        counter[diction['name']] = 0
        for word in diction['common_words']:
            for text_word in text.split():
                if word == text_word:
                    counter[diction['name']] += 1
    
    return max(counter, key = counter.get)
    
    # return [k for k, v in counter.items() if v == max(counter.values())][0]
    # pre-converted list comp 
    # for k, v in counter.items():
    #     if v == max(counter.values()):
    #         return k
            
    # attempted list comp before adding counter         
    # return diction['name'] for diction in languages for word in diction['common_words'] for text_word in text.split() if word == text_word