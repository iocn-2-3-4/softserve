#!/usr/bin/python

import time

def histogram( argument ):
    for i in range(0,len(argument)):
        time.sleep(1)
        print '*' * argument[i]
    return

histogram([4,9,15])
