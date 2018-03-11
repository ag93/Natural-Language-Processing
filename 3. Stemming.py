# -*- coding: utf-8 -*-

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

#example_words = ["dog","dogger","dogging","dogged","dogma"]
#for w in example_words:
#    print(ps.stem(w))
#    
    
new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))