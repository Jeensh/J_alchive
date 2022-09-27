from gettext import find
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 팀 합치기 연산 (union)
def union(parent, a, b):
    if parent[a] < parent[b]:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

# 부모 초기화 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 같은 팀 여부 확인 (find)
def isInSameTeam(parent, a, b):
    if parent[a] == parent[b]:
        return "YES"
    return "NO"

# N과 M입력받기
N, M = map(int, input().split())

# 부모 리스트 초기화
parent = [i for i in range(N + 1)]

# 출력 문자열
result = []

# M개의 연산 입력받아 처리하기
for i in range(M):
    type, n1, n2 = map(int, input().split())
    if type == 0:
        union(parent, n1, n2)
    elif type == 1:
        result.append(isInSameTeam(parent, n1, n2))

# 결과 출력
for text in result:
    print(text)
