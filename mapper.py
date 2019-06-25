#!/usr/bin/python3

import sys
import re

WINDOW = 2

for line in sys.stdin:
    pattern = r'[\?!\.]'
    sentences = re.split(pattern, line)
    for sentence in sentences:
        sentence = sentence.strip()
        words = re.split(r'\s+', sentence)
        for idx in range(len(words) - 1):
            sorted_words = sorted([words[idx], words[idx+1]])
            print('{}.{}\t1'.format(sorted_words[0], sorted_words[1]))


# import sys

# for line in sys.stdin:
#     words = line.lower().split()
#     for w in words:
#         print('{}\t1'.format(w))
