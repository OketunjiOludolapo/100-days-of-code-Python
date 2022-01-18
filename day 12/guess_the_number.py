
import random
from app import game_logo

print(game_logo)
import random #the module to make the game interesting
numbers=list(range(1,101)) #a predefined range of numbers between 1-100
def number():
    """A function for the script to generate a random number that the player will guess against"""

  actual_number=random.choice(numbers)
  return actual_number #The program's random number

def user_guess():
    """A function to accept player's guess"""
  user_pick=int(input("Enter a number: "))
  return user_pick

def play():
    """The function to play the game"""
  game_over=False
  num=number()
  print(num)
  choose=input("Choose Easy for easy mode or Hard for hard mode: ").lower()
  if choose=="easy":
      print("You have 10 lives to use")
      lives=10
  elif choose=="hard":
    lives=5
    print("You have 5 lives to use")
  else:
    print("Enter a valid response")
  while not game_over:
    lives-=1
    guess=user_guess()
    if lives==0:
      print("You have no more lives. Game Over")
      game_over=True
    else:
      if guess==num:
        print(f"The number was {num} and your guess was {guess}.You Win!!!")
        game_over=True
      elif guess < num:
        print("Too Low")
        print(f"You have {lives} left")
      elif guess > num:
        print("Too High")
        print(f"You have {lives} left")

play() #Calling the function and playing the game

#Looping so that the player can play again after a win or lose
while input("Would you like to play again? Enter y or n ")=="y":
  play()