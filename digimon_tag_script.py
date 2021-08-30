#!/usr/bin/env python3
""" digimon tag script
    by Rob Womble       """

from itertools import product

''' The purpose of this script was to solve an issue I had been
    wracking my mind over.

    I had recently dug out my Digimon 20th Anniversary V-Pet
    with the intention of starting a new set of mons.  For those
    unaware, digmon v-pet toys are similar to the tomagotchi toys of
    olden days in that one cares for a virtual creature. The difference
    in digimon is that these creatures are also trained to do battle
    with each other.  In the 20th anniversary model in particular, you
    raise two digimon at a time, and they can engage in tag team battles
    or train together. The team training worked as a guessing game,
    where pressing the A button would cause the creature you're
    controlling to attack high and the B button would attack low. The
    other creature would then block high or low, seemingly at random.
    This would occur 5 times, and if 3 of your 5 attacks hit, the
    training session would count as a success and improve the combat
    ability of both creatures.

    While refamiliarizing myself with the functions of the unit, I
    recalled discovering previously that there were only six different
    patterns that the system used to determine where the opposing
    creaturee would block.  I decided to embark on an attempt to find
    the perfect attack sequence that would defeat all 6 patterns.    '''

# these are the inputs to beat the block patterns
BATTLE_SEQUENCES = (
    ('A', 'B', 'A', 'B', 'A'),
    ('A', 'B', 'A', 'B', 'B'),
    ('B', 'B', 'A', 'A', 'B'),
    ('B', 'A', 'A', 'B', 'B'),
    ('A', 'B', 'B', 'A', 'A'),
    ('B', 'A', 'B', 'A', 'B')
                   )

# generator for all possible input sequences
input_sequences = product('AB', repeat=5)


def winner(tested, target):
    ''' compare the two sequences,
        return true if 3 of 5 match '''
    win_count = 0
    for comp in zip(tested, target):
        if comp[0] == comp[1]:
            win_count += 1
    return bool(win_count > 2)


def success_count(test_list, target_collection):
    ''' compare the sequence against the list of
        sequences and return how many of them win   '''
    successes = 0
    for battle in target_collection:
        if winner(test_list, battle):
            successes += 1
        else:
            continue
    return successes


def main():
    ''' check every possible sequence to see how many it wins,
        print if it meets criteria                              '''
    for attempt in input_sequences:
        wins = success_count(attempt, BATTLE_SEQUENCES)
        if wins > 3:
            print(attempt)
        else:
            continue


if __name__ == "__main__":
    main()


""" In the end, the experiment was technically a failure.

    I was unable to get a sequence that wins every time.  In hindsight,
    I suppose that's why the developers programmed 6 of them: to
    prevent the user from finding a win button and reducing the game
    to repetition. It was redundant to make 6, as I couldn't find a
    sequence that wins in 5 of the 6 patterns, either. I did find
    several that win 4 out of 6 times, so perhaps I'll come back to
    this to find a sequence that can tell me quickly if I'll need to
    change the last input or two.

    In the meantime, I've learned to use for the zip() function, and
    discovered the itertools module, so as a python practice script,
    this was a rousing success.                                     """
