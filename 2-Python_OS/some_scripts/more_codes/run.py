#!/usr/bin/env python3

import subprocess
import os
if "new.py" in os.listdir():
	subprocess.run(["rm", "new.py"])

subprocess.run(["./change.py"])

if "new.txt" in os.listdir():
	subprocess.run(["mv", "new.txt","new.py"])
	subprocess.run(["chmod","+X","new.py"])
	subprocess.run(["cat","new.py"])

