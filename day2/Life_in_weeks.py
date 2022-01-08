print("Life remaining with the assumption of totla years as 90\n")

#Asking for the user's current age
age=input("what is your current age? ")

# Converting to Int
age_as_int=int(age)

#Calculation
years_remaining= 90-age_as_int

months_remaining= years_remaining*12

weeks_remaining= years_remaining*52

days_remaining= years_remaining*365

total_remaining=f"Assuming you would live to 90 years, you have {years_remaining} years left,{months_remaining} months remaining,\
{weeks_remaining} weeks remaining and {days_remaining} days left. Ensure you use them wisely. Good Luck!!!"

print(total_remaining)
