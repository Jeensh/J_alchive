import sys
sys.setrecursionlimit(10 ** 6)

# 디버깅용
def print_danzi(danzi):
    print("-단지-")
    for x in danzi:
        for y in x:
            print(y, end=' ')
        print()

def dfs(danzi, pos, danzi_i):
	if pos[0] < 0 or pos[1] < 0:
		return
	if pos[0] < N and pos[1] < N and danzi[pos[1]][pos[0]] == 1:
#		디버깅용
#		print("-",str(pos),"-")
		pos_l = []
		pos_l = pos
  		# 방문한 곳 0으로 set
		danzi[pos_l[1]][pos_l[0]] = 0
		houses_in_danzi[danzi_i] += 1
		# 위쪽 탐색
		pos_l = (pos[0], pos[1] + 1)
		dfs(danzi, pos_l, danzi_i)
		# 아래 탐색
		pos_l = (pos[0], pos[1] - 1)
		dfs(danzi, pos_l, danzi_i)
		# 왼쪽 탐색
		pos_l = (pos[0] - 1, pos[1])
		dfs(danzi, pos_l, danzi_i)
		# 오른쪽 탐색
		pos_l = (pos[0] + 1, pos[1])
		dfs(danzi, pos_l, danzi_i)

def count_danzi(danzi):
	danzis = 0
	for y in range(N):
		for x in range(N):
			if danzi[y][x] == 1:
				houses_in_danzi.append(0)
#				디버깅용
#				print((x,y))
				danzis = danzis + 1
				# dfs로 방문한 곳 전부 0으로 치환
				pos = [x, y]
				dfs(danzi, pos, danzis - 1)
	return danzis

if __name__ == "__main__":
	N = int(input())
	danzi = [[] for i in range(N)]
	for i in range(N):
		tmp = input().strip()
		for j in range(N):
			danzi[i].append(int(tmp[j]))
	houses_in_danzi = []
	print(count_danzi(danzi))
	houses_in_danzi.sort()
	for d in houses_in_danzi:
		print(d)
