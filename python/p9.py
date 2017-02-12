#!/usr/bin/python

string1 = '[]'
string2 = '[[]]'
string3 = '[[[]]]'
string4 = ']['
string5 = '][]['
string6 = '[]][[]'

def brackets( str ):
    le = len(str)
    if le % 2 == 0:
        half = le / 2
        first = '[' * half
        last = ']' * half
        if str[0:half] == first and str[half:le] == last:
            return str, 'OK'
        else:
            return str, 'NOT OK'
    else:
        return str, 'NOT OK'

print brackets(string1)
print brackets(string2)
print brackets(string3)
print brackets(string4)
print brackets(string5)
print brackets(string6)
