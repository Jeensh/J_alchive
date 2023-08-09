# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점(i, j)에 대해서
# i에서 j로 가는 경로가 있는지 없는지 구하시오

# 플로이드 워셜 알고리즘 수행
def floyd(graph, n):
    for k in range(n):
        for x in range(n):
            for y in range(n):
                if graph[x][y] == 1:
                    continue
                else:
                    if graph[x][k] + graph[k][y] == 2:
                        graph[x][y] = 1


############## 진행 ##############
# 정점의 개수 n입력받기
n = int(input())

# 그래프 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

floyd(graph, n)
for i in graph:
    for j in i:
        print(j, end = ' ')
    print()
