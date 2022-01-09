print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Hello Pirate,Welcome to Treasure Island.")
print("Your mission is to find the treasure which we know pirates can't resist🤩.")


choice1 = input('You are in front of a cave. Do you go in or you leave without the treasure? Type "in" or "leave" \n').lower()
if choice1 == "in":
  choice2 = input("You are at a crossroad within the cave, do you go left or right?Type 'left' or 'right' \n").lower()
  if choice2 == "right":
    choice3 = input("You are almost at the other end of the cave. There are two entrances. One of it will lead to the other end of the cave.\
One of the entrances has a pretty siren guarding it while the other has a scary bouncer guarding it . Which entrance do you choose?\
Type 'siren' or 'bouncer' \n").lower()
    if choice3 == "siren":
      print("You got baited by beauty,pirate. No one follows a siren and get out again.Game Over.")
    elif choice3 == "bouncer":
        choice4=input("You are inside another cave. There are two roads. do you go left or right? Type 'left' or 'right'\n")
        if choice4=="right":
            print("You did it. The treasure is finally yours. You win!!!")
        else:
            print("Almost there but not there. You enterd into a dragon room. Game over")
    else:
      print("You choose an entrance that doesn't exist. Game Over.")
  else:
    print("You got into a room full of snakes and got bitten. Game Over")
else:
  print("Oh no! You disappointed your crew captain. That was not so pirate-y of you. Bye and never come back")







