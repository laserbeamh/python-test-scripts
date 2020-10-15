def decor(func):
  def wrap():
    print("##########")
    func()
    print("##########")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()

#also works as:
#@decor
#def print_text():
#  print("Hello world!")
#
#print_text();
