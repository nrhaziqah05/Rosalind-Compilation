#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:46:16 2019

@author: haziqah
"""

import sys
import numpy as np
from Bio import SeqIO

def main():
    with open("/home/haziqah/anaconda2/Rosalind /Dataset/rosalind_bphr.txt") as f:
        threshold = int(f.readline().strip())
        fastq = np.array([rcd.letter_annotations["phred_quality"] for rcd in SeqIO.parse(f, "fastq")])
        fq = np.mean(fastq, axis=0)
    sys.stdout = open("bphr.out", "w")
    print len(fq[fq < threshold])

if __name__ == '__main__':
    main()