#/usr/bin/python

import sys,os

def create_folders(path,prefix,counts,mode):
    path = path + "/" + prefix
    try:
        for i in range (1, int(counts)):
            result = os.mkdir(path + str(i), int(mode))
    except OSError:
        print('Something went wrong')
    else:
        print('Folders are created')

if __name__ == '__main__':
    create_folders(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
