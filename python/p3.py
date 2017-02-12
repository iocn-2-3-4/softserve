#!/usr/bin/python

def reverse( str ):
    rev=""
    for i in str:
        rev = i + rev
    return rev

print(reverse("I'm testing"))
