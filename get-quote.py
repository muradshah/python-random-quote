import random
from re import A
from tkinter import W


def hello_world():

  f = open("quotes.txt", 'a')
  L = "This is programaticly added qoute \n"
  f.write(L)
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 21
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)

  print (quotes[rnd1], end="")
  print (quotes[rnd2])

if __name__== "__main__":
  hello_world()
