# 볼링공의 개수 N 공의 최대 무게 M 입력받기
n, m = map(int, input().split())

# 각 볼링공의 무게 입력받기
weight = list(map(int, input().split()))

# 조합 함수
def comb(arr, r):
    result = []

    if r > len(arr):
        return result

    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr) - (r-1)):
            for j in comb(arr[i + 1:], r - 1):
                if j[0] == arr[i]:
                    continue
                result.append([arr[i]] + j)
    return result

print(comb(weight, 2))
print(len(comb(weight, 2)))
