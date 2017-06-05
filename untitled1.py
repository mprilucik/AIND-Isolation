# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:30:08 2017

@author: Petruska
"""
import re
with open('tournament_history2.txt','r') as f:
    for l in f:
        if 'Rate' in l:
            l.replace('%','')
            l.replace('.',',')
#            print (l, re.findall('(\d+\.\d)', l))
            numbers = re.findall('(\d+\.\d)', l)
            print (','.join(numbers))
            
    