import sys
import time
import replit
def slowPrint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.055)
def slowerPrint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.060)
def slowerprintfromfile(s):
    with open(s, "r") as f:
        slowerPrint(f.read())
        f.close()
def slowInput(s):
	slowPrint(s)
	replit.clear()
	return input(s)

reset = "\033[0m"
dim = "\033[2m"
underline = "\033[4m"
blue = "\033[1;34m"
red = "\033[1;91m"
green = "\033[1;32m"
flash = "\033[5m"