#!/bin/bash
ls -l / | awk '{print toupper($9)}'
