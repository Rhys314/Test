# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:14:28 2016
Test script.
@author: Rhys Poolman
"""
import spiceypy as spice
import numpy as np

# print out the toolkit version
#print(spice.tkvrsn('TOOLKIT'))

spice.furnsh('./cassini_kernel/cassMetaK.txt')

step = 4000

# we are going to get positions between these two dates
utc = ['Jun 20, 2004', 'Dec 1, 2005']

# get et values one and two, we could vectorize str2et
etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
print('Et One: {}, ET Two: {}'.format(etOne, etTwo))
