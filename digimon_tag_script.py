#!/usr/bin/env python3
""" Tag script | by Rob Womble
    script to determine ideal button
    sequence for consistent results
    in tag training on
    Digimon 20th anniversary vpet"""

# not sure if I need the whole module or just one function
import itertools


# tuple of tuples containing the sequences to beat
BATTLE_SEQUENCES = (
    ('A', 'B', 'A', 'B', 'A'),
    ('A', 'B', 'A', 'B', 'B'),
    ('B', 'B', 'A', 'A', 'B'),
    ('B', 'A', 'A', 'B', 'B'),
    ('A', 'B', 'B', 'A', 'A'),
    ('B', 'A', 'B', 'A', 'B')
                   )

# generate all possible input sequences
input_sequences = itertools.product('AB', repeat=6)

# function to determine if listed sequence wins
## testing zip
example_a = ('A', 'A', 'A', 'A', 'A')
example_b = ('B', 'B', 'B', 'B', 'B')
example_c = ('A', 'B', 'A', 'B', 'A')

for comp in zip(example_a, example_c):
    print(comp[0] == comp[1])
print('\n')
for comp in zip(example_b, example_c):
    print(comp[0] == comp[1])
