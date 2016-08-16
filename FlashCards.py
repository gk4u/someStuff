import random

#opens the file used for the flash cards.

f = open('Spanish.txt','r')

#reads first line to find out what the category is and prints it to the screen
category = f.readline()
print("The category is "+category)

#a dictionary used to store the clue and answer
cards ={}
keys = []
#loop through the file to grab the clue and answer and adds it to the dictionary.
for line in f:
	commaLoc = line.index(',')
	clue = line[:commaLoc]
	answer = line[commaLoc+1:-1]
	cards[clue]=answer
	keys.append(clue)

random.shuffle(keys)

for card in keys:
	print("\n"+card+"?")
	answer = input()
	if(answer == 'exit'):
		exit()
	if answer == cards[card]:
		print("Correct! Nice Job!")
	else:
		print("Incorrect.  The correct answer is "+cards[card]+"")