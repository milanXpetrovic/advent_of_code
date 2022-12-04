

with open("input.txt", "r") as file:
    aoc = file.read().split("\n")


count = 0
for l in aoc: 
    l = l.split(",")
    f, s = l
    start1, end1 = f.split("-")
    start2, end2 = s.split("-")
    start1, end1 = int(start1), int(end1)
    start2, end2 = int(start2), int(end2)
    
    if start1 <= start2 and end1 >= start2:
        count += 1
    
    elif start2 <= start1 and end2 >= start1:
        count += 1
    
    else:
        pass
        
print(count)