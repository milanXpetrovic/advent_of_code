import utils

DAY = 3
site_content = utils.get_data(DAY)


print("number of lines: {}".format(len(site_content)))

ones_counter = 0
value = ''
for position in range(0, len(site_content[0])):
	for row in site_content:
		ones_counter += int(row[position])

	if ones_counter > (len(site_content)/2):
		value += '1'

	else:
		value += '0'

	ones_counter = 0


invers_value = ''
for v in value:
	if v == '1':
		invers_value += '0'

	else:
		invers_value += '1'

value = (int(value, 2))
invers_value = (int(invers_value, 2))

print("part 1: {}".format(value*invers_value))


#part 2 

def get_key(position, site_content):
	ones_counter = 0

	for row in site_content:
		ones_counter += int(row[position])

	if ones_counter >= (len(site_content)/2):
		return '0'

	else:
		return '1'



indices = []

for position in range(0, len(site_content[0])):
	key = get_key(position, site_content)

	for index, row in enumerate(site_content):
		if key == row[position]:
			indices.append(int(index))

	site_content = [site_content[index] for index in indices]
	
	indices = []

	print(position)
	print(site_content)




val1 = int('111101010001', 2)
val2 = int('001101000100', 2)

print("part 2: {}".format(val1 * val2))

