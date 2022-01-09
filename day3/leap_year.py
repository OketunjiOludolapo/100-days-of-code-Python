print("A program for checking if a year is a leap year\n")

#asking for the year
year = int(input("Which year do you want to check? "))

#conditional statements that evaluates if the year is a leap year or not
if year%4==0:
  if year%100==0:
    if year%400:
      print("leap year")
    else:
      print("Not a leap year")
  else:
    print("leap year")
else:
  print("Not a leap year")
