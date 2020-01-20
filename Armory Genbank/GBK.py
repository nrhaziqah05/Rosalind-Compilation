#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:36:33 2019

@author: haziqah
"""

from Bio import Entrez

term = "Trigonia"
start = "2002/09/29"
end = "2007/12/17"

Entrez.email = "nhaziqah883@gmail.com"
handle = Entrez.esearch(db="nucleotide",term='"' + term + '"[Organism] AND ("' + start + '"[PDAT] : "' + end + '"[PDAT]"')
record = Entrez.read(handle)
print record["Count"]

