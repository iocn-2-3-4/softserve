#!/bin/bash
subtract () {
  c=$(($1-$2))
  echo $c
  }
    
subtract 12 512
subtract 623 98
subtract 12 0
subtract 0 23
