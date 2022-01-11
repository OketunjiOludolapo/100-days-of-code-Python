list_of_values=input("Enter the numbers and seperate them by a space ").split()


min_value=list_of_values[0]
sum_value=0
len_value=0
max_value=0
for i in list_of_values:
    i=int(i)
    sum_value+=i
    len_value+=1
    if i>max_value:
        max_value=i
    min_value=int(min_value)
    if i <min_value:
        min_value=i
print(type(min_value))




    
print(f"The min value is {min_value}\n The max is {max_value}\n The sum is {sum_value}\n The len is {len_value}")
