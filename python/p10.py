#!/usr/bin/python

def char_freq( str ): 
    dict = {}
    print(str)
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]]= int(dict.get(str[i]))+1
        else:
            dict[str[i]]= 1
    print dict 
    return dict
         
char_freq("abbabcbdbabdbdbabababcbcbabahsdfjaaadasd")
