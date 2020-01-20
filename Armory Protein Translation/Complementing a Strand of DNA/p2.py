#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 00:17:46 2019

@author: haziqah
"""

import sys
from Bio import SeqIO

def main():
    fasta = list (SeqIO.parse(open("/home/haziqah/anaconda2/Rosalind /Dataset/rosalind_rvco.txt"), "fasta"))
    sys.stdout = open("rvco.out", "w")
    print sum([seq.seq == seq.reverse_complement().seq for seq in fasta])

if __name__ == '__main__':
    main()
    
    