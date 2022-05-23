# 맵 출력
def print_b(board):
    for i in board:
        print(i)

# N 입력받기 교실은 N x N 격자의 공간
N = int(input())
classroom = [[0] * (N) for i in range(N)]

# 각 줄마다 학생의 번호와 좋아하는 학생의 번호 입력받기
data = []
for i in range(N**2):
    a, b, c, d, e = map(int, input().split())
    data.append((a, (b,c,d,e)))

# 빈 칸 리스트
empty_spaces = []
for r in range(N):
        for c in range(N):
            if classroom[r][c] == 0:
                empty_spaces.append((r, c))

for student in data:
    student_id = student[0]
    friends = student[1]
    # (인접한 친구들 수, 인접한 빈칸 수, (x, y))
    avail_spaces = []
    for space in empty_spaces:
        number_of_friends = 0
        number_of_empty = 0
        # 상 하 좌 우
        for x, y in [(-1 ,0), (1, 0), (0, -1), (0, 1)]:
            if (space[0] + x < 0 or space[0] + x > N - 1) or (space[1] + y < 0 or space[1] + y > N - 1):
                continue
            if classroom[space[0] + x][space[1] + y] == 0:
                number_of_empty += 1
                continue
            if classroom[space[0] + x][space[1] + y] in friends:
                number_of_friends += 1
                continue
        avail_spaces.append((number_of_friends, number_of_empty, space))
    # 가장 친구가 많은 자리 순으로 정렬
    avail_spaces.sort()
    avail_spaces.reverse()
    # 가장 친구가 많은 자리보다 친구가 더 적은 자리는 삭제
    tmp = avail_spaces[0][0]
    tmp_list = []
    for i in avail_spaces:
        if i[0] < tmp:
            continue
        tmp_list.append(i)
    avail_spaces = tmp_list
    # 가장 빈자리가 많은 자리 순으로 정렬
    avail_spaces.sort(key = lambda x : x[1])
    avail_spaces.reverse()
    # 가장 빈자리가 많은 자리보다 빈자리가 더 적은 자리는 삭제
    tmp = avail_spaces[0][1]
    tmp_list = []
    for i in avail_spaces:
        if i[1] < tmp:
            continue
        tmp_list.append(i)
    avail_spaces = tmp_list
    # 가장 행과 열의 번호가 작은 칸을 구하기
    tmp = []
    for i in avail_spaces:
        tmp.append(i[2][0] * N + i[2][1])
    tmp.sort()
    x = tmp[0] // N
    y = tmp[0] % N
    classroom[x][y] = student_id
    empty_spaces.remove((x,y))

# 만족도 구하기
result = 0
data.sort()
for r in range(N):
    for c in range(N):
        student_id = classroom[r][c]
        friends = data[student_id - 1][1]
        number_of_friends = 0
        for x, y in [(-1 ,0), (1, 0), (0, -1), (0, 1)]:
            if (r + x < 0 or r + x > N - 1) or (c + y < 0 or c + y > N - 1):
                continue
            if classroom[r + x][c + y] in friends:
                number_of_friends += 1
                continue
        if number_of_friends == 1:
            result += 1
        elif number_of_friends == 2:
            result += 10
        elif number_of_friends == 3:
            result += 100
        elif number_of_friends == 4:
            result += 1000

print(result)