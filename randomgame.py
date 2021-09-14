import random
import math
import os

charhealth = 100
pikahealth = 100
squrhealth = 100

pokerandom = [1, 2, 3]
pikahit = [1, 2]

gamepicker = input("Pick a number between 1 - 3: ")

if gamepicker == "1":
  headsortails = input("Heads or Tails: ")

  if headsortails == "Heads":
    coinflip = [1, 2]
    
    if random.choice(coinflip) == 1:
      print("Heads!")

    else:
      print("Tails!")

if gamepicker == "2":
  os.system('clear')
  print("Welcome to PyMon!")
  print("Pikapoo")
  print("Charmanader")
  print("Squirrleturle")

  pokepicker = input("Pick your PyMon: ")

  if pokepicker == "Pikapoo":
    print("Pikapoo! Great Choice!")
    print("A challenger appears!")

    keepon = input("Fight? ")

    if keepon == "yes":

     if random.choice(pokerandom) == 1:
       print("Charmanader approaches!")
       print("Available Attacks:")
       print("Electro Ball")
       print("Smack")

       attack = input("What attack will you use: ")

       if attack == "Electro Ball":

         if random.choice(pikahit) == 1:
           print(charhealth - 25 + "Nice Hit!")
  
