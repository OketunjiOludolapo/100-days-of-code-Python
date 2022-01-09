print("An app for checking your bmi and it's implication\n")

#asking for user's info
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#bmi calculation
bmi=weight/height**2

# Conditional statements depending on the bmi score
if bmi<18.5:
  print(f"Your bmi is {bmi},thus you are underweight")
elif bmi>18.5 and bmi<25:
  print(f"Your bmi is {bmi},thus you have normal weight")
elif bmi>25 and bmi<35:
  print(f"Your bmi is {bmi},thus you are obese")
else:
  print(f"Your bmi is {bmi},thus you are clinically obese")
