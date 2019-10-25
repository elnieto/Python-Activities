#Elizabeth Nieto
#10/01/19
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/6P4RmM_qedQ
#Homework 2 Part 2 

import os
import math
os.chdir('C:\\Users\\eniet\\Documents\\School\\Autumn19\\DSC_430_Python_Programing\\Week_2_The_Art_of_Programing\\HW\\Week2')
os.getcwd()

def greetUser():
    'Returns allo mate to greet user'
    print('Allo Mate')

def getUserInput():
    'Asks user to enter a number 1 - 3. Returns that value'
    n = input('Enter a number 1 - 3')
    return n

def readfile(num):
    'Reads a file based on input and returns a formatted and sorted \
     string of numbers in the file'
    
    #figure out which file to read in
    fileName = ' '
    num = int(float(num))
    if num == 1:
        fileName ='StemAndLeaf1.txt'
    elif num == 2:
        fileName ='StemAndLeaf2.txt'
    elif num == 3:
        fileName ='StemAndLeaf3.txt'
    else:
        print('Invalid entry. Enter a number 1-3')
    
    #read in the file
    infile = open(fileName, "r") 
    lineList = infile.readlines()
    infile.close()
    listofNum = []
    
    #format file
    for i in range ( 0, len(lineList)):
        x = int(lineList[i].strip('\n'))
        listofNum.append(x)
        listofNum.sort()
    return listofNum

def bp(maxNum):
    ' Returns a breaking point based on the given number'
    breakingpt = 0
    numstr =str(maxNum)
    maxLen = len(numstr)
    if maxLen % 2 == 0:
        breakingpt = maxLen / 2 
    else:
        breakingpt = math.ceil(maxLen / 2)
    return breakingpt 

def createStemAndLeaf(NumList):
    'Takes a list of numbers and creates a stem and leaf plot'
    #createStemAndLeaf(sorted)
    maxNum = max(NumList)
    print(maxNum)
    minNum = min(NumList)
    print(minNum)
    breakingpoint = int(bp(maxNum))
    print('breakingpoint {}'.format(breakingpoint))
    #create list of stems and stem and leaves
    stemList = []
    stemleafList =[]
    for num in NumList:
        num = str(num)
        stem = num[0:breakingpoint]
        leaf = num[breakingpoint:]
        if stem not in stemList:
                stemList.append(stem)
                #create a new sublist with new stem and leaf
                stemleafList.append([stem,leaf])
        else:
           #find maching [0] to current stem
           for x in stemleafList:
               if stem == x[0]:
                   x.append(leaf)
               else:
                   None
    #format list
    for x in stemleafList:
        print (x[0], '|', x[1:], '\n' )

def exit():
    'runs the main function again or exits depending in user input'
    response = input('Would you like ot continue? Enter Y/N ')
    if response == 'Y':
        return True
    else:
        print('Program ended.')

def main():
    'Runs a series of functions in a while loop that will \
    greet the user, get user input, create a stem and leaf \
    plot from the input, and ask the user if they would   \
    like to repeat the function'
    q = True
    while q == True:
        greetUser()
        n = getUserInput()
        listofNum = readfile(n)
        createStemAndLeaf(listofNum)
        q = exit()

#test code
main()









