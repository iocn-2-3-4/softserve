#!/bin/bash
echo "enter three numbers, separated by space"
read n1 n2 n3

if [ $n1 -gt $n2 ]
then
echo " ";
if [ $n3 -gt $n2 ]
then
echo the smallest is: $n2;
else
echo the smallest is: $n3 ;
fi
elif [ $n2 -gt $n3 ]
then
echo the smallest is: $n3;
else
echo the smallest is: $n1;
fi


