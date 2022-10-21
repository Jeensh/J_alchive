# 3 x 3 배열 A
# 인덱스는 1부터 시작, 1초가 지날때마다 배열에 연산이 적용
#   R 연산 : 배열 A의 모든 행에 대해서 정렬을 수행한다, 행의 개수 >= 열의 개수인 경우에 적용
#   C 연산 : 배열 A의 모든 열에 대해서 정렬을 수행한다, 행의 개수 < 열의 개수 인 경우에 적용

# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다
# 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다
# 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다
# 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다

# 정렬된 결과를 배열에 다시 넣으면, 행 또는 열의 크기가 달라질 수 있다
# R연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고,
# C연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다
# 행 또는 열의 크기가 커진 곳에는 0이 채워진다, 수를 정렬할 때 0은 무시해야 한다
#   예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다

# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다
# 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자

# R연산
def op_R(A):
    # A 배열 분석
    A_len = len(A)
    tmp = [[] for i in range(A_len)]
    for x in range(A_len):
        MAX = max(A[x])
        for i in range(1, MAX + 1):
            n = A[x].count(i)
            if n == 0:
                continue
            tmp[x].append((n, i))
        tmp[x].sort()

    # 분석 결과로 정렬 수행한 행렬 만들기
    result = [[] for i in range(A_len)]
    MAX_len = 0
    for x in range(A_len):
        for item in tmp[x]:
            n, i = item
            result[x].append(i)
            result[x].append(n)
        MAX_len = max(MAX_len, len(result[x]))

    # 정렬 수행한 행렬에 0 알맞게 채우기
    for x in range(A_len):
        padding = MAX_len - len(result[x])
        for i in range(padding):
            result[x].append(0)
    return result

# C연산
def op_C(A):
    # A 행렬 뒤집기
    A = spin(A)

    # A 배열 분석
    A_len = len(A)
    tmp = [[] for i in range(A_len)]
    for x in range(A_len):
        MAX = max(A[x])
        for i in range(1, MAX + 1):
            n = A[x].count(i)
            if n == 0:
                continue
            tmp[x].append((n, i))
        tmp[x].sort()

    # 분석 결과로 정렬 수행한 행렬 만들기
    result = [[] for i in range(A_len)]
    MAX_len = 0
    for x in range(A_len):
        for item in tmp[x]:
            n, i = item
            result[x].append(i)
            result[x].append(n)
        MAX_len = max(MAX_len, len(result[x]))

    # 정렬 수행한 행렬에 0 알맞게 채우기
    for x in range(A_len):
        padding = MAX_len - len(result[x])
        for i in range(padding):
            result[x].append(0)

    # 행렬 뒤집기
    result = spin(result)

    return result

# 행렬 뒤집기
def spin(A):
    r = len(A)
    c = len(A[0])
    result = [[0] * r for i in range(c)]
    for x in range(r):
        for y in range(c):
            result[y][x] = A[x][y]
    return result


# r, c, k 입력받기
r, c, k = map(int, input().split())
r -= 1
c -= 1

# 배열 A에 들어있는 수를 입력받기
A = []
for i in range(3):
    A.append(list(map(int, input().split())))

for i in range(101):
    row_len = len(A)
    col_len = len(A[0])
    if r < row_len and c < col_len and A[r][c] == k:
        print(i)
        break
    if i == 100:
        print(-1)
        break
    if row_len >= col_len:
        A = op_R(A)
    else:
        A = op_C(A)
