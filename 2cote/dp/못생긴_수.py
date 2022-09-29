# 못생긴 수 : 2, 3, 5만을 소인수로 가지는 수

# n 입력받기
n = int(input())

result = [1]
i = 2
while len(result) < n:
    tmp = i
    while 1:
        if tmp == 1:
            result.append(i)
            break
        if tmp % 2 == 0:
            tmp /= 2
            continue
        if tmp % 3 == 0:
            tmp /= 3
            continue
        if tmp % 5 == 0:
            tmp /= 5
            continue
        break
    i += 1

print(result[-1])
