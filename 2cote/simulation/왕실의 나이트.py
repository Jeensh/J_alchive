# 나이트 이동 가능 경로
# 좌상, 좌하, 우상, 우하, 상좌, 상우, 하좌, 하우
pos = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 시작 위치 입력받기
tmp = input()
start = (alpha.index(tmp[0]) + 1, int(tmp[1]))

# 도착 위치 유효성 확인
count = 0
for p in pos:
    dest = (start[0] + p[0], start[1] + p[1])
    if (dest[0] > 0 and dest[0] < 9) and (dest[1] > 0 and dest[1] < 9):
        count += 1

# 결과 출력
print(count)