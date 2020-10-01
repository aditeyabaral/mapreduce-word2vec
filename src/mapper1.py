#!/usr/bin/python3

import sys
from nltk.tokenize import word_tokenize

C = int(sys.argv[1].strip())
W = 2*C + 1

for line in sys.stdin:
    words = word_tokenize(line.strip())
    num_words = len(words)
    for i in range(num_words-W+1):
        window_words = words[i:i+W]
        middle_word = window_words[W//2]
        context_words = window_words[:W//2] + window_words[W//2+1:]
        print(f"{context_words}\t{middle_word}")
