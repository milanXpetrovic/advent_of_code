import utils

DAY = 2
site_content = utils.get_data(DAY)

# part 1

horizontal = 0
depth = 0

for row in site_content:	
	direction, amount = row.split(' ')
	amount = int(amount)

	if direction == 'forward':
		horizontal += amount

	elif direction == 'down':
		depth += amount

	else:
		depth -= amount

print("part 1: {}".format(horizontal*depth))

# part 2


horizontal = 0
depth = 0
aim = 0

for row in site_content:	
	direction, amount = row.split(' ')
	amount = int(amount)

	if direction == 'forward':
		horizontal += amount
		depth = depth + (aim * amount)

		
	elif direction == 'down':
		aim += amount

	else:
		aim -= amount

print("part 2: {}".format(horizontal*depth))