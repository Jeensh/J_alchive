from collections import deque

# 진입 차수가 0인 원소 큐에 넣기, 한번에 두개가 들어가면 False 리턴
def setQueue(q, levels):
    count = 0
    for i in range(1, len(levels)):
        if levels[i] == 0:
            levels[i] = -1
            q.appendleft(i)
            count += 1
    if count > 1:
        return False
    else:
        return True

# n개의 팀 1~n
# 테스트 케이스 수 입력받기
t = int(input())

for _ in range(t):
    # 팀의 수
    n = int(input())
    # 작년 순위 - 인덱스가 순위
    last_rank = list(map(int, input().split()))
    # 상대적인 등수가 바뀐 상의 수 m
    m = int(input())
    # 등수가 바뀐 쌍 정보
    changed = []
    for i in range(m):
        a, b = map(int, input().split())
        changed.append((a, b))

    # 자기보다 낮은 순위를 가리키도록 방향 그래프를 만들기
    graph = [[] for i in range(n + 1)]
    for i in range(1, n + 1):
        graph[last_rank[i - 1]] += last_rank[i:]

    # 등수가 바뀐 녀석들 방향 그래프 바꿔주기
    for c in changed:
        if last_rank.index(c[0]) < last_rank.index(c[1]):
            graph[c[0]].remove(c[1])
            graph[c[1]].append(c[0])
        else:
            graph[c[1]].remove(c[0])
            graph[c[0]].append(c[1])

    # 진입 차수 테이블 만들기
    levels = [0] * (n + 1)
    for l in graph:
        for i in l:
            levels[i] += 1

    # 위상 정렬 수행하기
    flag = False
    result = []
    q = deque([])

    if not setQueue(q, levels):
        print("?")
        continue
    while q:
        now = q.pop()
        result.append(now)
        for i in graph[now]:
            levels[i] -= 1
        if not setQueue(q, levels):
            print("?")
            flag = True

    if flag:
        print("?")
        continue
    elif len(result) != n:
        print("IMPOSSIBLE")
        continue
    else:
        for i in result:
            print(i, end = ' ')
        print()