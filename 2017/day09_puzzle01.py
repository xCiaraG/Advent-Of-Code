line = input().strip()
i = 0
total = 0
current = 0
while i < len(line):
	if line[i] == "{":
		current += 1
		total += current
	elif line[i] == "}":
		current -= 1
	elif line[i] == "!":
		i += 1
	elif line[i] == "<":
		while line[i] != ">":
			if line[i] == "!":
				i += 1
			i += 1
	i += 1
print(total)