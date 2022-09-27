# 학생 N명의 성적을 분실
# 성적을 비교한 결과의 일부만 가지고 있음
# 학생 N명의 성적은 모두 다름
INF = int(1e9)

# 학생들의 수 n, 성적을 비교한 횟수 m
n, m = map(int, input().split())

# 성적 비교결과로 그래프 만들기
graph = [[0] * (n + 1) for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 테이블 갱신하기
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1

count = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] == 1:
            tmp += 1
        if graph[j][i] == 1:
            tmp += 1
    if tmp == n - 1:
        count += 1

print(count)