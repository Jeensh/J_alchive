import sys
sys.setrecursionlimit(10 ** 6)

def dfs(computers, com, infested):
	if not infested[com]:
		infested[com] = True
		count[0] = count[0] + 1
		for c in computers[com]:
			dfs(computers, c, infested)


if __name__ == "__main__":
	N = int(input())
	M = int(input())
	computers = [[] for i in range(N + 1)]
	for i in range(M):
		c1, c2 = map(int, input().split())
		computers[c1].append(c2)
		computers[c2].append(c1)
	infested = [False] * (N + 1)
	count = [0]
	dfs(computers, 1, infested)
	print(count[0] - 1)