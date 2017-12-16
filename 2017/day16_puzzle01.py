moves = input().split(",")
current = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
for m in moves:
	if m[0] == "s":
		tmp = int(m[1:])
		current = current[-tmp:] + current[:-tmp]
	elif m[0] == "x":
		tmp1, tmp2 = [int(x) for x in m[1:].split("/")]
		current[tmp1], current[tmp2] = current[tmp2], current[tmp1]
	elif m[0] == "p": 
		tmp1, tmp2 = m[1:].split("/")
		tmp1 = current.index(tmp1)
		tmp2 = current.index(tmp2)
		current[tmp1], current[tmp2] = current[tmp2], current[tmp1]
print("".join(current))