import questionsDatabase #Imports database file: WWTBAM_dataBase.py
import random #Import random function
import time

print (" ┎―――――――――――――――――――――――――――――――――――――――――――――――┒")
print (" |           _______Wants to Be_______           |")
print (" |          //  Who              a   \\\          |")
print (" |          ||      MILLIONAIRE       ||         |")
print (" |          \\\  Who              a   //          |")
print (" |           ͞ ͞ ͞ ͞ ͞ ͞  Wants to Be ͞ ͞ ͞ ͞ ͞ ͞ ͞           |")          
print (" ┕―――――――――――――――――――――――――――――――――――――――――――――――┙\n")

print ("Welcome to 'Who Wants to Be a Millionaire!'")
print("\n '- And with us tonight we have...?'")
playerName = str( input("\n My name is:" + " "))
ValidPlayerName = 0

#Prevent input of invalid names so there won't be conflicts
while ValidPlayerName == 0: #Until valid (1)
    if (playerName == "Score" or playerName == "score" or playerName == "Proceed" or playerName == "proceed" or playerName == "Stage" or playerName == "stage" or playerName == "History" or playerName == "history" or playerName == "1" or playerName == "2" or playerName == "3"):
        playerName = str( input("\n My name is:" + " "))
        print ("\n\t" + "Invalid Name Found: Please enter another name")
        ValidPlayerName = 0 
    else:  
        ValidPlayerName = 1 #sets boolean to 1 (True)
        
print ("\n\t" + 3* " " + "— 'Hello and welcome to the greatest trivia show on national television.\
           \n\t" + 3* " " + "— 'Let's start the game, " + playerName + "!'\n\
           — 'There are dozens of possible questions for you to play.'\n\
           — 'Can you get to the grand prize of 1 Million Euros!?'\n\
           \n\t   — 'Here we go, and good Luck, "+ playerName + "!!'")
           
"""variables setup"""
pause = int() #just to give a little breathing room
sessionQuestions = 3 #counter for how many questions have been asked while program has been running

"""setup game history of correct answers"""
answerHistory = ['Paris', 'Tennis', 'Wear it'] #will store all the correct guesses per round.
questionHistory = ['What is the capital of France?', 'What sport did André Agassi played?', "What is the name of Odin's Hammer?"] #will store all the correct guesses per round.
stageHistory = ["100€", "200€", "300€"] #will store all stages per round.

