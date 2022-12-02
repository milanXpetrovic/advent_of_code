def find_unique(key):
	one = ""
	four = ""
	seven = ""
	for e in key:
		if len(e) == 2:
			one = e
		elif len(e) == 4:
			four = e

		elif len(e) == 3:
			seven = e

		elif len(e) == 7:
			eight = e

		else:
			pass

	return one, four, seven, eight


import utils

DAY = 8
input_str = utils.get_data(DAY)

print(input_str)

numbers = []
for s in input_str:

	s = s.split('|')
	key = s[0].split(' ')

	#   	   0   1   2   3   4   5   6   7   8   9
	n_keys = ["", "", "", "", "", "", "", "", "", ""]
	n_keys[1], n_keys[4], n_keys[7], n_keys[8] = find_unique(key)


	for e in key:
		if len(e) == 5:
			if len(set(e).intersection(n_keys[1])) == 2:
				n_keys[3] = e

			elif len(set(e).intersection(n_keys[4])) == 3:
				n_keys[5] = e
				
			elif len(set(e).intersection(n_keys[4])) == 2:
				n_keys[2] = e

		elif len(e) == 6:
			if len(set(e).intersection(n_keys[1])) == 1 or len(set(e).intersection(n_keys[7])) == 1:
				n_keys[6] = e

			elif len(set(e).intersection(n_keys[4])) == 4:
				n_keys[9] = e

			else:
				n_keys[0] = e



	dechiper = s[1].split(' ')
	number = ""
	for unknown in dechiper: 
		for i, keys in enumerate(n_keys):
			if sorted(keys) == sorted(unknown):
				number += str(i)

	numbers.append(int(number))

print(numbers)
print(sum(numbers))