#!/usr/bin/python3

import sys
import numpy as np

C = int(sys.argv[1].strip())
N = int(sys.argv[2].strip())
word2index = dict()

with open("../model/vocabulary") as vocabulary_file:
    content = vocabulary_file.read().strip().split('\n')
    for line in content:
        word, index = line.strip().split('\t')
        word2index[word] = int(index)

V = len(word2index.keys())

W1 = np.random.rand(N, V)
W2 = np.random.rand(V, N)
b1 = np.random.rand(N)
b2 = np.random.rand(V)

X = np.empty((V, 0))
y = np.empty((V, 0))

for line in sys.stdin:
    try:
        context_words, middle_word = line.strip().split('\t')
        context_words = eval(context_words.strip())
        middle_word = middle_word.strip()
    except ValueError:
        continue

    X_vector = np.zeros((V, 1))
    for context_word in context_words:
        context_word_index = word2index[context_word]
        word_vector = np.zeros((V, 1))
        word_vector[context_word_index] = 1.0
        X_vector += word_vector
    X_vector /= 2*C

    y_vector = np.zeros((V, 1))
    mapped_middle_index = word2index[middle_word]
    y_vector[mapped_middle_index] = 1.0

    X = np.hstack((X, X_vector))
    y = np.hstack((y, y_vector))

rows = X.shape[0]
for i in range(rows):
    print(f"{X[i]},{y[i]}")

np.save("../model/W1", W1)
np.save("../model/W2", W2)
np.save("../model/b1", b1)
np.save("../model/b2", b2)
