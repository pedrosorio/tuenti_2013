f = open('lol.txt')
ints = []
for line in f:
	ints.append(int(line))

T = int(raw_input())

for test in range(T):
	n = int(raw_input())
	print ints[n-1]
