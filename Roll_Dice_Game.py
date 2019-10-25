#Elizabeth Nieto
#10/21/19
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/VCLUV48pK5Q 
#Homework 5 Part 2 

import random
import sys

#append file directory of where both files are saved BEFORE importing HW_5a
sys.path.append('C:\\Users\\eniet\\Documents\\School\\Autumn19\\DSC_430_Python_Programing\\Week_5_OOP\\HW5')
sys.path

from HW_5a import cup
from HW_5a import sixsideddie
from HW_5a import tensideddie
from HW_5a import twentysideddie


def greetuser():
    'Greets the user, asks for their name and returns their name.'

    name = input('Allo Mate. Wos yohr name?')

    return name


def getbalance():
    'Instantiates and returns a balance of $100 for the user.'

    balance = 100.00

    return balance


def playgame ():
    'Asks the user if they would like to play a game and returns their response'

    response = input('Would you like to play a game mate?')

    if response == 'Yes':

        return True
    
    else:

        print ('Fine. :p')


def ran_num_gen():
    'Generates and returns a random number.'

    goal = random.randrange(1,1000)

    return goal
  

def placebet(balance):
    'Asks the user how much money they would like to bet.'
    
    print ('Balance: $',balance)

    bet = int(float(input('How much money would yeh like to bet?')))

    if bet <= 0:
        print('Troin to be chummy eh?\nGood try')
        bet = abs(bet)
        return bet
    else:
        return bet


def fillcup():
    'Asks the user how many of each die they would like to use and then fill up a cup accordingly'
    
    die_6, die_10, die_20 = (input('How many 6, 10, and 20 sided die would ye liken in the cup mate?')).split()
    
    die_6 = int(float(die_6))

    die_10 = int(float(die_10))

    die_20 = int(float(die_20))

    filled_cup = cup(die_6,die_10,die_20)

    return (filled_cup)


def roll(filled_cup):
    'Takes as input a cup full of die, rolls it and returns the sum of all the die'

    result = filled_cup.roll()

    result_sum = filled_cup.getSum()

    print('Total die sum', result_sum)

    return result_sum


def checker(goal, die_sum):
     'Take as input the sum of the rolled die and compares it to the random number.'
     
     diff = die_sum - goal

     return diff
 
     
def assesor(bet, balance, diff):
    'Takes as input return value from checker() and \
    awards or deducts money from the user based on their bet.'

    if diff == 0:

        balance += (bet*10)
        return balance

    if diff < 0:

        print('Yeh\'ve lost.')
        balance = balance - bet
        return balance

    else:

        if diff <= 3:

            balance += (bet*5)
            return balance

        if diff <= 10:

            balance += (bet*2)
            return balance


def report(name, balance):
    'Report to the user their new balance'

    print(name, 'your new balance is', balance, '\n')
    

def cups_and_dice():
    'Runs a series of functions used to roll dice, awards or deducts user money based \
    on the sum of the die compared to a random number their placed bets.'

    name = greetuser()

    balance = getbalance()

    play = playgame()

    while play == True:

        if balance > 0:

            randnum = ran_num_gen()
            bet = placebet(balance)
            filled_cup = fillcup()
            die_sum = roll(filled_cup)
            check = checker(randnum,die_sum)
            balance = assesor(bet, balance,check)
            report(name, balance)
            play = playgame()

        else:

             print ('That was a trick.\nNo more bets lad. Yer broke')

             break
        
cups_and_dice()