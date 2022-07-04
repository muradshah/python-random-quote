def hello_world():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__main__":
  hello_world()
