from collections import deque

# 디버깅용
# def print_maze(maze):
#     print("-미로-")
#     for x in maze:
#         for y in x:
#             print(y, end=' ')
#         print()

def solve_maze(maze):
	# 0,0 부터 출발, 3번째 요소는 count
	queue = deque([(0,0,1)])
	while queue:
		v = queue.popleft()
		maze[v[0]][v[1]] = 0

		if v[0] == N - 1 and v[1] == M - 1:
			return v[2]
		# 위쪽 탐색
		if (v[0] - 1 >= 0 and v[1] >= 0) and (v[0] - 1 < N and v[1] < M) and maze[v[0] - 1][v[1]] == 1:
			maze[v[0] - 1][v[1]] = 0
			queue.append((v[0] - 1, v[1], v[2] + 1))
		# 아래 탐색
		if (v[0] + 1 >= 0 and v[1] >= 0) and (v[0] + 1 < N and v[1] < M) and maze[v[0] + 1][v[1]] == 1:
			maze[v[0] + 1][v[1]] = 0
			queue.append((v[0] + 1, v[1], v[2] + 1))
		# 왼쪽 탐색
		if (v[0] >= 0 and v[1] - 1 >= 0) and (v[0] < N and v[1] - 1 < M) and maze[v[0]][v[1] - 1] == 1:
			maze[v[0]][v[1] - 1] = 0
			queue.append((v[0], v[1] - 1, v[2] + 1))
		# 오른쪽 탐색
		if (v[0] >= 0 and v[1] + 1 >= 0) and (v[0] < N and v[1] + 1 < M) and maze[v[0]][v[1] + 1] == 1:
			maze[v[0]][v[1] + 1] = 0
			queue.append((v[0], v[1] + 1, v[2] + 1))


if __name__ == "__main__":
    # N : 행 개수, M : 열 개수
    N, M = map(int, input().split())
    # 미로 생성
    maze = [[] for i in range(N)]
    for row in range(N):
        buf = input().strip()
        for col in range(M):
            maze[row].append(int(buf[col]))
    print(solve_maze(maze))
