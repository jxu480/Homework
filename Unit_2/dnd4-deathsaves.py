# dnd4-deathsaves.py

# Death saves are a little different than normal saving throws. If your
# health drops to 0 or below, you are unconscious and may die. Each time it
# is your turn, roll a d20 to determine if you get closer to life or fall
# deeper into death. If the number is less than 10, you record a "failure".
# If the number is 10 or greater, you record a "success". If you collect 3
# failures, you "die". If you collect 3 successes, you are "stable" but
# unconscious. If you are unlucky and roll a 1, it counts as 2 failures.
# If you're lucky and roll a 20, you gain 1 health and have "revived".
# Write a program that simulates death saves. What is the probability one
# dies, stabilizes, or revives?

import random

threshold = 10
trials = 100

rev = 0
stab = 0
die = 0


for i in range(trials):
#Does this character die? Survive? Revive?
	s = 0
	f = 0
	state = None
	while True:
		roll = random.randint(1, 20) 
		if roll == 20:
			state = 'revive'
			break
			
		if roll == 1:
			f += 2	
		elif roll < 10:
			f += 1
		elif roll >= 10:
			s += 1
			
		if s == 3:
			state = 'stability'
			break
		if f >= 3:
			state = 'death'
			break

	if state == 'revive': rev += 1
	elif state == 'stability': stab += 1
	else: die += 1
		
	
print(f'die: {die/trials:.3f}', f'stabilize: {stab/trials:.3f}', f'revive: {rev/trials:.3f}' )


"""
python3 dnd4-deathsaves.py
die: 0.405
stabilize: 0.414
revive: 0.181
"""
