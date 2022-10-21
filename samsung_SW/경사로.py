# n x n 인 지도
# 각 칸에는 그곳의 높이가 적혀있음
# 길을 지나가려면 길에 속한 모든 높이가 같아야 한다
#   - 또는 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다
#   - 경사로의 높이는 1이고 길이는 L이다, 개수는 무한이다
# 경사로를 같은곳에 여러개 놓을 수는 없다

# 가로 길
# 한 위치씩 가면서 다음 위치와 현재 위치의 높이차가 1이면 count 시작
#   - count가 l미만인데 위치가 2이상 차이나면 해당 길은 갈 수 없음
#   - count가 l이상이면 다시 카운트를 0으로 돌림
#   - 해당 길 끝까지 통과하면 통과가능한 길 판단
def check_h(board, i, n, l):
    # 앞에서부터 탐색
    count = 1 # 연속된 수의 개수
    past = board[i][0]
    j = 1
    while j < n:
        now = board[i][j]
        # 이전 수와 같은 경우
        if now == past:
            past = now
            count += 1
        # 이전 수보다 1큰 경우
        elif now - past == 1:
            # 연속된 이전 수가 경사로 크기보다 같나 큰 경우
            if count >= l:
                past = now
                count = 1
            # 연속된 이전 수가 경사로 크기보다 작은 경우
            else:
                return False
        # 이전 수보다 1작은 경우
        elif now - past == -1:
            c_tmp = 0
            for k in range(j, n):
                n_tmp = board[i][k]
                if n_tmp == now:
                    c_tmp += 1
                if c_tmp >= l:
                    past = n_tmp
                    j = k
                    count = 0
                    break
                if n_tmp != now:
                    return False
                if k == n-1:
                    return False
        # 이전 수보다 2이상 크거나 작은 경우
        else:
            return False
        j += 1
    return True


# 세로 길
def check_v(board, i, n, l):
    # 앞에서부터 탐색
    count = 1 # 연속된 수의 개수
    past = board[0][i]
    j = 1
    while j < n:
        now = board[j][i]
        # 이전 수와 같은 경우
        if now == past:
            past = now
            count += 1
        # 이전 수보다 1큰 경우
        elif now - past == 1:
            # 연속된 이전 수가 경사로 크기보다 같나 큰 경우
            if count >= l:
                past = now
                count = 1
            # 연속된 이전 수가 경사로 크기보다 작은 경우
            else:
                return False
        # 이전 수보다 1작은 경우
        elif now - past == -1:
            c_tmp = 0
            for k in range(j, n):
                n_tmp = board[k][i]
                if n_tmp == now:
                    c_tmp += 1
                if c_tmp >= l:
                    past = n_tmp
                    j = k
                    count = 0
                    break
                if n_tmp != now:
                    return False
                if k == n-1:
                    return False
        # 이전 수보다 2이상 크거나 작은 경우
        else:
            return False
        j += 1
    return True


if __name__  == "__main__":
    # n, 과 l 입력받기
    n, l = map(int, input().split())

    # 맵 입력받기
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    # 결과
    result = 0

    # 가로길 확인
    for i in range(n):
        if check_h(board, i, n, l):
            # print("**", i)
            result += 1
    # 세로길 확인
    for i in range(n):
        if check_v(board, i, n, l):
            # print("--", i)
            result += 1

    print(result)