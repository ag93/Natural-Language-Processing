# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 23:03:39 2018

@author: Aniket Gade
"""

from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Alderson! Are you Elliot? or is this daddy Alderson. You seem to be awful lot cheerful today! You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT)) #returns a list of sentences!

print(word_tokenize(EXAMPLE_TEXT)) #returns a list of words!