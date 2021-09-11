import math
import sys

print('Programs:')
print("Calculator")
print("Notepad")
print("Random Game")
print("Quit")

programcall = input("What program would you like to run: ")

if programcall == "Notepad":
  exec(open('notepad.py').read())

if programcall == "Calculator":
  exec(open('calculator.py').read())

if programcall == "Random Game":
  exec(open('randomgame.py').read())

if programcall == 'Quit':
  sys.exit("cmdOS Terminated")
