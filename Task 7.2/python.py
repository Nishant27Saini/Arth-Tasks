#!/usr/bin/python3
print("Content-type: text/html")
print()

import subprocess
X=subprocess.getoutput("date")
print(X)
