# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
	print('Take a guess.')
	guess = int(input())
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high!.')
	else:
		break
		if guess==secretNumber:
			print("Well done! You are a Hero!...You guessed ' +str(guessesTaken +' guesses!")
		#condition for the correct guesses
		else:
			print("Kama haujui rudi nyumbani kwa mama yako!..olumulwasii!!")

		
	
		