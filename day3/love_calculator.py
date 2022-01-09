# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")

#asking for the names
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()


#Calculating their love score
concate_both=name1+name2
t=concate_both.count("t")
r=concate_both.count("r")
u=concate_both.count("u")
e=concate_both.count("e")

true=t+r+u+e

l=concate_both.count("l")
o=concate_both.count("o")
v=concate_both.count("v")
e=concate_both.count("e")

love=l+o+v+e

score=int(str(true)+str(love))


if (score < 10) or (score >90):
  print(f"Your love score is {score},you go together like coke and mentos.")
elif (score>=40) and (score<=50):
  print(f"Your score is {score},you are alright together")
else:
  print(f"Your score is {score}, you are not compatible")