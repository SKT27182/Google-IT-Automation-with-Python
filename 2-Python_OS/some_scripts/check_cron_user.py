#!/usr/bin/env python3
import re
import sys
import os
from to_parent import change_dir_to_parent

change_dir_to_parent()
os.chdir("data")

#takes the input of the syslog file from environment
logfile = sys.argv[1]  #syslog

usernames = {}


with open(os.path.abspath(logfile)) as file:
	for line in file:
		#if CRON is not present in line then username is also not present in that line
		if "CRON" not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)
		if result is None:
			continue
		name = result[1]
		usernames[name] = usernames.get(name,0) + 1
print(usernames)
