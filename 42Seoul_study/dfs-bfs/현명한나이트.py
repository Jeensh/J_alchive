from collections import deque
import sys
input = sys.stdin.readline

# 디버깅용
# def print_board(board):
#     print("-체스판-")
#     for x in board:
#         for y in x:
#             print(y, end=' ')
#         print()

def kill_enemy(board, queue):
	while queue and enemies:
		v = queue.popleft()
		if (v[0], v[1]) in enemies:
			enemies[enemies.index((v[0], v[1]))] = v[2]
		#상좌
		if (v[0] - 2 >= 0 and v[1] - 1 >= 0) and (v[0] - 2 < N and v[1] - 1 < N) and not board[v[0] - 2][v[1] - 1]:
			board[v[0] - 2][v[1] - 1] = True
			queue.append((v[0] - 2, v[1] - 1, v[2] + 1))
		#좌상
		if (v[0] - 1 >= 0 and v[1] - 2 >= 0) and (v[0] - 1 < N and v[1] - 2 < N) and not board[v[0] - 1][v[1] - 2]:
			board[v[0] - 1][v[1] - 2] = True
			queue.append((v[0] - 1, v[1] - 2, v[2] + 1))
		#좌하
		if (v[0] + 1 >= 0 and v[1] - 2 >= 0) and (v[0] + 1 < N and v[1] - 2 < N) and not board[v[0] + 1][v[1] - 2]:
			board[v[0] + 1][v[1] - 2] = True
			queue.append((v[0] + 1, v[1] - 2, v[2] + 1))
		#하좌
		if (v[0] + 2 >= 0 and v[1] - 1 >= 0) and (v[0] + 2 < N and v[1] - 1 < N) and not board[v[0] + 2][v[1] - 1]:
			board[v[0] + 2][v[1] - 1] = True
			queue.append((v[0] + 2, v[1] - 1, v[2] + 1))
		#상우
		if (v[0] - 2 >= 0 and v[1] + 1 >= 0) and (v[0] - 2 < N and v[1] + 1 < N) and not board[v[0] - 2][v[1] + 1]:
			board[v[0] - 2][v[1] + 1] = True
			queue.append((v[0] - 2, v[1] + 1, v[2] + 1))
		#우상
		if (v[0] - 1 >= 0 and v[1] + 2 >= 0) and (v[0] - 1 < N and v[1] + 2 < N) and not board[v[0] - 1][v[1] + 2]:
			board[v[0] - 1][v[1] + 2] = True
			queue.append((v[0] - 1, v[1] + 2, v[2] + 1))
		#우하
		if (v[0] + 1 >= 0 and v[1] + 2 >= 0) and (v[0] + 1 < N and v[1] + 2 < N) and not board[v[0] + 1][v[1] + 2]:
			board[v[0] + 1][v[1] + 2] = True
			queue.append((v[0] + 1, v[1] + 2, v[2] + 1))
		#하우
		if (v[0] + 2 >= 0 and v[1] + 1 >= 0) and (v[0] + 2 < N and v[1] + 1 < N) and not board[v[0] + 2][v[1] + 1]:
			board[v[0] + 2][v[1] + 1] = True
			queue.append((v[0] + 2, v[1] + 1, v[2] + 1))

if __name__ == "__main__":
	N, M = map(int, input().split())
	X, Y = map(int, input().split())
	# 나이트의 첫 위치
	pos = (X - 1, Y - 1, 0)
	# 지도 만들기
	board = [[False for i in range(N)] for i in range(N)]
	enemies = []

	# 체스판에 적군 놓기
	for i in range(M):
		A, B = map(int, input().split())
		enemies.append((A - 1, B - 1))

	queue = deque([pos])
	board[pos[0]][pos[1]] = True
	kill_enemy(board, queue)
	for e in enemies:
		print(e, end=' ')