- Eduardo Carvalho
	- nº 55881
		- fc55881@alunos.fc.ul.pt

- Introduction to Programming.
	- Lecturer: Dr. José Campos.

- FCUL - Faculdade de Ciências da Universidade de Lisboa.
	- Master's in Informatics - 2020/21


DELIVERY STRUCTURE
---------------

- fc55881_projectWhoWantsToBeAMillionaire.zip
	- main.py
	- questionsDatabase.py
	- README.md
	

INTRODUCTION
---------------

> This project was made by Eduardo Carvalho for the Introduction to Programming class - lectured by Dr. José Campos.
> The game showcased is based on 'Who Wants to be a Millionaire?', a quiz game with
> 4 possible answers and a prize corresponding to each of the 15 stages of the game.
> The QAs were retrieved from the Who Wants to be a Millionaire? 2nd Edition for Nintendo's GameBoy Advance.
> https://gamefaqs.gamespot.com/gba/919785-who-wants-to-be-a-millionaire-2nd-edition/faqs/40044
	 
	 
REQUIREMENTS
---------------

This module requires the following to run correctly.

```sh 
Spyder 4.1.*
```

There's no guarantees it will work correctly in any other environments.


USAGE
---------------
 
- Enter Name
        - The first thing the user is required to do is to input his/her name.
	    - There's a few names that are invalid. i.e. Score, Proceed, etc.

- Answering Questions
        - Each question has 4 possible answers and each of them corresponds to the following: A, B, C, D. 
        - The user can answer by writing any of the above - non case sensitive.

- Other valid inputs
		Users can input 'score'/'2' or 'history'/'2' to access several other mechanics
    - Show current score
			- Users can request their current score in the pre-question screen.
			- It will display a metric of correct answers and the prize stage they're at. It will also display a % of correct questions.

    - Show answer history
			- Users can request their current correctly guessed answers history in the pre-question screen.
			- It will display a list of said answers per round. If the user loses a round, it will be cleared.


TODO LIST
---------------

1. Creates a data structure to handle the game's status." 
2. Populates the data structure with some data, i.e., simulates that someone had played."
```sh
* DONE	06/10/2020	Add user input for name
* DONE	06/10/2020	Print questions and answers to 5 different strings
* DONE	06/10/2020	Get questions from list & database /// [see credits]
* DONE	07/10/2020	Randomize questions retrieved
* DONE	08/10/2020	Add a small pause between questions so the player can input-check his current score instead of writing it when a questions is asked. And have a little timeout which is nice
* DONE	09/10/2020	Prevent user name to be named score, proceed or ABCD.
* DONE	10/10/2020	Write a random list of the presenters intro to each stage and say how much money's on the line
* DONE	11/10/2020	Add Stages of question intros
* DONE	12/10/2020	Add the 15 stages of the money until 1 million
* DONE	16/10/2020	Try - Except Zero Division Error is no more! | if sessionQuestions != 0: blabla | if questionsAsked != 0: blabla | did the trick
* DONE	16/10/2020	Score is now per Round and a separate one per Game. 
* DONE	16/10/2020	Fixed some consistency bugs, typos etc. 
* DONE	17/10/2020	Add game history of all correct answers per round
* WIP	17/10/2020	Add a stage bar that shows the current stage based on correct answers /// Compare current stage, print several "[Current Stage = 1000€]" or something like that.	
* DONE	30/10/2020	Add question, history and stage history
* DONE	30/10/2020	Game now starts at stage 4 [worth 500€]
* DONE	30/10/2020	Populated game's history with 3 questions 
* DONE	30/10/2020	Added zip() to merge all history lists together
* DONE	31/10/2020	Retrieve the answers randomly to ABCD instead of being static.
	
3.	Better localization & fix typos.
4.	Add a little timeout before some prints and questions.
5.	Add list of acceptable answers, if invalid input, allow repeat instead of incorrect
6.	Fix misc bugs, everything works great until it doesn't, because of some wacky steps.
7.	Add a Save & Load feature
8.	Refactor code. Looping everything within itself is a bad idea /// see Functions		
9.	Add fallback stages (5-10) for guaranteed money if incorrect.
10.	Add 15th - Final question special with sparkles and unicorns if won.
11.	Add lifelines(random input for lifeline help certainty?)				
12.	Check on how to print with colors - It is possible but not without installing plugins
```

Resources Consulted
---------------

* http://zetcode.com/lang/python/lists/
* https://overiq.com/python-101/lists-in-python/
* https://stackoverflow.com/questions/53618114/print-list-without-brackets-or-commas-in-python
* https://www.tutorialspoint.com/generating-random-number-list-in-python
* https://docs.python.org/3/reference/import.html
* https://realpython.com/python-string-split-concatenate-join/#going-from-a-list-to-a-string-in-python-with-join
* https://docs.python.org/3/tutorial/errors.html
* https://pynative.com/python-random-choice/
* https://stackoverflow.com/questions/35401019/how-do-i-print-something-underlined-in-python
* http://ascii-table.com/ansi-escape-sequences.php
* https://stackoverflow.com/questions/6539860/how-do-i-keep-score-in-a-rock-paper-scissors-game
* https://www.tutorialspoint.com/generating-random-number-list-in-python
* https://pynative.com/python-random-choice/
 * https://www.programiz.com/python-programming/methods/list/append
 * https://www.geeksforgeeks.org/different-ways-to-clear-a-list-in-python/
 * https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
 * https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line

	 
	 
Credits and Acknowledgements
---------------

>* In acordance to https://www.di.fc.ul.pt/~jcmcampos/courses/fp2021/index.html#academic-integrity
>
>> While researching previous iterations and/or projects of Who Wants to be a Millionaire, quiz or trivia games, I found several structures that were of great assistance and inspiration.
>>
>> However, they served solely for the purpose of inspiration and checking how previous works had been structured and implemented.
>>
>> While conducting the research I also made sure these consulted project were open source and/or with a licence that was free to use for any purpose and intents. 
>>
>> Some of my game logic and implementations were inspired by these.
> >
> * No code was therefore copied.


MANTAINERS
---------------

>This program was coded and is maintained by:
>
>> Eduardo Carvalho | nº55881 | fc55881@alunos.fc.ul.pt | FCUL
