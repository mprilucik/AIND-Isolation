# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:11:04 2017

@author: mprilucik
"""

from numpy import cross, subtract
from numpy.linalg import norm


#distance  6.0 my_loc (1, 0) opp_loc (1, 4)
#distance  8.0 my_loc (1, 0) opp_loc (3, 0)
#distance  8.0 my_loc (2, 3) opp_loc (0, 3)

opp_loc = (0,0)
my_loc = (8,8)
sub = subtract(opp_loc, my_loc)
dist = norm(subtract(my_loc,opp_loc))

print (sub, dist)