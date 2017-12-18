from sys import stdin
from collections import defaultdict

def integer(a, ids):
	if a in "abcdefghijklmnopqrstuvwxyz":
		return dicts[ids][a]
	else:
		return int(a)

def sett(a, b, ids):
	dicts[ids][a] = integer(b, ids)

def add(a, b, ids):
	dicts[ids][a] += integer(b, ids)

def mul(a, b, ids):
	dicts[ids][a] *= integer(b, ids)

def mod(a, b, ids):
	dicts[ids][a] %= integer(b, ids)

def jgz(a, b, ids):
	if integer(a, ids) > 0:
		ij[ids] += integer(b, ids) - 1

def run(instruction, ids):
	if len(instruction) == 3:
		cmds[instruction[0]](instruction[1], instruction[2], ids)
	elif instruction[0] == "snd":
		counts[ids] += 1
		rcv[ids - 1].append(integer(instruction[1], ids))
	elif rcv[ids]:
		dicts[ids][instruction[1]] = rcv[ids].pop(0)
	else:
		ij[ids] -= 1
		
cmds = {"set" : sett, "add": add, "mul" : mul, "mod" : mod, "jgz" : jgz}
dicts = [defaultdict(int), defaultdict(int)]
dicts[0]["p"] = 0
dicts[1]["p"] = 1
rcv = [[], []]
counts = [0, 0] 
ij = [0, 0]

instructions = {}
lines = stdin.readlines()
for i in range(len(lines)):
	instructions[i] = lines[i].strip()

while True:
	current1 = instructions[ij[0]].strip().split()
	current2 = instructions[ij[1]].strip().split()
	if current1[0] == "rcv" and current2[0] == "rcv" and not rcv[0] and not rcv[1]:
		break
	run(current1, 0)
	run(current2, 1)
	ij[0] += 1
	ij[1] += 1

print(counts[1])