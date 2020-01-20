#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 01:08:43 2019

@author: haziqah
"""
import sys
from Bio import SeqIO                      
sequences = []                             
handle = open('/home/haziqah/anaconda2/Rosalind /Dataset/rosalind_sseq.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    sequences.append(str(record.seq))      
handle.close()                             
s = sequences[0]                           
t = sequences[1]                           

pos = 0                                    
positions = []                             
for i in range(len(t)):                    
    for j in range(pos, len(s)):           
        pos += 1                           
        if len(positions) < len(t):        
            if t[i] == s[j]:               
                positions.append(pos)      
                break 
            
sys.stdout = open ("output.txt","w")                     
print(positions) 
   



