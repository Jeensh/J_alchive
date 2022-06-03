import sys
sys.setrecursionlimit(10 ** 6)

# 가게 부품의 개수 N 입력받기
n = int(input())

# 부품들 입력받기
data = list(map(int, input().split()))

# 찾을 부품의 개수 M 입력받기
m = int(input())

# 찾을 부품들 입력받기
to_find = list(map(int, input().split()))

# 부품 데이터 정렬
data.sort()

# 부품 찾기 함수
def search(goal, start, end):
    global data
    mid = (start + end) // 2
    if start > end:
        return False
    if goal == data[mid]:
        return True
    elif goal < data[mid]:
        return search(goal, start, mid - 1)
    elif goal > data[mid]:
        return search(goal, mid + 1, end)

# 결과 출력
for goal in to_find:
    if search(goal, 0, n - 1):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')