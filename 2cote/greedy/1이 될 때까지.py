# 입력 받기
N, K = map(int, input().split())

# 1이 될때까지 연산
count = 0
while(N != 1):
    count += 1
    if N % K == 0 and K != 1:
        N = N / K
        continue
    N = N - 1

# 출력
print(count)