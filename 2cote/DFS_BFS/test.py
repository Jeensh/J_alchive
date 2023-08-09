# 순열 함수
def perm(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            tmp = [i for i in arr]
            tmp.remove(arr[i])
            for j in perm(tmp, n - 1):
                if [arr[i]] + j not in result:
                    result.append([arr[i]] + j)
    return result

print(perm([1, 1, 2,3], 3))