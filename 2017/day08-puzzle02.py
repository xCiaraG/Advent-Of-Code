from sys import stdin

def greater_than(a, b):
	return a > b

def less_than(a, b):
	return a < b

def greater_than_equal(a, b):
	return a >= b

def less_than_equal(a, b):
	return a <= b

def equal(a, b):
	return a == b

def not_equal(a, b):
	return a != b

lines = stdin.readlines()
variables = {}
functions = {"<" : less_than, ">" : greater_than, "<=" : less_than_equal,
			 ">=" : greater_than_equal, "==" : equal, "!=" : not_equal}
m = 0
for line in lines:
	v1, inc_dec, n1, _, v2, f, n2 = line.strip().split()
	if v1 not in variables:
		variables[v1] = 0
	if v2 not in variables:
		variables[v2] = 0
	if functions[f](variables[v2], int(n2)):
		if inc_dec == "inc":
			variables[v1] += int(n1)
		else:
			variables[v1] -= int(n1)
	if max(variables.values()) > m:
		m = max(variables.values())
print(m)