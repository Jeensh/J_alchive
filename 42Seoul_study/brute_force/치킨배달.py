import sys
input = sys.stdin.readline
from itertools import combinations

# 입력 받기 및 지도 생성
N, M = map(int, input().split())
map = [[] for i in range(N)]
tmp = []
for i in range(N):
	map[i] = list(input().split())

# 치킨집들과 가정집들 위치 리스트로 추출
chicken_houses = []
homes = []
for row in range(N):
	for col in range(N):
		tmp = map[row][col]
		if tmp == '2':
			chicken_houses.append((row, col))
		elif tmp == '1':
			homes.append((row, col))

# 최소 도시 치킨 거리 초기화
MIN = 1000000

# 치킨집들 중 M개를 선택하는 조합 구하기
c_comb = list(combinations(chicken_houses, M))

# 각 조합마다 도시 치킨거리를 구해서 최소 도시 치킨거리 갱신하기
for comb in c_comb:
	mcd = 0
	for h in homes:
		tmp = 10000000
		for c in comb:
			tmp = min(tmp, abs(h[0] - c[0]) + abs(h[1] - c[1]))
		mcd = mcd + tmp
		if mcd > MIN:
			break
	MIN = min(MIN, mcd)

print(MIN)

