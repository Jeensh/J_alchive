import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
inings = []
for i in range(N):
	inings.append(list(map(int, input().split())))

players = [0, 1, 2, 3, 4, 5, 6, 7, 8]
arrs = list(permutations(players, 9))

# 타자의 순번
sequence = 0

# 선수 순번이 정해졌을 때 1이닝 경기 시뮬레이션
def play(arr, ining):
	global sequence
	out = 0
	score = 0
	pos = [False, False, False]
	while (out < 3):
		result = ining[arr[sequence]]
		# 아웃일 떄
		if result == 0:
			out += 1
		# 안타일 때
		elif result == 1:
			if pos[2]:
				score += 1
			pos[2] = pos[1]
			pos[1] = pos[0]
			pos[0] = True
		# 2루타일 때
		elif result == 2:
			if pos[2]:
				score += 1
			if pos[1]:
				score += 1
			pos[2] = pos[0]
			pos[1] = True
			pos[0] = False
		# 3루타일 때
		elif result == 3:
			if pos[2]:
				score += 1
			if pos[1]:
				score += 1
			if pos[0]:
				score += 1
			pos[2] = True
			pos[1] = False
			pos[0] = False
		# 홈런일 때
		elif result == 4:
			if pos[2]:
				score += 1
			if pos[1]:
				score += 1
			if pos[0]:
				score += 1
			score += 1
			pos[2] = False
			pos[1] = False
			pos[0] = False
		sequence = (sequence + 1) % 9
	return(score)

MAX = 0
scroe_total = 0
for arr in arrs:
	if arr[3] != 0:
		continue
	sequence = 0
	scroe_total = 0
	for i in range(N):
		scroe_total += play(arr, inings[i])
	MAX = max(MAX, scroe_total)
print(MAX)
