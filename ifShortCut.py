

nb=input("Enter an int: ")
nb=int(nb)

if nb>=0:
    absNb=nb
else:
    absNb=-nb
    
print(f"Abs value of {nb} is {absNb}")


# The shortcut:
    
absNb = nb if nb>=0 else -nb
    
print(f"Abs value of {nb} is {absNb}")