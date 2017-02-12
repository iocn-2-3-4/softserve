#!/usr/bin/python

def diaginal_reverse( matrix ):
    reversed_matrix = zip(*matrix)
    print "Input: ", matrix
    print "Output: ", reversed_matrix
    return matrix

diaginal_reverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

