

data=[56,78,78,90,100]
try:
    index=input("Enter an int in the range [0,4]: ")
    index=int(index)
    
    print(f"Element of data at position {index} is {data[index]}")
    print("End of try")
except:
    print("Exception raised")

print("The end")