import utils

DAY = 7
start = utils.get_data(DAY)[0].split(',')
horizontal_positons = utils.list_elem_to_int(start)

fuel_cost = []
list_positions = list(range(1, int(max(horizontal_positons)/2)))

for position in list_positions:
	abs_cost = 0
	for crab_pos in horizontal_positons:

		distance = abs(position - crab_pos)

		abs_cost += sum(list(range(distance+1)))

	fuel_cost.append(abs_cost)

print(min(fuel_cost))


94460895
