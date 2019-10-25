#Elizabeth Nieto
#10/21/19
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/ni0yGCrpsjo
#Homework 5 Part 1

#Class for six sided die

import random

class sixsideddie(list):
    'a six sided die class'  
    
    def __init__(self):
        'instantiates 6 sided die'

        self.values = {1,2,3,4,5,6}

        self.die = []

        for side in self.values:

            self.die.append(side)

    def roll(self):
        'Randomly return side from dice'

        self.faceval = random.choice(self.die)
        
        return self.faceval

    def facevalue(self):
        'Return the face value of the side the die is on'
        self.face = self.faceval
        return self.face

    def __repr__(self):
        'Returns canonical string representation of the rolled die'

        return 'sixsideddie({})'.format(self.faceval)


dice_6 = sixsideddie()
dice_6.roll()
dice_6.facevalue()
dice_6.__repr__()



class tensideddie(sixsideddie):
    'a ten sided die class'

    def __init__(self):
        'instantiates 10 sided die'

        self.die = sixsideddie()
        
        for num in range(7,11):
            self.die.append(num)

    def __repr__(self):
        'Returns canonical string representation of the rolled die'

        return 'tensideddie({})'.format(self.faceval)


dice_10 = tensideddie()
dice_10.roll()
dice_10.facevalue()
dice_10.__repr__()



class twentysideddie(tensideddie):
    'a ten sided die class'

    def __init__(self):
        'instantiates 10 sided die'

        self.die = tensideddie()
        
        for num in range(11,20):
            self.die.append(num)

    def __repr__(self):
        'Returns canonical string representation of the rolled die'

        return 'twentysideddie({})'.format(self.faceval)


dice_20 = twentysideddie()
dice_20.roll()
dice_20.facevalue()
dice_20.__repr__()



class cup(twentysideddie):
    "Class object that can hold die, roll the die, get the sum and return the average."
    
    def __init__(self,six=0,ten=0,twenty=0):
        'Creates a cup and adds the number of die stated'
       
        self.six = six
        self.ten = ten
        self.twenty = twenty

        self.cup = []
        
        for count in range(self.six):
            self.cup.append(sixsideddie())

        for count in range(self.ten):
            self.cup.append(tensideddie())

        for count in range(self.twenty):
            self.cup.append(twentysideddie())
    
    def roll(self):
        'Rolls all the dice in the cup'

        self.results = []

        for self.die in self.cup:  

             self.num = sixsideddie.roll(self.die)
             self.results.append(self.num)

        return self.results

    def getSum(self):
        'Returns the sum of a passed list.'
        
        self.sum = sum(self.results)

        return self.sum

    def __repr__(self):
        'Returns canonical string representation of an object'

        return 'cup({})'.format(self.sum) 

mycup = cup(1,2,3)
mycup.roll()
mycup.getSum()
mycup.__repr__()
