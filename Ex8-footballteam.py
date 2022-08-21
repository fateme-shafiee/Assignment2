from typing import Counter


final_score = 0
equal = 0
winner = 0 
loser = 0
Counter = 1
while (Counter < 9):
    print ('enter your point in game : \n winner : 3  equal : 1  loser : 0 \n score ', Counter ,' : ')
    score = int(input())
    if ((score == 0) or (score == 3)):
        final_score += score
        Counter += 1
        if (score == 3):
            winner += 1
        elif (score == 1):
            equal += 1
        elif (score == 0):
            loser += 1
    else:
        print('your entered an error !')
print ('final_score   winner  equal  loser ',' ',final_score,'     ',winner,'     ',equal,'    ',loser)
