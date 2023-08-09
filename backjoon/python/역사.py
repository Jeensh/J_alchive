# 알고 있는 일부 사건들의 전후 관계가 주어질 때, 주어진 사건들의 전후 관계도 알아보자

# 플로이드 워셜로 먼저 일어난 것에 a가 b보다 먼저 일어났으면 graph[a][b] = 1로 바꾸기
def solve(graph, n):
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if graph[x][y] == 1:
                    graph[y][x] = 0
                    continue
                elif graph[x][y] == 0:
                    graph[y][x] = 1
                    continue
                else:
                    if graph[x][k] == 1 and  graph[k][y] == 1:
                        graph[x][y] = 1
                        graph[y][x] = 0
                    elif graph[x][k] == 0 and  graph[k][y] == 0:
                        graph[x][y] = 0
                        graph[y][x] = 1

########## 진행 ##########
# 사건의 개수 n과 알고있는 사건의 전후 관계의 개수 k를 입력받기
n, k = map(int, input().split())

# 전후 관계를 알고있는 두 사건씩 입력받기
# a가 b보다 먼저 일어남
graph = [[-1] * (n + 1) for _ in range(n + 1)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 0

# 전후 관계를 알고 싶은 사건쌍의 수 s를 입력받기
s = int(input())

# 각 사건쌍 입력받기
# a가 b보다 먼저 일어났으면 -1, b가 먼저 일어났으면 1, 모르면 0을 출력한다
problem = []
for i in range(s):
    a, b = map(int, input().split())
    problem.append((a, b))

# for i in graph:
#     print(i)
solve(graph, n)
# for i in graph:
#     print(i)

for a, b in problem:
    if graph[a][b] == 1:
        print(-1)
    elif graph[a][b] == 0:
        print(1)
    else:
        print(0)