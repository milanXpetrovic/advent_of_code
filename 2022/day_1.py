#part 1
with open('test_input.txt', 'r') as aoc_input:
	print(max([sum([int(x) for x in total]) for total in [x.split("\n") for x in aoc_input.read().split("\n\n")]]))

# part 2
with open('test_input.txt', 'r') as aoc_input:
	cals = [sum([int(x) for x in total]) for total in [x.split("\n") for x in aoc_input.read().split("\n\n")]]
	cals.sort(reverse=True)
	print(sum(cals[:3]))