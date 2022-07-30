#!/usr/bin/env python3
import os
import re
import sys


p= r"-1"
file = "try.txt"

file2 = open("new.txt", 'a')

with open(file) as f:
	for line in f.readlines():
		if '-1' in line:
			l = line.replace('-1',' ')
			file2.write(l)
		else:
			file2.write(line)

file2.close()

			
