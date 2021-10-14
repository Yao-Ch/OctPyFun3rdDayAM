
l1=[5,6,7]
l2=[6,7,8,9]

l3=l1+l2
print(l3)


class ListPlus(list):
    def addList(li1, li2):
        li1_tmp=li1.copy() # li1_tmp=li1[:]
        li2_tmp=li2.copy()
        
        if len(li1) < len(li2):
            li1_tmp.extend([0]*(len(li2)-len(li1)))
            
        elif len(li2) < len(li1):
            li2_tmp.extend([0]*(len(li1)-len(li2)))   
            
        res=ListPlus()
        for i in range(len(li1_tmp)):
            res.append(li1_tmp[i]+li2_tmp[i])
        return res
    def __add__(li1, li2): # redefinition of +
        li1_tmp=li1.copy() # li1_tmp=li1[:]
        li2_tmp=li2.copy()
        
        if len(li1) < len(li2):
            li1_tmp.extend([0]*(len(li2)-len(li1)))
            
        elif len(li2) < len(li1):
            li2_tmp.extend([0]*(len(li1)-len(li2)))   
            
        res=ListPlus()
        for i in range(len(li1_tmp)):
            res.append(li1_tmp[i]+li2_tmp[i])
        return res
   

l1=ListPlus()
l1.append(45)
l1.insert(0,100)
print(l1)

l2=ListPlus()
l2.append(48)
l2.insert(0,120)
l2.append(49)
print(l2)

l3=l1.addList(l2)
print(l3)
l3=l1+l2
print(l3)

