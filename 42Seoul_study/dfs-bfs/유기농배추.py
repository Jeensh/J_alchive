# id : 00001
import sys
sys.setrecursionlimit(10 ** 6)

# 디버깅용
# def print_patch(patch):
#     print("-배추밭-")
#     for x in patch:
#         for y in x:
#             print(y, end=' ')
#         print()

def worm_dfs(patch, pos, end):
	if pos[0] < 0 or pos[1] < 0:
		return
	if pos[0] < end[0] and pos[1] < end[1] and patch[pos[1]][pos[0]] == 1:
#		디버깅용
#		print("-",str(pos),"-")
		pos_l = []
		pos_l = pos
  		# 방문한 곳 0으로 set
		patch[pos_l[1]][pos_l[0]] = 0
		# 위쪽 탐색
		pos_l = (pos[0], pos[1] + 1)
		worm_dfs(patch, pos_l, end)
		# 아래 탐색
		pos_l = (pos[0], pos[1] - 1)
		worm_dfs(patch, pos_l, end)
		# 왼쪽 탐색
		pos_l = (pos[0] - 1, pos[1])
		worm_dfs(patch, pos_l, end)
		# 오른쪽 탐색
		pos_l = (pos[0] + 1, pos[1])
		worm_dfs(patch, pos_l, end)

def count_worm(patch, end):
	worm = 0
	for y in range(end[1]):
		for x in range(end[0]):
			if patch[y][x] == 1:
#				디버깅용
#				print((x,y))
				worm = worm + 1
				# dfs로 방문한 곳 전부 0으로 치환
				pos = [x, y]
				worm_dfs(patch, pos, end)
	return worm

if __name__ == "__main__":
	# T : 테스트 케이스 개수
	T = int(input())
	patches = []

	# 케이스별 배추밭 만들기
	for case in range(T):
		# M : 배추밭의 가로길이 / N : 배추밭의 세로길이 / K : 배추 개수
		M, N, K = map(int, input().split())
		# pos : 각 배추들의 위치
		pos = []
		for i in range(K):
			pos.append(tuple(map(int, input().split())))
		# 2차원 밭 만들기
		patch = [[0 for x in range(M)] for y in range(N)]
		for y in range(N):
			for x in range(M):
				if (x, y) in pos:
					patch[y][x] = 1
					pos.remove((x, y))
		patches.append([patch,(M, N)])

	# 배추밭별 지렁이 개수 구해서 출력하기
	for patch in patches:
#		디버깅용
#		print_patch(patch[0])
		print(count_worm(patch[0], patch[1]))