import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))
G = 5
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
	G,
	" chances to guess the integer!\n")
print("The random number is ",x)

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < G :
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= G :
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
