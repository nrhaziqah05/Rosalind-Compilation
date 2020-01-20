#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:08:15 2019

@author: haziqah
"""

import sys
from Bio import SeqIO

def hamming(s1, s2):
    # Return the Hamming distance between equal-length sequences
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def main():
    dna = list (SeqIO.parse(open("/home/haziqah/anaconda2/Rosalind /Dataset/rosalind_subo.txt"), "fasta"))
    # Run LALIGN with +4/-8 Matrix, -8 Gap Open/Extend, and pick the 100% match.
    r = 'TCGCGACGTCATGGAGCGCCGTGGGATTCAAGCCTAA'
    count = [sum([hamming(dna[seq_num][i:i + len(r)], r) <= 3 for i in \
            xrange(len(dna[seq_num]) - len(r) + 1)]) for seq_num in xrange(2)]
    sys.stdout = open("suboANS.out", "w")
    print ' '.join(map(str, count))

if __name__ == '__main__':
    main()
    