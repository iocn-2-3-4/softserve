#/usr/bin/python

import sys,os

path = sys.argv[1]
prefix = sys.argv[2]
counts = sys.argv[3]
mode = sys.argv[4]

path = path + "/" + prefix
print path
for i in range (1, int(counts)):
    result = os.mkdir(path+str(i),int(mode))

print('Folders are created')

