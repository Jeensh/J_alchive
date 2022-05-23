import sys
input = sys.stdin.readline

# 시험장의 개수 N 입력받기
N = int(input())

# 각 시험장에 있는 응시자의 수
testrooms = list(map(int, input().split()))

# 총감독관이 한 시험장에서 감시할 수 있는 응시자의 수 B, 부감독관은 C
B, C = map(int, input().split())

chief = 0
sub = 0

for t in testrooms:
    if t == 0:
        continue
    elif t < B:
        chief += 1
        continue
    else:
        chief += 1
        t -= B
        sub += t // C
        if t % C != 0:
            sub += 1
print(chief + sub)