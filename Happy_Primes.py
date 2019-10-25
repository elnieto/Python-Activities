#Elizabeth Nieto
#10/08/19
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/pBmK5W9abLY 
#Homework 3 Part 1 

#create a fucntion to get a list of prime numbers
def createprimelist(max):
    'Creates a list of prime number up to the given range.'
    notprime = []
    prime = [2,3,5,7]

    for n in range(8,max+1):
        if any(n % x == 0 for x in prime):
            notprime.append(n)
        else:
            prime.append(n)

    prime = [1] + prime 

    return prime

createprimelist(10)    


def goldbachs(num):
    'fucntion that creates a list of prime numbers from 1 to num using   \
    createprimelist function and prints an equation of two prime numbers \
    that make up each even number in the range 0 to num'

    #create a list of prime numbers using the createprimelist function
    listofprimes = createprimelist(num)

    for n in range(2,num+1):
        #create a solution count that will later only allow one solution 
        #per n to be printed
        sol=0
        
        if n % 2 == 0: 

            for prime1 in listofprimes:
                for prime2 in range(1,prime1 +1): 
                    if prime1 + prime2 == n:
                        sol+=1
                        if sol == 1:
                            print(n,' = ', prime1,' + ',prime2,end='\n')
 
goldbachs(100)

