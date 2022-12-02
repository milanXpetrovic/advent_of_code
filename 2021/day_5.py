import utils

DAY = 5
site_content = utils.get_data(DAY)

plane = []


for i in range(1000):
	row = []
	for j in range(1000):
		row.append(0)
	plane.append(row)

skip_indices = []
for index, input_str in enumerate(site_content):

	firs_pair, second_pair = input_str.split('->')
	x1, y1 = firs_pair.split(',')
	x2, y2 = second_pair.split(',')
	x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

	min_x = min(x1, x2) 
	min_y =	min(y1, y2)
	max_x = max(x1, x2)
	max_y = max(y1, y2)
	


	if (x1 == x2 or y1 == y2):

		skip_indices.append(index)
		for x in range(min_x, max_x+1):
			for y in range(min_y, max_y+1):
				plane[y][x] += 1

	# x1 6 y1 4 x2 2 y2 0	
	elif(x1 > x2 and y1 > y2 and index not in skip_indices):
		skip_indices.append(index)
		x = x2
		y = y2
		while x <= x1 and y <= y1:

			plane[y][x] += 1
			x +=1
			y +=1

	elif(x2 > x1 and y2 > y1 and index not in skip_indices):
		skip_indices.append(index)

		x = x1
		y = y1
		while x <= x2 and y <= y2:
			
			plane[y][x] += 1
			x +=1
			y +=1

	# x1 8  y1 0  x2 0  y2 8
	elif(x1 > x2 and y2 > y1 and index not in skip_indices):
		skip_indices.append(index)

		x = x1
		y = y1
		while x >= x2 and y <= y2:
			
			plane[y][x] += 1
			x -=1
			y +=1

	# x1 5  y1 5 x2 8 y2 2
	elif(x2 > x1 and y1 > y2 and index not in skip_indices):
		skip_indices.append(index)

		x = x2
		y = y2
		while x >= x1 and y <= y1:
			
			plane[y][x] += 1
			x -=1
			y +=1



count_max_val = 0
for row in plane:
 	for val in row:
 		if val > 1:
 			count_max_val +=1


print(count_max_val)

# for row in plane:
# 	print(row)