#!/bin/bash
echo "enter catalog name"
read cat_name
mkdir $HOME/$cat_name
cat_name=$HOME/$cat_name
echo "enter path to folder which you need to copy"
read folder
cp -r $folder/* $cat_name
