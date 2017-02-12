#!/usr/bin/python

def sum_f( argument ):
    sum=0
    for element in argument:
        sum += element
    print sum
    return sum

def mult_f( argument ):
    mult=1
    for element in argument:
        mult *= element
    print mult
    return mult

sum_f([1,2,3,4])
mult_f([1,2,3,4])
