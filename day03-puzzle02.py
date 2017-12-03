def add_spiral(l, n):
	#Add right
	for i in range(len(l) - 1, -1, -1):
		count = l[i][-1]
		if i != 0:
			count += l[i-1][-1]
		if i < len(l) - 1:
			count += l[i+1][-1]
			count += l[i+1][-2]
		l[i].append(count)
		if count > n:
			print(count)
	#Add top
	tmp = []
	for i in range(len(l), -1, -1):
		count = l[0][i]
		if i != 0:
			count += l[0][i-1]
		if i < len(l):
			count += l[0][i+1]
			count += tmp[0]
		tmp = [count] + tmp
		if count > n:
			print(count)
	l = [tmp] + l
	#Add left
	for i in range(len(l)):
		count = l[i][0]
		if i > 0:
			count += l[i-1][0]
			count += l[i-1][1]
		if i < len(l) - 1:
			count += l[i+1][0]
		l[i] = [count] + l[i]
		if count > n:
			print(count)
	#Add bottom
	tmp = []
	for i in range(len(l) + 1):
		count = l[len(l)-1][i]
		if i > 0:
			count += l[len(l)-1][i-1]
			count += tmp[-1]
		if i < len(l[-1]) - 1:
			count += l[len(l)-1][i+1]
		tmp.append(count)
		if count > n:
			print(count)
	l += [tmp]
	return l

n = int(input())
current, count = [[1]], 2
while current[-1][-1] < n:
	current = add_spiral(current, n)
	
