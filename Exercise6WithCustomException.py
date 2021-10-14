class IsPrimeError(Exception):
    pass

def isPrime(nb):
    if not isinstance(nb, int): # Error: an int should be provided!!!
        e=IsPrimeError("Wrong type of argument received")
        raise e
        
    if nb < 0: # Error: a positive int should be provided!!!
        # print("Negative argument received")
        # return None
        raise IsPrimeError("Negative argument received")
  
    if nb in [0,1]: # <=>   if nb==0 or nb==1:
        return False # 0 and 1 are not a prime numbers
    
    ix=2
    while ix < nb:   
    
        if nb % ix == 0:        # If ix is a divisor of nb:
            return False        #       nb is not a prime number
        
        ix += 1
        
    # for ix in range(2,nb):   
    #     if nb % ix == 0:        # If ix is a divisor of nb :
    #         return False        # 		nb is not a prime number
      
    return True # If we have reach this point, it means nb is a prime number


numbers=[-22,6,78,"abc",6,89,23]

for nb in numbers:
    if isPrime(nb) == True:
        print(f"{nb} is a prime number")
    else:
        print(f"{nb} is not a prime number")
        
        
        
        
        