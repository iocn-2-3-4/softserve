#!/bin/bash
n=0
echo "enter 10 numbers, after each number press enter"
while [ $n -lt 10 ]
do
  read number
  array_n[n]=$number
  n=$(( $n + 1 ))
done

mult=1
for i in ${array_n[@]}; do
  let mult=$(($mult * $i))
done
echo "Result is: $mult"

