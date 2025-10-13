from email import message


temperature = 35;
if temperature >> 30:
  print("It's warm ");
  print("isn't warm");
elif temperature != 30:
  print("true")
else: 
  print("false")
print("not Done")


#ternary operator \
age = 22 ; 
if age >=18:
  message = " eligible"
else:
  message = " not eligible";

print(message);

alerta = "value added" if  age >= 30 else "not added";
print(alerta);

comparando =  age = age-10 if  age <= 2  else input(" inser your value");


#logicals 

high_income = true ; 
good_credit = true; 
if high_income and good_credit: 
  print("eligible");
else:
  print("not eligible");