#!/bin/bash
ls -l / | sed  'N;s/.*/&\nnew_line/' | sed '1~3d'
