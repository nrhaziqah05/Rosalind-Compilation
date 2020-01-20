#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 07:31:41 2019

@author: norhaziqah
"""

import urllib2
import re
list = ['Q5WFN0',
'P01044_KNH1_BOVIN',
'P13473_LMP2_HUMAN',
'P02974_FMM1_NEIGO',
'P01217_GLHA_BOVIN',
'P02748_CO9_HUMAN',
'A1TJ10',
'P23185',
'A5GVY9',
'A9QYN2',
'Q2YCH6',
'P04441_HG2A_MOUSE',
'P00748_FA12_HUMAN'
]
 
for one in list:
    name = one.strip('\n')
    url = 'http://www.uniprot.org/uniprot/'+name+'.fasta'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    start = the_page.find('\nM')
    seq = the_page[start+1:].replace('\n','')
    seq = ' '+seq
    regex = re.compile(r'N(?=[^P][ST][^P])')
    index = 0
    out = []
    '''
    out = [m.start() for m in re.finditer(regex, seq)]
    '''
    index = 0
    while(index<len(seq)):
        index += 1
 
        if re.search(regex,seq[index:]) == None:
            break

        #print S[index:]
        if re.match(regex,seq[index:]) != None:
            out.append(index)
 
    if out != []:
        print name
        print ' '.join([ str(i) for i in out])