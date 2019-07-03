from random import*
from string import*
while True:
	noun=['steph','steve','kamau','leah','socrates','waire','nevoh','adhiambo']
	adjective=['loving','cheeky','honesty','talkative','hardworking','creative']
	print('Welcome to the password picker!\n\n')
	number=randrange(0,100)
	#randrange() chooses a number from 0 to 99
	#choice() is a function that selects one item from the given one
	noun=choice(noun)
	adjective=choice(adjective)
	specialchar=choice(punctuation)
	password=adjective + noun +str(number) +specialchar
	print("Your new password is :", password)
	print('\n')
print()
#response=input('would you like another password....\nType yes if you need another')
#if response != 'yes' or 'YES' or 'Yes' or 'YEs' or 'yES':
	#break
#breakstatement has refused to work	

