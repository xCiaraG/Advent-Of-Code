from collections import defaultdict
houses = defaultdict(int)
directions = input().strip()
santax, santay = 0, 0
robox, roboy = 0, 0
houses[(0, 0)] = 1
nsew = {"<" : (-1, 0), ">" : (1, 0), "^" : (0, 1), "v" : (0, -1)}
for i in range(len(directions)):
	tmpx, tmpy = nsew[directions[i]]
	if i % 2 == 0:
		santax += tmpx
		santay += tmpy 
		houses[(santax, santay)] += 1
	else:
		robox += tmpx
		roboy += tmpy 
		houses[(robox, roboy)] += 1
print(len(houses))