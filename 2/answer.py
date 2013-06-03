#!/usr/bin/env python

import collections

# find the rare characters by using a defaultdict to count up the
# characters. remember their order to reveal the answer!
counter = collections.defaultdict(int)
character_order = []
with open('raw_data.txt', 'r') as stream:
    for line in stream:
        for c in line.strip():
            counter[c] += 1
            if c not in character_order:
                character_order.append(c)
answer = []
for c in character_order:
    if counter[c]==1:
        answer.append(c)
print ''.join(answer)
