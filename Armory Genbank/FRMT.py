#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:49:39 2019

@author: haziqah
"""
from Bio import Entrez
from Bio import SeqIO
Entrez.email = "nhaziqah883@gmail.com"
handle = Entrez.efetch(db ="nucleotide", id=["JX491654, JX308821, NM_001135551, JX460804, JX914595, JQ011270, FJ817486, JX295575"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))

shortest=0
length=0

for x in range(0, len(records)):
    rec = records[x].seq
    lengthC = len(rec)
    if x==0:
        length=lengthC
    else:
        if lengthC < length:
            shortest = x
            length = lengthC
            
print records[shortest].description
print records[shortest].seq

