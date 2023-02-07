"""Word Finder: finds random words from a dictionary."""

import random 

class WordFinder:
    """
    Class to read words from file and return a random word
    
    >>> wf = WordFinder('words.txt')
    235886 words read
    >>> word = wf.random()
    >>> word in wf.words 
    True
    >>> word = wf.random()
    >>> word in wf.words 
    True
 
    """    
    def __init__(self, filename):
        """Read dictionary and reports number of items read."""

        words_file = open(filename)

        self.words = self.parse(words_file)

        print(f"{len(self.words)} words read")

    def parse(self, words_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in words_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)
        
