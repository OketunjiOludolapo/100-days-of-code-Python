
print("Welcome to Python Pizza Deliveries!\n")

#Asking for user's preference
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Conditional statements to calculate bill
bill=0
if size=="S":
  bill+=15
  

elif size=="M":
  bill+=20
  

else:
  bill+=25
  

if add_pepperoni=="Y":
  if size=="S":
    bill+=2
  else:
    bill+=3
  
else:
  bill+=3

if extra_cheese=="Y":
  bill+=1

print(f"Your final bill is ${bill}, your pizza will be delivered with 10 minutes. Pls pay with your card when the rider arrives")
 





