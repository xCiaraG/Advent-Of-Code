from sys import stdin

def repeat(s):
	for i in range(len(s) - 2):
		if s[i] == s[i + 2]:
			return True
	return False

def pair(s):
	for i in range(len(s) - 2, -1, -1):
		if s.index(s[i : i + 2]) < i - 1:
			return True
	return False

def nice(s):
	if repeat(s) and pair(s):
		return 1
	return 0

print(sum([nice(x.strip()) for x in stdin.readlines()]))