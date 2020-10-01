#!/usr/bin/python3

import sys

vocabulary = dict()

for line in sys.stdin:
    try:
        word, _ = line.strip().split('\t')
    except ValueError:
        continue
    vocabulary[word.strip()] = True

vocabulary_words = sorted(vocabulary.keys())

with open("../model/vocabulary", 'w') as vocabulary_file:
    for index, word in enumerate(vocabulary_words):
        vocabulary_file.write(f"{word}\t{index}\n")
