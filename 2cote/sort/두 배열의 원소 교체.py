# N, K 입력받기
n, k = map(int, input().split())

# 배열 A, B 입력받기
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순으로 B는 내림차순으로 정렬
A.sort()
B.sort()
B.reverse()

# 최대 K번 까지 A의 가장 작은 원소와 B의 가장 큰 원소를 교체
for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

# A의 합 출력
print(sum(A))