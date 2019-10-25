#Elizabeth Nieto
#09/20/19
#Honor Statement: I have not given or received any unauthorized assistance \
#on this assignment.
#https://youtu.be/6rhgXRIZ6OA
#HW 1 Part 2

def coprime(a,b):
    'takes two numbers and returns whether or not they are are coprime'
    #check if the numbers are divisible by 2 or if both are 2
    if (a % 2 != 0 and b % 2 != 0) or (a ==2 and b ==2):
        classification = 'Coprime'
    else:
        classification = 'Not Coprime'
    return classification

def coprime_test_loop():
    'Asks users for two numbers then passes these numbers to function \
    coprime which identifies the nuber as coprime or not and returns \
    the classification for the user. After it asks the user if they would\
    like to repeat the function.'
 
    #ask for user to enter two nums
    a2, b2 = input( 'Enter two numbers seperated by a space(e.g. 34 24) \
    or enter "Stop Process" to end this process.').split()
    #base case to end recursion
    if a2 == 'Stop':
        return 'Process Stopped'
    else:
        a2 = int(float(a2))
        b2 = int(float(b2))
        #calls function coprime, format output, loop function
        result = coprime(a2,b2) 
        print(a2, ' and ', b2, ' are ', result)
        return coprime_test_loop()

#test code
print(coprime_test_loop())


 
