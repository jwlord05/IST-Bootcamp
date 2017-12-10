primeList = []
# check for factors
for num in range(2,20):
    if num > 1 and len(primeList) != 5:
        for i in range(2,num):
            if (num % i) == 0:
               break
        else:
            primeList.append(num)
            print(num,"is a prime number")
       
print(primeList)

'''

primeList = [] 
# check for factors 
for num in range(2,101): 
    if num > 1 and len(primeList) != 5: 
        for i in range(2,num): 
            if (num % i) == 0: 
               break 
        else: 
            primeList.append(num) 
            
            
print (primeList)


'''

import random

#Write a short program which creates a list of the first 5 prime numbers

primeList = [] 
# check for factors 
for num in range(2,101): 
    if num > 1 and len(primeList) != 5: 
        for i in range(2,num): 
            if (num % i) == 0: 
               break 
        else: 
            primeList.append(num) 
            
            
print (primeList)

#Create a tuple a which contains the first four positive integers and a tuple b which contains the next four positive integers.

a = (1,2,3,4)
b = (5,6,7,8)

print (a) ; print (b)

ab = (a+b)

print(ab)

print(ab[:4])

#Create a tuple c which combines all the numbers from a and b in any order.

for val in range(0,5):
    
    print(str(random.choice(ab)) + ", ",end='')
    
#Print the length of  c 

print ("\n",len(ab))

print (ab)
