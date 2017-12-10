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
