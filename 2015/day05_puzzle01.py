from sys import stdin

def nice(s):
	if s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") < 3:
		return 0
	if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
		return 0
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			return 1
	return 0

print(sum([nice(x.strip()) for x in stdin.readlines()]))
