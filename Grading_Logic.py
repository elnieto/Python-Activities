
#Elizabeth Nieto
#09/20/19
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/ZZaoYRsR-zo
#HW1 1 Part 1

def grader():
    'Function used to calculate grades'
    import datetime

    #initiate student's score
    score = 0 

    #Ask grader if student has met first set of requirements
    prelimReqs = input("Has the HW been submitted in a single .py uncompressed file,\n\
include student's name, date, honor statement, and video link? Enter Yes only if\n\
ALL requirements have been met, otherwise enter No." ) 
    
    #Identify first set of requirements have been met
    #If requirements have been met, ask the user to enter individual scores for the 
    #second set of requiremnts.
    if prelimReqs == 'Yes':
        correctness, elegance, hygiene, video = input('How would you rate the\n\
student\'s code based on four requirements, correctness, elegance, hygiene,\n\
and quality of video discussion? Award up to 10pts per category and seperate\n\
your values by a space.').split()
        correctness = int(float(correctness))
        elegance = int(float(elegance))
        hygiene = int(float(hygiene))
        video = int(float(video))
        #calculate score
        Req2 = correctness + elegance + hygiene + video
        score += Req2

        #Ask the grader how many hours late the assignment was.
        hrslate = int(float(input('Enter how many hours late the assignment was.\n\
If the assignment was not late enter 0')))
        if hrslate > 0:
            #calculate deduction for hw being late
            percent = (score/40)*100
            rate = percent * .01
            deduction = hrslate * rate
            newpercent = percent - deduction
            score = 40 * (newpercent/100)

        #If the grade enters 0, score remains unchanged
        else:
            score = score
    #If the first set of requirements has not bee met, set score to  0 
    else:
        score = 0
    
    return score

grader()

prelimReqs = 'Yes'
prelimReqs == 'Yes' 