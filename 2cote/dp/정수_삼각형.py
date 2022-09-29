# 삼각형의 크기 n 입력받기
n = int(input())

# 삼각형 정보 입력받기
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(tri[i])):
        ni = i - 1
        # 왼쪽 위
        nj1 = j - 1
        # 오른쪽 위
        nj2 = j
        if nj1 >= 0:
            left_up = tri[ni][nj1]
        else:
            left_up = 0
        if nj2 < len(tri[ni]):
            right_up = tri[ni][nj2]
        else:
            right_up = 0
        tri[i][j] += max(left_up, right_up)

print(max(tri[n - 1]))