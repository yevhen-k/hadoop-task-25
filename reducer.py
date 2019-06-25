#!/usr/bin/python3

import sys
from itertools import groupby

for key, group in groupby((l.split('\t') for l in sys.stdin), key=lambda x: x[0]):
    words = key.split('.')
    print('{} {}\t{}'.format(words[0], words[1], sum(int(g[1]) for g in group)))


# import sys
# from itertools import groupby

# for key, group in groupby((l.split('\t') for l in sys.stdin), key=lambda x: x[0]):
#     print('{}\t{}'.format(key, sum(int(g[1]) for g in group)))
