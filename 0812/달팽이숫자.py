# T = int(input())
# for tc in range(T):
#     N = int(input())  # 그래프 크기
#     graph = [[0] * N for _ in range(N)]  # 그래프
#
#     dx = [1, 0, -1, 0]  # 하, 좌, 상, 우 방향
#     dy = [0, -1, 0, 1]
#     num = 1  # 숫자는 1부터 시작
#
#     for i in range(0, N):  # 가로는 차례대로 숫자를 넣어준다.
#         graph[0][i] = num
#         num += 1
#
#     x, y = 0, N - 1  # 가로가 끝난 후 시작하는 곳
#     cnt = N - 1  # 횟수 카운트
#     direction = 0  # 방향
#
#     # 4칸 사각형 기준으로 오른쪽으로 처음에 4칸을 진행하면 그 다음부터는 3칸이동 2번, 2칸이동 2번, 1칸이동 2번으로 마무리를 해준다.
#     # 그래서 for문을 2번씩 진행하고 카운트를 -1씩 해주었다.
#     while True:
#         # 횟수가 0이되면 숫자가 다 찼으므로 탈출
#         if cnt == 0:
#             break
#
#         # 한 방향으로 횟수 카운트 만큼 숫자를 넣어준다.
#         for _ in range(cnt):
#             x += dx[direction]
#             y += dy[direction]
#             graph[x][y] = num
#             num += 1
#
#         # 한방향이 끝났으니 다른방향으로 바꿔준다.
#         direction += 1
#         if direction == 4:
#             direction = 0
#
#         # 똑같이 한 방향을 넣어준다.
#         for _ in range(cnt):
#             x += dx[direction]
#             y += dy[direction]
#             graph[x][y] = num
#             num += 1
#
#         # 방향이 끝났으니 다른방향으로 바꿔주고 direction이 4가 되면 다시 맨 앞으로 돌아오게 설정해준다.
#         cnt -= 1
#         direction += 1
#         if direction == 4:
#             direction = 0
#
#     print("#{}".format(tc + 1))
#     for row in range(len(graph)):
#         for col in range(len(graph)):
#             print(graph[row][col], end=' ')
#         print()


# # 2
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# T =int(input())
#
# for tc in range(1, T+1):
#     N =int(input())
#
#     arr = [[0]*N for _ in range(N)]
#
#     d=0     # 방향
#     r=0     # 행좌표
#     c=0     # 열좌표
#     num = 1 # 내가 찍을 수
#
#     while num <= N * N:
#         arr[r][c] = num
#         num += 1
#
#         # 다음 칸을 결정 해야한다.
#         nr = r + dr[d]
#         nc = c + dc[d]
#         # 유효한 좌표인지 검사
#         if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 0:
#             # 무조건 간다.
#             r, c = nr, nc
#         else:
#             d = (d+1) % 4
#             r += dr[d]
#             c += dc[d]
#
#     print("#{}".format(tc))
#     for i in range(N):
#         for j in range(N):
#             print(arr[i][j], end=' ')
#         print()


# 3
# 수평 -> 수직 : 이동거리 -1
# 수직 -> 수평 : 증가, 감소 변환
T =int(input())

for tc in range(1, T+1):
    N =int(input())

    arr = [[0]*N for _ in range(N)]

    r = 0   # 행의 위치
    c = -1  # 열의 위치
    d = 1   # 증감
    k = N   # 이동거리
    num = 1 # 넣을 값

    while True:
        # 수평이동
        for i in range(k):
            c += d
            arr[r][c] = num
            num += 1

        # 수평 -> 수직
        k -= 1
        if k ==0:break

        # 수직이동
        for i in range(k):
            r += d
            arr[r][c] = num
            num += 1

        # 수직 -> 수평
        d *= -1


    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()