"""question code"""
while len(questionHistory) <= 14: #loops question after question until 15th
    if len(questionHistory) >= 0 and ValidPlayerName == 1:
        """Question Intro"""
        introNumber = int(random.randint(0, 9))
        getIntro = questionsDatabase.getintro(introNumber)
        intro = ''.join([getIntro[0]])
        """Prize Stage"""
        stageNumber = len(questionHistory)
        getstage = questionsDatabase.getstage(stageNumber)
        stage = ''.join([getstage[0]])
	#Generates a random number and gets that question from the database questionsDatabase.py
        questionNumber = int(random.randint(0, 149)) #randomizer
	#Gets question from database based on the generated random number
        getQuestion = questionsDatabase.getquestion(questionNumber)
        """picks questions to be printed"""
        question = ''.join([getQuestion[0]])
        """Shuffles possible answers"""
        answerList = getQuestion[1:5]
        random.shuffle(answerList)
    #assigns the random possible answers ABCD to each variable.
        optionA = ''.join([answerList[0]])
        optionB = ''.join([answerList[1]])
        optionC = ''.join([answerList[2]])
        optionD = ''.join([answerList[3]])
        
        print("\n\n Type: "+"\u0332".join(str("'1"))+"' or "+"\u0332".join(str("'Proceed'"))+" to advance to the "+ str(stageNumber+1)+" question worth"+"\u0332".join(str(" "+stage))+".")
        print(" "+"Type: "+"\u0332".join(str("'2"))+"' or "+"\u0332".join(str("'Score'"))+" to check your current score.")
        print(" "+"Type: "+"\u0332".join(str("'3"))+"' or "+"\u0332".join(str("'History'"))+" to see your correctly guessed answers.")
        
        pause = str( input("\n"+" " + playerName + ":" + " "))
        if (pause == "score" or pause == "Score" or pause == "2"):
            if sessionQuestions != 0:
                print("\n\n"+ "While playing, you've scored"+" "+ str(len(answerHistory))+" " + "out of"+" "+ str(sessionQuestions)+" questions asked.")
                print("\t — This is about {}% correctness out of all questions asked since you started.".format(int(len(answerHistory)/sessionQuestions*100)))
                if not (len(questionHistory)):
                    print("\n [ You need to start a new round before checking your current score ]")
                else:
                    print("\n"+ "This round, you've scored"+" "+ str(len(answerHistory))+" " + "out of"+" "+ str(len(questionHistory))+" for a grand total of"+"\u0332".join(str(" "+stage))+".")
                    print("\t — This is about {}% correctness out of all questions asked this round.".format(int(len(answerHistory)/len(questionHistory)*100)))
            else:
                print("\n\n [ Either your score is 0 or you haven't guessed any question. Try Again! ]")
        if (pause == "history" or pause == "History" or pause == "3"):
            if len(answerHistory) != 0:
                print("\n"+"'"+playerName + ", these are the answers you've guessed correctly this round:' \n")
                #merge 3 tuples w/ items paired together - stage + question + correct answer
                for combinedQA in zip(stageHistory, questionHistory, answerHistory): 
                    print (' | '.join(combinedQA))
            else:
                print("\n\n [ Try starting a round before checking your correct answers. ]")
        if (pause == "Proceed" or pause == "proceed" or pause == "1" and len(questionHistory) >= 0):
            print("\t\n\n"+"Stage: ["+ str(stageNumber+1)+" | "+str(stage)+"] "+"'— ",intro, str(len(questionHistory) +1), "for a total prize of","\u0332".join(str(""+stage)),":'")
            print ("\n\n\t"+"— '"+question+"'")
            sessionQuestions += 1
        
        #prints question: ["question", "option A", "option B", "option C", "option D", "correct answer"]
            print("\n\t [ A. " + str(optionA)+" ]" + "\t\t\t\t [ B. " + str(optionB)+" ]")
            print("\n\t [ C. " + str(optionC)+" ]" + "\t\t\t\t [ D. " + str(optionD)+" ]")
            
            correct_answer = getQuestion[5] #defines correct answer to a variable, always item 5 from the list.
            questionHistory.append(str(getQuestion[0]))
            answerHistory.append(str(getQuestion[5]))
            stageHistory.append(str(stage))
        
            answer = input("\n The answer is:" + " ")
        #checks if it's option () and if option () is the correct one (always item [5])
            if (answer == "a" or answer == "A") and (optionA == str(correct_answer)):
                stageNumber += 1
                print("\n\n\t — 'Congratulations "+ playerName + ", that is correct! "+ playerName+". You've won"+"\u0332".join(str(" "+stage))+".'")
                print("\n\t\t The correct answer was: " + str(correct_answer)+".")
            elif (answer == "b" or answer == "B") and (optionB == str(correct_answer)):
                stageNumber += 1
                print("\n\n\t [ — 'Congratulations "+ playerName + ", that is correct! "+ playerName+". You've now won"+"\u0332".join(str(" "+stage))+".'' ]")
                print("\n\t\t The correct answer was: " + str(correct_answer)+".")
            elif (answer == "c" or answer == "C") and (optionC == str(correct_answer)):
                stageNumber += 1
                print("\n\n\t [ — Congratulations "+ playerName + ", that is correct! "+ playerName+". You've now won"+"\u0332".join(str(" "+stage))+". ]")
                print("\n\t\t The correct answer was: " + str(correct_answer)+".")
            elif (answer == "d" or answer == "D") and (optionD == str(correct_answer)):
                stageNumber += 1
                print("\n\n\t [ — 'Congratulations "+ playerName + ", that is correct! "+ playerName+". You've now won"+"\u0332".join(str(" "+stage))+".'' ]")
                print("\n\t\t The correct answer was: " + str(correct_answer)+".")
            else:
                time.sleep(1)
                print("\n\n\t '— Incorrect. The correct answer was: " + str(correct_answer)+".'")
                print("\n\t '— You won a total of:","\u0332".join(str(" "+stage)),".'")
                print("\n Your Prize Stage been reset to question nº1, worth"+"\u0332".join(" 100€")+".")
                answerHistory, questionHistory, stageHistory = ([] for i in range(3)) # Clears all histories
                stageNumber = 0 # Go back to prize stage [0] -> 100€
else:
    print("\n\n\t — 'Congratulations "+ playerName + ", you've won Who Wants to Be a Millionaire!'")