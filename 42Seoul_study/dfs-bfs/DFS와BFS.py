import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def dfs(graph, v, visited):
    # 방문하지 않은 곳이면
	if not visited[v]:
		print(v, end = ' ')
		# 방문처리 한다
		visited[v] = True
		# 가까운 연결된 곳부터 들어간다
		for p in graph[v]:
			dfs(graph, p, visited)

def bfs(graph, start, visited):
    # 시작 정점 큐에 넣기
	queue = deque([start])
	visited[start] = True
	while queue:
		# 큐에서 하나 뽑아서 출력(방문)
		v = queue.popleft()
		print(v, end = ' ')
		# 아직 방문하지 않은 인접한 노드들을 큐에 삽입
		for p in graph[v]:
			if not visited[p]:
				queue.append(p)
				# 방문처리
				visited[p] = True



if __name__ == "__main__":
    # N : 정점의 개수, M : 간선의 개수, V : 시작 정점 번호
	N, M, V = map(int, input().split())
	graph = [[] for i in range(N + 1)]
 	# 각 간선에 연결된 두 정점 입력 받기
	edge = []
	for i in range(M):
		edge.append(list(map(int, input().split())))
	# 각 정점에 인접한 정점을 요소로 추가해주기
	for e in edge:
		graph[e[0]].append(e[1])
		graph[e[1]].append(e[0])
	# 방문 정보 확인용 리스트 생성
	visited = [False for i in range(N + 1)]

	# 정점마다 인접 정점 오름차순으로 정렬
	for v in range(1, N + 1):
		graph[v].sort()

	# dfs 탐색
	dfs(graph, V, visited)
	print()
	for i in range(N + 1):
		visited[i] = False
	# bfs 탐색
	bfs(graph, V, visited)