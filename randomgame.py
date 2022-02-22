import random
import math
import os

charhealth = 100
charint = 'Charmanaders Health is now at '
squrhealth = 100
squrint = 'Squirrleturles Health is now at '
pikahealth = 100
pikaint = 'Pikapoos Health is now at '

pokerandom = [1, 2, 3]
pikahit = [1, 2]
pikasmack = [1, 2]
charhit = [1, 2]
charsmack = [1, 2]
squrhit = [1 , 2]
sqursmack = [1, 2]
coinflip = [1, 2]

gamepicker = input("Pick a number between 1 - 3: ")

if gamepicker == "1":
  headsortails = input("Heads or Tails: ")

  if headsortails == "Heads":
    if random.choice(coinflip) == 1:
      print("Heads!")

    if random.choice(coinflip) == 2:
      print("Tails!")

  if headsortails == "Tails":
    if random.choice(coinflip) == 1:
      print("Heads!")
    
    if random.choice(coinflip) == 2:
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

    if keepon == "y":
      if random.choice(pokerandom) == 1:
        print("Charmanader approaches!")
        print("Available Attacks:")
        print("Electro Ball")
        print("Smack")

        while charhealth > 0:
         attack = input("What attack will you use: ")

         if attack == "Electro Ball":
          if random.choice(pikahit) == 1:
            charhealth = charhealth - 25
            print(charint + str(charhealth))
            
          if random.choice(pikahit) == 2:
            charhealth = charhealth - 50
            print(charint + str(charhealth))

         if attack == "Smack":
          if random.choice(pikasmack) == 1:
            charhealth = charhealth - 15
            print(charint + str(charhealth))

          if random.choice(pikasmack) == 2:
            charhealth = charhealth - 35
            print(charint + str(charhealth))

        if charhealth <= 0:
          print("Charmanader Fainted!")
          
          playagain = input("Play Again? ")

          if playagain == "y":
            os.system('clear')
            exec(open('randomgame.py').read())
          
          if playagain == "n":
            os.system('clear')
            exec(open('main.py').read())

      if random.choice(pokerandom) == 2:
        print("Squirrleturle approaches!")
        print("Available Attacks")
        print("Electro Ball")
        print("Smack")

        while squrhealth > 0:
         attack2 = input("What attack will you use: ")

         if attack2 == "Electro Ball":
          if random.choice(pikahit) == 1:
            squrhealth = squrhealth - 35
            print(squrint + str(squrhealth))

          if random.choice(pikahit) == 2:
            squrhealth = squrhealth - 60
            print(squrint + str(squrhealth))

         if attack2 == "Smack":
          if random.choice(pikasmack) == 1:
            squrhealth = squrhealth - 20
            print(squrint + str(squrhealth))

          if random.choice(pikasmack) == 2:
            squrhealth = squrhealth - 40
            print(squrint + str(squrhealth))

        if squrhealth <= 0:
          print("Squirrleturle Fainted!")
          playagain = input("Play Again? ")

          if playagain == "y":
            os.system('clear')
            exec(open('randomgame.py').read())
          
          if playagain == "n":
            os.system('clear')
            exec(open('main.py').read())

      if random.choice(pokerandom) == 3:
        print("Pikapoo Appears!")
        print("Available Attacks:")
        print("Electro Ball")
        print("Smack")
