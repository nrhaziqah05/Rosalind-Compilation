#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 01:35:12 2019

@author: haziqah
"""

import sys
def main():
    with open("/home/haziqah/anaconda2/Rosalind /Dataset//rosalind_ini.txt") as f:
        seq = f.readline().strip()
        sys.stdout = open("ini.out","w")
        print " ".join(map(str, [seq.count(x) for x in ['A','C','G','T']]))

if __name__ == '__main__':
    main()
    