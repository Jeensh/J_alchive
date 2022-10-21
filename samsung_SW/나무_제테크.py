# nxn 크기의 땅
# 가장 처음에 양문은 모든 칸에 5만큼 있음

# m개의 나무를 구매해 땅에 심음
# 한 칸에 여러 개의 나무가 심어져 있을 수 있음

# 나무는 다음과 같은 과정 반복
#   - 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1증가
#       - 나무는 자기 칸에 있는 양분만 먹을 수 있음
#       - 하나의 칸에 여러개의 나무가 있다면 어린 나무부터 양분을 먹음
#       - 먹을 만큼의 양분이 없는 경우 즉시 죽음
#   - 여름에는 봄에 죽은 나무가 양분으로 변함
#       - 각각의 죽은 나무마다 나이를 2로 나눈 값이 양분으로 됨(소수점은 버림)
#   - 가을에는 나무가 번식
#       - 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생김
#   - 겨울에는 땅에 양분을 추가함
#       - 각 칸에 추가되는 양분의 양은 A[r][c]이고 입력으로 주어짐

# k년이 지난 후 상도에 땅에 살아있는 나무의 개수를 구하는 프로그램 작성

# 주변 8개
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 봄, 여름 진행
def spring(나무, 땅, n):
    for x in range(n):
        for y in range(n):
            tree_len = len(나무[x][y])
            for k in range(tree_len):
                if 나무[x][y][k] <= 땅[x][y]:
                    땅[x][y] -= 나무[x][y][k]
                    나무[x][y][k] += 1
                else:
                    for _ in range(k, tree_len):
                        땅[x][y] += (나무[x][y].pop() // 2)
                    break
# 가을, 겨울 진행
def fall(나무, 땅, 양분, n):
    for x in range(n):
        for y in range(n):
            tree_len = len(나무[x][y])
            for k in range(tree_len):
                if 나무[x][y][k] % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            나무[nx][ny].insert(0, 1)
            땅[x][y] += 양분[x][y]

# n, m, k 입력받기
n, m, k = map(int, input().split())

# 각 칸에 추가될 양분의 양 입력받기
양분 = []
for i in range(n):
    양분.append(list(map(int, input().split())))

# 땅 : 현재 있는 양분을 담고있음
땅 = [[5] * n for i in range(n)]

# 심은 나무의 정보를 입력받기
# (z, 1) : 나무의 나이, 같은 나이 나무 개수
나무 = [[[] for i in range(n)] for i in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    x = x - 1
    y = y - 1
    나무[x][y].append(z)

day = 0
while day < k:
    spring(나무, 땅, n)
    fall(나무, 땅, 양분, n)
    day += 1

result = 0
for i in range(n):
    for j in range(n):
        result += len(나무[i][j])

print(result)