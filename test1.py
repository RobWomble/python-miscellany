#!/usr/bin/env python3
""" testing toolbox functions """

import toolbox

IF = "userdata/samplelines.txt"

sample1 = toolbox.strdictfromfile(IF)
print(sample1)
sample2 = toolbox.intdictfromfile(IF)
print(sample2)
