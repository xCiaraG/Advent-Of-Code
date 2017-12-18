brackets = input().strip()
total = 0
for i in range(len(brackets)):
	if brackets[i] == "(":
		total += 1
	else:
		total -= 1
	if total < 0:
		print(i + 1)
		break
