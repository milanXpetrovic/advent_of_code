import utils

DAY = 9
input_str = utils.get_data(DAY)

matrix = []
for row in input_str:
	matrix.append([int(x) for x in row])


minimums = []
locations = []
for i in range(0, len(matrix)):
	for j in range(0, len(matrix[0])):

		num = matrix[i][j]
		n1 = 99
		n2 = 99
		n3 = 99
		n4 = 99
		if i+1 >= 0 and i+1 < len(matrix):
			n1 = matrix[i+1][j]

		if i-1 >= 0:
			n2 = matrix[i-1][j]

		if j+1 >= 0 and j+1 < len(matrix[0]):
			n3 = matrix[i][j+1]

		if j-1 >= 0 and j-1 < len(matrix[0]):
			n4 = matrix[i][j-1]

		if num < n1 and num < n2 and num < n3 and num < n4:
			minimums.append(matrix[i][j]+1)
			locations.append((i,j))


print("Part 1 solution: {}".format(sum(minimums)))

## part2


def send_matrix(input_str):
	for row in input_str:
		matrix.append([int(x) for x in row])

	matrix_ = []
	for row in matrix:

		matrix_.append([9] + row + [9])

	nines = [9] * len(matrix_[0])

	matrix_ = [nines] + matrix_ + [nines]


	return matrix_


def flood_fill(x, y):
	global matrix

	if matrix[x][y] < 9:

		matrix[x][y] = 69

		if x > 0:
			flood_fill(x-1,y)

		if x < len(matrix[y]) - 1:
			flood_fill(x+1,y)

		if y > 0:
			flood_fill(x,y-1)

		if y < len(matrix) - 1:
			flood_fill(x,y+1)


# visited_nodes = []
basin_sizes = []
for coord in locations:
	x, y = coord

	matrix = send_matrix(input_str)
	
	flood_fill(x, y)

	counter = 0
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])): 
			if matrix[x][y] == 69:
				counter += 1


	basin_sizes.append(counter)


basin_sizes.sort(reverse=True)
print("Part 2 solution: {}".format(basin_sizes[0] * basin_sizes[1] * basin_sizes[2]))


print(basin_sizes)
