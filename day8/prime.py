#First method 
def prime_checker(number):
  if number%2==0 or number%3==0:
    print("This is not a prime number")
  else:
    print("This is a prime number")


# Second method

n = int(input("Check this number: "))
prime_checker(number=n)

def prime_checker(number):
  is_prime=True
  for i in range(2,number):
    if number%i==0:
      is_prime=False
  if is_prime==True:
    print("this is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
