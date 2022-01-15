import math

def paint_calc(height,width,cover):
  """A function that calculates the approximate total number of paint cans needed for a particular area and rounds it up if it's not a whole number"""
  no_of_cans=math.ceil((height*width)/cover)
  print(no_of_cans)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
