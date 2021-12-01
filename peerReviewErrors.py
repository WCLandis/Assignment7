# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: William Landis
# Creation Date: 12/01/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#This message originally displayed tabbed over, and visually unappealing and looked shifted. I removed the unneeded quotations and spaces to correct this mistake.
	print('You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.')
	print()
#When attempting to run this program for the first time, I found this error: inconsistent use of tabs and spaces in indentation. It appears that instead of using the tab, spacebar was used, which caused inconsistent formatting. I fixed the error by backspacing and adding the tab.
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
#Line 24 returned the following error: NameError: name 'caves' is not defined. I fixed this by changing the name to 'cave' to return the correct variable.
	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#In line 31, the comment states that sleep should last for a total of two seconds, it was originally set to three seconds. I corrected this error by changing it to two.
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
#Line 42 revealed the following error: SyntaxError: Missing parentheses in call to 'print.' I added parenthesis around 'Gobbles you down in one bite' to resolve this error.
	else:
		print('Gobbles you down in one bite!')

playAgain = 'yes'
#Line 45 had the following error: SyntaxError: invalid syntax. I fixed this error by adding an additional '=' before 'yes' and before 'y'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
#Line 49 had the following error: NameError: name 'choosecave' is not defined. The choosecave function was not written in camel case as it is defined. I rewrote it as 'chooseCave' to correct this error.
	caveNumber = chooseCave()
	checkCave(caveNumber)
	print('Do you want to play again? (yes or no)') 
	playAgain = input()
#In line 55, the user is not given the 'n' option to receive the 'Thanks for playing' message. I added that for consistency.
	if playAgain == "no" or playAgain == 'n':
#In line 57, 'playing' was misspelled 'planing.' I corrected this misspell.
		print("Thanks for playing")

