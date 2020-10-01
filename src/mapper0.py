#!/usr/bin/python3

import sys
from nltk.tokenize import word_tokenize

for line in sys.stdin:
    words = word_tokenize(line.strip())
    unique_words = list(set(words))
    for word in unique_words:
        print(f"{word}\t1")

