import os

readorwrite = input("Write or Read a file? ")

if readorwrite == "Write":

 print("File 1")
 print("File 2")
 print("File 3")
 print("File 4")
 pickfile = input("What file do you want to write in? ")

 if pickfile == "1":
  writeinfo = input("Type Here: ")

  f = open("notepadfiles/notepadstorage.txt", "w")
  f.write(writeinfo)
  f.close()

 if pickfile == "2":
   writeinfo = input("Type Here: ")

   f = open("notepadfiles/notepadstorage2.txt", "w")
   f.write(writeinfo)
   f.close()

 if pickfile == "3":
   writeinfo = input("Type Here: ")

   f = open("notepadfiles/notepadstorage3.txt", "w")
   f.write(writeinfo)
   f.close()

 if pickfile == "4":
   writeinfo = input("Type Here: ")

   f = open("notepadfiles/notepadstorage4.txt", "w")
   f.write(writeinfo)
   f.close()
