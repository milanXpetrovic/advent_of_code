part1 = {
		"A X" : 4,
		"A Y" : 8,
		"A Z" : 3,
		"B X" : 1,
		"B Y" : 5,
		"B Z" : 9,
		"C X" : 7,
		"C Y" : 2,
		"C Z" : 6
}

part2 = {
		"A X" : 3,
		"A Y" : 4,
		"A Z" : 8,
		"B X" : 1,
		"B Y" : 5,
		"B Z" : 9,
		"C X" : 2,
		"C Y" : 6,
		"C Z" : 7
}

with open('test_input.txt', 'r') as aoc_input:
	aoc_input = aoc_input.read().split("\n")

print(sum([part1[l] for l in aoc_input]))
print(sum([part2[l] for l in aoc_input]))

