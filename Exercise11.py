
"""
Exercise 10:
    
    class Stack 
    A Stack is a mutable collection, a FILO (first in last out) collection
    A Stack has a maximum size (provided when the stack is created)
    You are limited to add elements at the end of the stack (with the help of the push() method)
    You can only have access to the element that is "on top" (at the end) of the stack
    (with the help of the pop() method)
    Note: the pop() method returns AND removes the element that is on top of the stack
    
    attributes:
        maxSize: an int (the maximum size of the stack)
        content: a list (used to store the stack's elements)
    methods:
        push()
        pop()
        __init__() # to control the way a stack is constructed -> s1=Stack(10) for instance
        __str__() # in order to control the way a Stack is printed (converted into a str)
        __len__() # in order to be able to use the len() function
        __eq__()  # to control how the == operator works when it is used to compare 2 stacks
        
"""

class Stack(list): # Now the class Stack "inherit from" list
# Stack is a subclass (derived or child) class of list
# list is a super (base or mother) class of Stack

    def __init__(self, size):
        if isinstance(size, int) and size > 0:
            self.maxSize=size
        else:
            raise Exception("Wrong stack size given")
    def __str__(self):
        return f"({len(self)}/{self.maxSize}) {super().__str__()}"

    def __eq__(self, other):
        return self.maxSize == other.maxSize and super().__eq__(other)

    def push(self, value):
        if len(self) >= self.maxSize: #The stack is full
            raise Exception("Stack full!")
        else:
            self.append(value)
    def pop(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return super().pop()

        
s1=Stack(10) # a stack of 10 elements (10 is a maximum)

s1.push(45)
s1.push(56)
s1.push(78)

print(s1) # (3/10) [45,56,78]

print(len(s1)) # 3

if 56 in s1:
#if s1.contains(56):
    print("56 is present in s1")
top=s1.pop()
print(top) # 78

print(s1) # (2/10) [45,56]

top=s1.pop()
print(top) # 56

print(s1) # (1/10) [45]

top=s1.pop()
print(top) # 45

print(s1) # (0/10) []
#top=s1.pop() # Exception raised

s2=Stack(10) # a stack of 10 elements (10 is a maximum)

s2.push(45)
s2.push(56)
s2.push(78)

print(s2)
s2.clear()
print(s2)

print(s1==s2)
s2.push(100)
print(s1==s2)


