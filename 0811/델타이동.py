arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r = 0
c = 1
N = 3

# 상하좌우
dr = [-1, 1 ,0, 0]
dc = [0, 0, -1, 1]
# 위와 동일
drc = [[-1,0], [1,0], [0,-1], [0,1]]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    # nr = r + drc[i][0]
    # nc = r + drc[i][1]

    # 범위 안에 들어와 있을 때 코드를 실행
    # if 0 <= nr <N and 0 <= nc < N:
    #     print(arr[nr][nc], end=' ')

    # 범위 안에 들어오지 않으면 다음 차례로 넘긴다.
    if nr < 0 or nr >= N or nc <o or nc >= N:
        continue
    print(arr[nr][nc], end=' ')