#!/bin/bash
echo "first num"
read  first_num
echo "second_num"
read second_num
sum=$(($first_num + $second_num)) 
echo "sum is $sum"
