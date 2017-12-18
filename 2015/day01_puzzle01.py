brackets = input().strip()
total = 0
for b in brackets:
	if b == "(":
		total += 1
	else:
		total -= 1
print(total)