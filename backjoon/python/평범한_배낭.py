# 백준 : 평범한 배낭

# 배낭을 최대한 가치있게 싸려고 함
# 준서가 여행에 필요하다고 생각하는 n개의 물건이 있음
# 각 물건은 무게 w와 가치 v를 가짐
#   - 해당 물건을 배낭에 넣어서 가면, 준서가 v만큼 즐길 수 있음
# 준서는 최대 k만큼의 무게만을 넣을 수 있음

# 넣을 수 있는 물건들의 가치의 최댓값 구하기

# 제한 조건
#   1 <= n <= 100
#   1 <= k <= 1000000
#   1 <= w <= 100000
#   0 <= v <= 1000

result = 0

# 테이블
#       0  1  2  3  4  5 ... k
# item1 0  0  0  0  0  0  13 
# item2 0  0  0  0  8  8  
# item3 
# item4
# itemn

def solve(data, n, k):
    table = [[0] * (k + 1) for _ in range(n)]
    w, v = data[0]
    for i in range(w, k + 1):
        table[0][i] = v
    for x in range(1, n):
        w, v = data[x]
        for y in range(k + 1):
            if w > y:
                table[x][y] = table[x - 1][y]
            else:
                table[x][y] = max(table[x-1][y - w] + v, table[x-1][y])
        # print('---------')
        # for s in table:
        #     print(s)
    print(table[n - 1][k])
    

############### 진행 ###############
 
# n, k 입력받기


n, k = map(int, input().split())

# 각 물건의 w, v 입력받기
data = []
for i in range(n):
    w, v = map(int, input().split())
    data.append((w, v))

solve(data, n, k)