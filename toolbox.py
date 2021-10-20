#!/usr/bin/env python3
""" Function Toolbox
    by Rob Womble
    A script to store functions that I foresee reusing """

# I'm putting this statement at the top so I can append future
# functions to the bottom
if __name__ == "__main__":
    print("This script does nothing by itself.")
    exit()


def intdictfromfile(infile):
    ''' returns a dictionary;
        keys come from input file,
        values are int(0)           '''
    newdict = dict()
    with open(infile, "r") as source:
        for i in source.readlines():
            newdict[i.strip()] = 0
    return newdict


def strdictfromfile(infile):
    ''' returns a dictionary;
        keys come from input file,
        values are empty strings    '''
    newdict = dict()
    with open(infile, "r") as source:
        for i in source.readlines():
            newdict[i.strip()] = ""
    return newdict
