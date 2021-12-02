# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: William Landis
# Creation Date: 12/01/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#Line 13 originally displayed tabbed over, and visually unappealing and looked shifted. 
	print('You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.')
#I removed the unneeded quotations and spaces to correct this mistake. This correction reformats the text so that it is clean and neat.
	print()
def chooseCave():
#When attempting to run this program for the first time, I found this error: inconsistent use of tabs and spaces in indentation. 
	cave = ''
#It appears that instead of using the tab, spacebar was used, which caused inconsistent formatting. I fixed the error by backspacing and adding the tab.
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
#Line 24 returned the following error: NameError: name 'caves' is not defined. 
	return cave
#I fixed this by changing the name to 'cave' because 'caves' was returning the incorrect variable.
def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#In line 31, the comment states that sleep should last for a total of two seconds, it was originally set to three seconds. 
	time.sleep(2)
#I corrected this error by changing the time interval to 2 seconds to match the intended sleep time.
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
#Line 42 revealed the following error: SyntaxError: Missing parentheses in call to 'print.' 
	else:
		print('Gobbles you down in one bite!')
#I added parenthesis around 'Gobbles you down in one bite' to resolve this error, because the print function requires partenthesis in its parameters.
playAgain = 'yes'
#Line 45 had the following error: SyntaxError: invalid syntax. 
while playAgain == 'yes' or playAgain == 'y':
#I fixed this error by adding an additional '=' before 'yes' and before 'y.' This was necessary because the equality operator requires two equal signs.
	displayIntro()
#Line 49 had the following error: NameError: name 'choosecave' is not defined. 
	caveNumber = chooseCave()
#The choosecave function was not written in camel case as it is defined. I rewrote it as 'chooseCave' to correct this error.
	checkCave(caveNumber)
	print('Do you want to play again? (yes or no)') 
	playAgain = input()
#In line 55, the user is not given the 'n' option to receive the 'Thanks for playing' message. 
	if playAgain == "no" or playAgain == 'n':
#I added "or playAgain == 'n'" to maintain coding consistency since 'y' will restart the game.
#line 57 orginally said 'Thanks for planing.' 
		print("Thanks for playing")
#Playing was misspelled, so I corrected this error.


