import utils

DAY = 1
site_content = utils.get_data(DAY)
site_content = conver_list_elems_to_int(site_content)


# part1

depth_increase = 1

for i in range(1, len(site_content)):
	if site_content[i-1] < site_content[i]:
		depth_increase +=1

print("part 1: {}".format(depth_increase))


# part2 

index = 0
new_depths = []

while(index <= len(site_content)-3):

	window = sum(site_content[index:index+3])
	index += 1
	new_depths.append(window)


depth_increase = 0

for i in range(1, len(new_depths)):
	if new_depths[i-1] < new_depths[i]:
		depth_increase +=1

print("part 2: {}".format(depth_increase))
