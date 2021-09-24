name1 = input("enter a name (last name first) ")
name2 = input("enter another name (last name first) ")

print('order alphabetic names')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)