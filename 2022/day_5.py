with open('test_input.txt', 'r') as f:
    a = f.read().split("\n")

stack = {
    '1' :['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'],
    '2' :['Z', 'C', 'D'],
    '3' :['H', 'J', 'F', 'C', 'N', 'G', 'W'],
    '4' :['P', 'J', 'D', 'M', 'T', 'S', 'B'],
    '5' :['N', 'C', 'D', 'R', 'J'],
    '6' :['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z'],
    '7' :['P', 'Z', 'T', 'F', 'R', 'H'],
    '8' :['L', 'V', 'M', 'G'],
    '9' :['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J']
}

for c in a:
    c = c.split(" from ")
    
    how_much = c[0].split(" ")[-1]

    source, target = c[1].split(" to ")

    take = stack[source][len(stack[source])-int(how_much):]
    stack[source] = stack[source][:len(stack[source])-int(how_much)]
    
    for l in take:
        stack[target].append(l)


for l in stack.values():
    print(l[-1], end="")

