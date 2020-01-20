#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:25:07 2019

@author: haziqah
"""
import sys, numpy
from Bio import SeqIO

def main():
    with open("/home/haziqah/anaconda2/Rosalind /Dataset/rosalind_filt.txt") as f:
        threshold, percent = map(int, f.readline().strip().split(" "))
        fastq = list (SeqIO.parse(f, "fastq"))
        fastx = numpy.array([rcd.letter_annotations["phred_quality"] for rcd in fastq])
        fastx = numpy.array([len(rcd[rcd >= threshold]) * 100 / len(rcd) for rcd in fastx])
        sys.stdout = open("filt.out", "w")
        print len(fastx[fastx >= percent])

if __name__ == '__main__':
    main()