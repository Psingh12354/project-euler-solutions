
# -*- coding: utf-8 -*-
'''
    File name: odd_period_square_roots\solution__64.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #64 :: Odd period square roots
# 
# For more information see:
# https://projecteuler.net/problem=64

# Problem Statement 
'''
b'All square roots are periodic when written as continued fractions and can be written in the form:\n\n\xe2\x88\x9aN = a0 +\n1\n\xc2\xa0\na1 +\n1\n\xc2\xa0\n\xc2\xa0\na2 +\n1\n\xc2\xa0\n\xc2\xa0\n\xc2\xa0\na3 + ...\n\nFor example, let us consider \xe2\x88\x9a23:\n\n\xe2\x88\x9a23 = 4 + \xe2\x88\x9a23 \xe2\x80\x94 4 = 4 +\xc2\xa0\n1\n\xc2\xa0= 4 +\xc2\xa0\n1\n\xc2\xa0\n1\xe2\x88\x9a23\xe2\x80\x944\n\xc2\xa0\n1 +\xc2\xa0\n\xe2\x88\x9a23 \xe2\x80\x93 37\n\nIf we continue we would get the following expansion:\n\n\xe2\x88\x9a23 = 4 +\n1\n\xc2\xa0\n1 +\n1\n\xc2\xa0\n\xc2\xa0\n3 +\n1\n\xc2\xa0\n\xc2\xa0\n\xc2\xa0\n1 +\n1\n\xc2\xa0\n\xc2\xa0\n\xc2\xa0\n\xc2\xa0\n8 + ...\n\nThe process can be summarised as follows:\n\na0 = 4,\n\xc2\xa0\n1\xe2\x88\x9a23\xe2\x80\x944\n\xc2\xa0=\xc2\xa0\n\xe2\x88\x9a23+47\n\xc2\xa0=\xc2\xa01 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x9437\na1 = 1,\n\xc2\xa0\n7\xe2\x88\x9a23\xe2\x80\x943\n\xc2\xa0=\xc2\xa0\n7(\xe2\x88\x9a23+3)14\n\xc2\xa0=\xc2\xa03 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x9432\na2 = 3,\n\xc2\xa0\n2\xe2\x88\x9a23\xe2\x80\x943\n\xc2\xa0=\xc2\xa0\n2(\xe2\x88\x9a23+3)14\n\xc2\xa0=\xc2\xa01 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x9447\na3 = 1,\n\xc2\xa0\n7\xe2\x88\x9a23\xe2\x80\x944\n\xc2\xa0=\xc2\xa0\n7(\xe2\x88\x9a23+4)7\n\xc2\xa0=\xc2\xa08 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x944\na4 = 8,\n\xc2\xa0\n1\xe2\x88\x9a23\xe2\x80\x944\n\xc2\xa0=\xc2\xa0\n\xe2\x88\x9a23+47\n\xc2\xa0=\xc2\xa01 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x9437\na5 = 1,\n\xc2\xa0\n7\xe2\x88\x9a23\xe2\x80\x943\n\xc2\xa0=\xc2\xa0\n7(\xe2\x88\x9a23+3)14\n\xc2\xa0=\xc2\xa03 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x9432\na6 = 3,\n\xc2\xa0\n2\xe2\x88\x9a23\xe2\x80\x943\n\xc2\xa0=\xc2\xa0\n2(\xe2\x88\x9a23+3)14\n\xc2\xa0=\xc2\xa01 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x9447\na7 = 1,\n\xc2\xa0\n7\xe2\x88\x9a23\xe2\x80\x944\n\xc2\xa0=\xc2\xa0\n7(\xe2\x88\x9a23+4)7\n\xc2\xa0=\xc2\xa08 +\xc2\xa0\n\xe2\x88\x9a23\xe2\x80\x944\n\nIt can be seen that the sequence is repeating. For conciseness, we use the notation \xe2\x88\x9a23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.\n\nThe first ten continued fraction representations of (irrational) square roots are:\n\xe2\x88\x9a2=[1;(2)], period=1\n\xe2\x88\x9a3=[1;(1,2)], period=2\n\xe2\x88\x9a5=[2;(4)], period=1\n\xe2\x88\x9a6=[2;(2,4)], period=2\n\xe2\x88\x9a7=[2;(1,1,1,4)], period=4\n\xe2\x88\x9a8=[2;(1,4)], period=2\n\xe2\x88\x9a10=[3;(6)], period=1\n\xe2\x88\x9a11=[3;(3,6)], period=2\n\xe2\x88\x9a12= [3;(2,6)], period=2\n\xe2\x88\x9a13=[3;(1,1,1,1,6)], period=5\nExactly four continued fractions, for N \xe2\x89\xa4 13, have an odd period.\nHow many continued fractions for N \xe2\x89\xa4 10000 have an odd period?'
'''

# Solution 

# Solution Approach 
'''
'''
