# n과 x 입력받기
n, x = map(int, input().split())

# 수열 입력받기
data = list(map(int, input().split()))

# 시작점, 끝점, 중간점 설정
start = 0
end = len(data) - 1

# 이진 탐색
def b_search(data, target, start, end):
    mid = int( (start + end) / 2 )

    if end < start:
        return -1

    if data[mid] > target:
        return b_search(data, target, start, mid - 1)
    elif data[mid] < target:
        return b_search(data, target, mid + 1, end)
    else:
        return mid

p = b_search(data, x, start, end)

# 첫번째 x의 인덱스 찾기
p_start = p
p_end = p
while p != -1:
    p_start = p
    p = b_search(data, x, start, p)

# 마지막 x의 인덱스 찾기
p = b_search(data, x, start, end)
while p != -1:
    p_end = p
    p_end = b_search(data, x, p, end)

print(p_start, p_end)
# print(b_search(data, x, start, end))
