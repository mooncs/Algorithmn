T = int(input())
for tc in range(1, T+1):
    # K : 이동 할 수 있는 거리
    # N : 마지막 종점의 위치(0번 정류장부터 출발)
    # M : 충전소의 개수
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))

    bus_stop = [0] * (N+1)

    # 충전소를 표시!!
    # for i in charge:
    #     bus_stop[i] = 1
    # 위와 동일한 표현
    for i in range(M):
        bus_stop[charge[i]] = 1

    bus_idx = 0     # 현재 버스의 위치
    ans = 0         # 충전할 횟수

    # 무한루프는 종료를 주의해야한다.
    while True:
        # 버스가 이동할 수 있는만큼 무조건 가
        bus_idx += K
        # 종점과 같거나 그 이상 움직일 경우 while문 종료
        if bus_idx >= N:break
        # 이동한 거리만큼 확인하겠다.
        for i in range(bus_idx, bus_idx - K, -1):
            # 충전소가 있다면 충전횟수 갱신
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus_idx = i
                break
        # 범위안에 충전소가 없을 경우
        # for문이 정상적으로 다 돌았을 때, else 실행
        else:
            ans = 0
            break

    print('#{} [}'.format(tc, ans))