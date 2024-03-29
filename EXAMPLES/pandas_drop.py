#!/usr/bin/env python
'''

@author: jstrick
Created on Sun May 19 20:42:32 2013

'''
from pandas.core.frame import DataFrame
from printheader import print_header

cols = ['alpha','beta','gamma','delta','epsilon']
index = ['a','b','c','d','e','f']
values = [
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]
print_header('values:')
print(values, '\n\n')

df = DataFrame(values, index=index, columns=cols)
print_header('DataFrame df')
print(df, '\n')

df2 = df.drop(['beta','delta'], axis=1)
print_header("After dropping beta and delta:")
print(df2, '\n')

print_header("After dropping rows b, c, and e")
df3 = df.drop(['b','c','e'], axis=0)
print(df3)
