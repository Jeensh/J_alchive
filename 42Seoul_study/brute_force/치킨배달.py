import sys
input = sys.stdin.readline

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

def solve(dept, chicken_houses_t):
	global M, MIN
	# 치킨집들 중 M개가 선택 되면
	if dept == M:
		# 이때의 도시 치킨 거리를 구하기
		tmp = 0
		for h in homes:
			mcd = 1000000
			for c in chicken_houses_t:
				mcd = min(mcd, abs(h[0] - c[0]) + abs(h[1] - c[1]))
			tmp = tmp + mcd
		# 방금 구한 도시 치킨 거리와 지금까지 구한 최소 도시 치킨 거리를 비교
		MIN = min(MIN, tmp)
		return
	# 치킨집들 중 M개 선택하기
	for c in chicken_houses:
		if c in chicken_houses_t:
			continue
		chicken_houses_l = chicken_houses_t[:]
		chicken_houses_l.append(c)
		solve(dept + 1, chicken_houses_l)

solve(0, [])
print(MIN)

