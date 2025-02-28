'''
Program: Trivia Game
Author: Mrs K
Date: 2022-02-16
'''

#open the document for reading
f = open("hiscore.txt", 'r')

#read info from the file
hiscore = f.read()

#close the file
f.close()

score = 0

#Asks a question and checks the answer.
#Returns 1 (for one point) if it's right and 0 if it's wrong
def askQuestion(question, answer):
    guess = input(question)
    if guess.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#Define Questions and Answers
qList = ["What city is the Eiffel Tower located in? ",
         "What is the largest country in the world, by area? ",
         "What city is hosting the 2022 Winter Olympics? ",
         "Where would you find the monolithic stone heads known as Mo'ai? ",
         "Uluru is a large rock formation sacred to the Pitjantjatjara people in the centre of what country? "]

aList = ["Paris",
         "Russia",
         "Beijing",
         "Easter Island",
         "Australia"]

#ask each question

for i in range(len(qList)):
    qstn = qList[i]
    ans = aList[i]
    #track score
    score = score + askQuestion(qstn, ans)

print(f'Your score is {score}')

if score > int(hiscore):
    print("Congratulations, new high score!")

    #open for writing
    f = open("hiscore.txt", "w")

    #write the data we want
    f.write(str(score))

    #close the file
    f.close()

    leader = input("What is your name?")
    
    f = open("leader.txt", 'w')
    f.write(leader)
    f.close()
    
