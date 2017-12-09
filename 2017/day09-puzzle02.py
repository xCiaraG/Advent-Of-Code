line = input().strip()
i = 0
cancelled = 0
while i < len(line):
	if line[i] == "!":
		i += 1
	elif line[i] == "<":
		i += 1
		while line[i] != ">":
			if line[i] == "!":
				i += 1
			else:
				cancelled += 1
			i += 1
	i += 1
print(cancelled)