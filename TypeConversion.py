#geting value from  user

import math



Name = input("Inser Your name ");
print(f" welcome Mister {Name}");

print(f"Mister {Name} inser the first value");
firstValue = int(input("Insert the value"));
secondValue   = int(input("Insert the value "))

total = firstValue + secondValue;

print(f"The total of value sum is : {total}");

if math.sqrt(total) < 1 :
    print(" value is not valid")
else: 
    print("try again");