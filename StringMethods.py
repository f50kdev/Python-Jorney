from traceback import print_tb

from primititveType import firstName


course = " python progrmaing  ";
#callingMathods
print(course.upper());
print(course.lower());
print(course.title());
print(course.strip())
print(course.lstrip())

if "bolls" in course:
      print(course);
else:
      print("false message");

if "bools" in course:
    value = input("inser your name");
else: 
    print(course);

    print(course.replace("p" , "c"))

    print("co" not in course);

    myfirst_name = "fausrtino"; 
    mysecond_name = "Henriques"; 

    #full  = myfirst_name + " "+ mysecond_name;
    full  = f" {int(len(myfirst_name))} +  {int(len(mysecond_name))}";
print(full)

#Methods in strings

hacking = "bsidesHacking";

hacking.isnumeric();
havluer_methods = hacking.upper();
print(havluer_methods);

print(hacking.find("sides"))
print(hacking.replace("h" , "H"));
print()




