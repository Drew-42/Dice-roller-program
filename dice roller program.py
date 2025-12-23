import random

# The script's data:

dice_art = {
	1: ('┌─────────┐', 
		'│         │', 
		'│    ●    │', 
		'│         │', 
		'└─────────┘'),
	2: ('┌─────────┐', 
		'│         │', 
		'│  ●   ●  │', 
		'│         │', 
		'└─────────┘'),
	3: ('┌─────────┐', 
		'│         │', 
		'│  ● ● ●  │', 
		'│         │', 
		'└─────────┘'),
	4: ('┌─────────┐', 
		'│  ●   ●  │', 
		'│         │', 
		'│  ●   ●  │', 
		'└─────────┘'),
	5: ('┌─────────┐', 
		'│  ●   ●  │', 
		'│    ●    │', 
		'│  ●   ●  │', 
		'└─────────┘'),
	6: ('┌─────────┐', 
		'│  ● ● ●  │', 
		'│  ● ● ●  │', 
		'│  ● ● ●  │', 
		'└─────────┘')
}

dice = []
total = 0

# The user selects the number of dice:

while True:
	try:
		nr_dice = int(input('Select number of dice: '))

	except Exception:
		print('Invalid input. Must be a whole number!')

	else:
		if nr_dice > 0:
			break

		else:
			print('Invalid input. Must be a positive number!')

# Random selection of outcome for each dice:

for die in range(nr_dice):
	dice.append(random.randint(1, 6))

# Each dice with their chosen outcome is printed from left to right:

for line in range(5):
	for die in dice:
		print(dice_art.get(die)[line], end='')
	print()

# The total is printed:

for die in dice:
	total += die

print(f'Total: {total}')