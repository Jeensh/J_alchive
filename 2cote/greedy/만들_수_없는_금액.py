
# 조합 함수
def comb(arr, r):
    result = []
    if r > len(arr):
        return result

    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr) - (r - 1)):
            for j in comb(arr[i+1:], r - 1):
                result.append([arr[i]] + j)
    return result

# 동전의 개수 N 입력받기
n = int(input())

# 동전의 화폐 단위 입력받기
cost = list(map(int, input().split()))

def solve(cost, n):
    # 부분집합
    subset = []
    # 부분 집합 별 값을 더한 테이블
    sumSubset = []

    # 부분집합 구하기
    for i in range(n):
        subset = subset + comb(cost, i)
    # 부분 집합별 값을 더한 테이블 작성
    for s in subset:
        sumSubset.append(sum(s))
    sumSubset = set(sumSubset)
    sumSubset = list(sumSubset)

    print(sumSubset)
    # 1부터 시작하여 인덱스와 값이 같지 않은 첫 수 찾기
    for i in range(sum(cost)):
        if i + 1 != sumSubset[i]:
            return i + 1

print(solve(cost, n))
