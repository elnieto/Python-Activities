#Elizabeth Nieto
#10/15/19
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/rmRIvLiVgLw
#Homework 4 Part 1 

import random
import math

def getuserinput():
    "Asks user for two numbers, converts inputs to int, and returns both values."
    
    i_input, n_input = input('Enter two numbers').split()
    
    i = int(float(i_input))
    n = int(float(n_input))
    
    return i, n;

#getuserinput()

def  RandNumListGenerator(i):
        "Takes a number(i) and creates and returns a list of i random numbers between 1-100."
        
        numList = []

        for num in range(i):                          #for i times
            numList.append(random.randrange(1,101))   #add a random number between 1 to 100 to numList

        return numList

#RandNumListGenerator(10)

def sorter(numList):
    'Takes as input a list of numbers and sorts and returns them.'

    sortedList = sorted(numList)

    return sortedList

#sorter([1,4,5,8,3])

def checker(sortedList,n):
    'Takes as input a sorted list and returns any two numbers when summed equal n or \
    prints number cannot be found'

    lessthan = []
    
    for num in sortedList:

       if num < n:
            lessthan.append(num)


    for snum in lessthan+[00]:              ##if loop gets to 00 this means none of the numbers - num is not in the list
                                            #if all numbers have been checked and the diff is not int the
        if snum == 00 or lessthan == []:    #list, or if the list is empty 
            print('Given the random number list a sum using two numbers equaling to ', 'n',' cannot be found.')        
        
        diff = n - snum
        

        if diff in lessthan:
            print( snum, '+', diff, '=', n)

            break

#checker([1,3, 4, 5, 8], 9) 
#checker([3, 4, 5, 8], 9)
#checker([89,99,56,37],9)
#checker([1,7,6,4],9)

def exit():
    'Ask the user if they would like to run the program again.'

    again = input('Do you want to continue? enter Y/N')

    if again == 'Y':
        return True
    else:
        print('Process ended')

def goldbachDeuce():
    'Runs a series of fucntions that will create a random number list based off \
    user input and then identify if the given number can be summed up using     \
    numbers from the list'

    q = True

    while q == True:    
        i, n = getuserinput()                    #getuserinput
        NumList = RandNumListGenerator(i)        #create a random number list
        SortedList = sorter(NumList)             #sort the randoom number list
        Response = checker(SortedList, n)        #Check if the sum of any set of number in the 
        q = exit()                               #sorted list is equal to n



goldbachDeuce()



def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

cascade(100)

def treecade(n):
    if n < 10:
        print(n)
    else:
        treecade(n // 10)
        print(n)
        treecade(n // 10)

treecade(100)

####hw option

	
def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3

mult3(4) 

	
#Which of these functions correctly implements a recursive 
#algorithm that returns the sum of the first n integers.	
	
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

sum_n(10)

	
def countDigits(n):
    if abs(n) < 9:
        return 1
    else:
        return 1 + countDigits(n//2)

def countDigits(n):
    if n < 9:
        return 1
    else:
        return 1 + countDigits(n//10)

def countDigits(n):
    if abs(n) < 9:
        return 0
    else:
        return 1 + countDigits(n//10)

	
def countDigits(n):
    if abs(n) < 10:
        return 1
    else:
        return 1 + countDigits(n//10)

countDigits(100)

def sumList(list):

    if(len(list) == 0):
        return 0

    return list[0] + sumList(list[1:])

sumList([1,2,3,4,5,6,7,8,9,10])