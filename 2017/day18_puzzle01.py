from sys import stdin
from collections import defaultdict

def integer(a):
	if a in variables:
		return variables[a]
	else:
		return int(a)

def sett(a, b):
	variables[a] = integer(b)

def add(a, b):
	variables[a] += integer(b)

def mul(a, b):
	variables[a] *= integer(b)

def mod(a, b):
	variables[a] %= integer(b)

def jgz(a, b):
	global i 
	if variables[a] > 0:
		i += integer(b) - 1

cmds = {"set" : sett, "add": add, "mul" : mul, "mod" : mod, "jgz" : jgz}
variables = defaultdict(int)
rcv = 0 

instructions = {}
lines = stdin.readlines()
for i in range(len(lines)):
	instructions[i] = lines[i].strip()

i = 0
while True:
	current = instructions[i].strip().split()
	if len(current) == 3:
		cmds[current[0]](current[1], current[2])
	elif current[0] == "snd":
		rcv = variables[current[1]]
	elif variables[current[1]] != 0:
		print(rcv)
		break
	i += 1