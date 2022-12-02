import utils

DAY = 4
site_content = utils.get_data(DAY)


bingo_numbers = site_content[0].split(',')
bingo_numbers =  utils.list_elem_to_int(bingo_numbers)

bingo_boards = site_content[1:]

window = 5

bingo = False
while(not(bingo)):
	drawn_numbers = bingo_numbers[:window]

	for index, row in enumerate(bingo_boards):
		row = utils.list_elem_to_int(row.split())

		if(len(list(set(row) & set(drawn_numbers))) > 4):
			print(index)
			print(row)
			print(drawn_numbers[-1])
			bingo = True

	window += 1


winning_board = [89, 86, 51, 84, 27, 47, 61, 35, 26, 18, 22, 79, 28, 78, 21, 15, 77, 65, 46, 64, 1, 99, 16, 80, 95]

wining_sum = 0
for wn in winning_board:
	if wn not in drawn_numbers:
		wining_sum += wn

print("not highlighted numbers: {}".format(wining_sum))
print("last deawn number is: {}".format(drawn_numbers[-1]))
print("multipl = {}".format(wining_sum*drawn_numbers[-1]))

print("-"*50)

def create_dict_with_boards(bingo_boards):
	bingo_dict = {}
	key = 0
	while(len(bingo_boards) > 1):
	    
	    r1 = utils.list_elem_to_int(bingo_boards[1].split())
	    r2 = utils.list_elem_to_int(bingo_boards[2].split())
	    r3 = utils.list_elem_to_int(bingo_boards[3].split())
	    r4 = utils.list_elem_to_int(bingo_boards[4].split())
	    r5 = utils.list_elem_to_int(bingo_boards[5].split())


	    bingo_dict.update({str(key): [r1, r2, r3, r4, r5]})
	    key +=1
	    bingo_boards = bingo_boards[6:]

	return bingo_dict


def check_win(board, drawn_numbers):
	
	r1 = utils.list_elem_to_int(board[0])
	r2 = utils.list_elem_to_int(board[1])
	r3 = utils.list_elem_to_int(board[2])
	r4 = utils.list_elem_to_int(board[3])
	r5 = utils.list_elem_to_int(board[4])


	if(len(list(set(r1) & set(drawn_numbers))) > 4):
		return True

	elif(len(list(set(r2) & set(drawn_numbers))) > 4):
		return True

	elif(len(list(set(r3) & set(drawn_numbers))) > 4):
		return True

	elif(len(list(set(r4) & set(drawn_numbers))) > 4):
		return True

	elif(len(list(set(r5) & set(drawn_numbers))) > 4):
		return True

	
	for i in range(0, 5):
		column = [r1[i], r2[i], r3[i], r4[i], r5[i]]
		column = utils.list_elem_to_int(column)
		
		if (len(list(set(column) & set(drawn_numbers))) > 3):
			return True
	
	return False


def check_wining_boards(bingo_boards, drawn_numbers):

	keys = []
	
	for key, board in bingo_boards.items():

		if (check_win(board, drawn_numbers)):
			keys.append(key)

		else:
			pass

	return keys


def remove_winners(bingo_boards, keys):
	for key in keys:
		bingo_boards.pop(key, None)



bingo_numbers = site_content[0].split(',')
bingo_numbers =  utils.list_elem_to_int(bingo_numbers)
bingo_boards = create_dict_with_boards(site_content[1:])

window = 5 

while(len(bingo_boards) > 1):

	drawn_numbers = bingo_numbers[:window]

	keys = check_wining_boards(bingo_boards, drawn_numbers)

	remove_winners(bingo_boards,keys)
	window +=1



winning_sum = 0


for key, value in bingo_boards.items():
	window = 5

	while(not check_win(value, drawn_numbers)):
		drawn_numbers = bingo_numbers[:window]
		window +=1

	for window in range(1,100):
		winning_sum = 0
		drawn_numbers = bingo_numbers[:window]

		for row in value:
			for number in row:
				if number not in drawn_numbers:
					winning_sum += number

		print(winning_sum*drawn_numbers[-1])