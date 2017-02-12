#!/usr/bin/python

def palindrome( str ):
    rev=""
    for i in str:
        rev = i + rev
    if rev == str:
        print "True"
        return rev
    else:
        print "False"
        return rev

palindrome("radar")
