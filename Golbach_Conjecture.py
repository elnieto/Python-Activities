def createprimelist(max):
    'Creates a list of prime number up to the given range.'
    primelist = []
    baseprime = [2,3,5,7]
    for j in range(2, max+1): 
        for i in baseprime:
            if j % i == 0:
                break
            else:
                continue
                primelist.append(j)
        break
    return primelist
createprimelist(30)

#####test
start = 11
end = 25
  
for val in range(1, end + 1): 
      
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 
#####test

even = [2,4,6]
prime  = [1,2,3,5]

for n in even:
    count = 0
        for j in prime:
            for i in range (j+1):
                answ = j+i
                if n == answ:
                    count = 1
                    while count == 0:
                        print(j,' + ', i,' = ', n)
                else:
                    None

