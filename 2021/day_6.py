import utils
import sys
DAY = 6
start = utils.get_data(DAY)[0].split(',')
start = utils.list_elem_to_int(start)

from collections import deque

s = start
number_of_fish = len(s)

#    0  1  2  3  4  5  6  7  8
c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for elem in start:
	if elem == 0:
		c[0] += 1

	elif elem == 1:
		c[1] += 1

	elif elem == 2:
		c[2] += 1

	elif elem == 3:
		c[3] += 1

	elif elem == 4:
		c[4] += 1

	elif elem == 5:
		c[5] += 1

	elif elem == 6:
		c[6] += 1

	elif elem == 7:
		c[7] += 1

	else:
		c[8] += 1


c = deque(c)

for i in range(256):
	c.rotate(-1)
	c[6] += c[-1]

	number_of_fish += c[-1] 

	print(number_of_fish)