#!/usr/bin/python
#recursion

def dec_to_bin( n ):
    if n > 1:
        dec_to_bin(n/2)
        n = n % 2
    print n,

#dec_to_bin(15)

#loop
def dec_to_bin2( n ):
    if n == 0: 
        return "0"
    res = ''
    while n:
        if n & 1 == 1:
            res = "1" + res
        else:
            res = "0" + res
        n /= 2
    print res
    return res

print "with recursion"
dec_to_bin(15)
print " " 
print "with loop"
dec_to_bin2(15)
