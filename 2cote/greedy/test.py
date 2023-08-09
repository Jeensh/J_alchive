def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result

# print(comb([0, 1, 2, 3], 2))


def perm(arr, n):
    result = []
    # 뽑아야 하는 개수가 구슬의 수보다 많은 경우 - 빈 리스트 반환
    if n > len(arr):
        return result

    # 뽑아야 하는 개수가 1인경우 - 한 개씩 원소로 해서 반환
    if n == 1:
        for i in arr:
            result.append([i])
    # 뽑아야 하는 개수가 2개 이상인 경우
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            print(ans)
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]] + p)
    return result

print(perm([0, 1, 2, 3], 2))