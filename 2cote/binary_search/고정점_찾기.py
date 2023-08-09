# 고정점 : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소

# n 입력받기
n = int(input())

# 수열 입력받기
data = list(map(int, input().split()))

# 이진 탐색
start = 0
end = n - 1
def binary_search(start, end, data):
    mid = (start + end) // 2
    if start > end:
        return -1
    if data[mid] == mid:
        return mid
    elif data[mid] > mid:
        return binary_search(start, mid - 1, data)
    elif data[mid] < mid:
        return binary_search(mid + 1, end, data)

print(binary_search(start, end, data))