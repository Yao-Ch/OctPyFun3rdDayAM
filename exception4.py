

data=[56,78,78,90,100]

while True:
    try:
        index=input("Enter an int in the range [0,4]: ")
        index=int(index)
        print(f"Element of data at position {index} is {data[index]}")
        break
    except IndexError as e:
        print("IndexError raised:", e)
    except ValueError as e:
        print("ValueError raised:", e)
    
print("The end")