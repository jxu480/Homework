# dnd1-elementaladept.py

# You are a mage with the Fire Bolt spell. This does 1d10 damage, or 5.5
# points of damage on average. If you have the Elemental Adept feat, damage
# rolls of 1 become 2. How much more damage do you do on average if you are
# an Elemental Adept? Simulate by rolling dice a million times.

import random

EA = 0
AV = 0
trials = 1000000

for i in range(trials):
	AV += random.randint(1, 10)

for i in range(trials):
	roll = random.randint(1, 10)
	if roll == 1:
		roll = 2
	EA += roll
	
a = AV / trials
b = EA / trials
print(b - a)

"""
python3 dnd1-elementaladept.py
0.1
"""
