from xxlimited import foo


def solution(food_times, k):
    answer = 0

    # 시간 초기화
    time = 0

    # 차례 초기화
    turn = 0

    # k시간이 되면 중단
    while time < k:

        # 현재 차례의 음식을 먹음
        # 만약 현재 차례 음식을 다 먹었다면 다음 음식으로 차례 바꿈
        count = 0
        while food_times[turn] == 0:
            count += 1
            # 모든 음식을 다 먹었다면 -1 반환
            if count == len(food_times):
                return -1
            turn = (turn + 1) % len(food_times)
        food_times[turn] -= 1
        # 시간이 흐르고 다음 음식을 가져옴
        time += 1
        turn = (turn + 1) % len(food_times)
        tmp = turn
        while food_times[turn] == 0:
            count += 1
            # 모든 음식을 다 먹었다면 -1 반환
            if count == len(food_times):
                return -1
            turn = (turn + 1) % len(food_times)
        if tmp == turn and food_times[turn] > k:
            return turn + 1


    # 다음에 먹어야 될 음식 반환
    answer = turn + 1
    return answer


print(solution([2000, 0, 0], 5))