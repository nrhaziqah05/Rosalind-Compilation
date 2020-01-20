#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 00:13:41 2019

@author: haziqah
"""

import sys
from Bio.Seq import translate

def main():
    with open("/home/haziqah/anaconda2/Rosalind /Dataset/rosalind_ptra.txt") as f:
        dna, aa = f.read().strip().split("\n")
    sys.stdout = open("ptra.out", "w")
    for code_var in range(1, 7) + range(9, 16):
        if translate(dna, table=code_var, to_stop=True) == aa:
            print code_var,

if __name__ == '__main__':
    main()
    