
fic=open("data3.txt")


for line in fic:
    if line.startswith("error"):
        continue
    print(line)
    
fic.close()
