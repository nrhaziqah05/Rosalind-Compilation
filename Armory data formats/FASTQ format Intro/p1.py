#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:27:04 2019

@author: haziqah
"""

from Bio import SeqIO
records = SeqIO.parse("/home/haziqah/anaconda2/Rosalind /Dataset/rosalind_tfsq.txt", "fastq")
count = SeqIO.write(records, "my_example.fasta", "fasta")
print("Converted %i records" % count)
