def search(start):      # 도착지에서 위로 올라가는 함수
    i = 99      # 행
    j = start   # 열
    while i>0:  # 맨 윗줄로 도착하기 전까지 위로 올라간다.
        i -= 1  # 위로 한 칸 이동
        if j>0 and ladder[i][j-1] == 1:         # 왼쪽 칸이 있고 1이면
            while j>0 and ladder[i][j-1] == 1:  # 사다리를 벗어나거나 0을 만날 때까지 이동
                j -= 1
        elif j<99 and ladder[i][j+1] == 1:      # 오른쪽 칸이 있고 1이면
            while j<99 and ladder[i][j+1] == 1: # 사다리를 벗어나거나 0을 만날 때까지 이동
                j += 1
        # 좌우가 0이면 위로
    return j    # 0번 행에 도착했을 때의 열(출발지)을 리턴

T = 10
for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print("#{} {}".format(tc, ans))



# 2
for a in range(10):
    T = int(input())
    test_list = list(list(map(int, input().split())) for _ in range(100))

    radder = []

    for li in range(len(test_list[0])):  # 사다리 막대를 구함
        if test_list[0][li] == 1:
            radder += [li]               # 사다리가 있는 자리 모두 체크

    for sada in range(len(radder)):  # 첫번째 사다리 막대일때
        cur_p = sada
        for start_p in range(100):  # 바닥까지이동할때
            if cur_p != 0 and test_list[start_p][radder[cur_p] - 1] == 1:
                cur_p -= 1  # 옆 막대로 이동

            elif cur_p != len(radder) - 1 and test_list[start_p][radder[cur_p] + 1] == 1:
                cur_p += 1

        if test_list[99][radder[cur_p]] == 2:  # 막대의 마지막이 이것일때
            print("#{} {}".format(T, radder[sada]))