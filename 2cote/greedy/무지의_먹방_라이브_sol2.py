def solution(food_times, k):
    foods = []
    # 남은 음식의 개수
    n = len(food_times)
    # 새로운 리스트에 (음식시간, 음식번호) 형태로 삽입
    for i in range(n):
        foods.append((food_times[i], i+1))
        
    # 음식시간 기준으로 리스트 정렬
    foods.sort()
    
    # 이전에 먹은 음식의 시간
    pretime = 0
    # 음식시간이 낮은 음식부터 순회
    for i, food in enumerate(foods):
        # 현재 음식과 이전 음식의 시간 차이
        diff = food[0] - pretime
        # 만약 차이가 0이 아니라면
        if diff != 0:
            # 사용할 시간은 : 차이 * 남은 음식의 수
            spend = diff * n
            # 만약 사용할 시간이 남은 시간보다 작은 경우
            if spend <= k:
                # 남은 시간에서 사용할 시간을 빼준다
                k -= spend
                # 이전에 먹은 음식을 방금 먹은 음식으로 갱신
                pretime = food[0]
            # 사용할 시간이 남은 시간보다 큰 경우
            else:
                # 다음 음식은 다 먹지 못하니, 남은 시간에서 남은 음식을 나눈 나머지 = 남은 음식 중 먹어야 할 인덱스
                k = k % n
                # 남은 음식을 음식 번호 순으로 정렬한 리스트 생성
                sublist = sorted(foods[i:], key = lambda x : x[1])
                # 정렬한 남은 음식의 남은 음식중 먹어야할 인덱스의 음식번호 반환
                return sublist[k][1]
        # 차이가 0이거나 다음 음식을 먹을 수 있을 때
        n -= 1
    
    # 모든 음식을 다 돌았는데 사용할 시간이 남은 시간보다 작은 경우 -> 시간이 남는 경우
    return -1