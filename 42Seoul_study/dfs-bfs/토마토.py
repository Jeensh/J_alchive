from collections import deque
import sys
input = sys.stdin.readline

# 디버깅용
# def print_box(box):
#     print("-미로-")
#     for x in box:
#         for y in x:
#             print(y, end=' ')
#         print()

# 박스안에 안익은 토마토가 없으면 True 반환
def check_box(box):
    for line in box:
        for tomato in line:
            if tomato == 0:
                return False
    return True

# 익은 토마토 위치 큐에 넣기
def put_ripenTomato(box, row, col):
	for r in range(row):
		for c in range(col):
			if box[r][c] == 1:
				queue.append((r,c,0))

def day_pass(box, queue):
	while queue:
		v = queue.popleft()
		day[0] = v[2]
		#상
		if (v[0] - 1 >= 0 and v[1] >= 0) and (v[0] - 1 < row and v[1] < col) and box[v[0] - 1][v[1]] == 0:
			box[v[0] - 1][v[1]] = 1
			queue.append((v[0] - 1, v[1], v[2] + 1))
		#하
		if (v[0] + 1 >= 0 and v[1] >= 0) and (v[0] + 1 < row and v[1] < col) and box[v[0] + 1][v[1]] == 0:
			box[v[0] + 1][v[1]] = 1
			queue.append((v[0] + 1, v[1], v[2] + 1))
		#좌
		if (v[0] >= 0 and v[1] - 1 >= 0) and (v[0] < row and v[1] - 1 < col) and box[v[0]][v[1] - 1] == 0:
			box[v[0]][v[1] - 1] = 1
			queue.append((v[0], v[1] - 1, v[2] + 1))
		#우
		if (v[0] >= 0 and v[1] + 1 >= 0) and (v[0] < row and v[1] + 1 < col) and box[v[0]][v[1] + 1] == 0:
			box[v[0]][v[1] + 1] = 1
			queue.append((v[0], v[1] + 1, v[2] + 1))

if __name__ == "__main__":
    # 상자 만들기
	col, row = map(int, input().split())
	box = [[] for i in range(row)]
	for r in range(row):
		box[r] = list(map(int, input().split()))

	day = [0]
	queue = deque([])
	put_ripenTomato(box, row, col)
	day_pass(box, queue)

	if not check_box(box):
		print(-1)
	else:
		print(day[0])