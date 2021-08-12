T = int(input())

for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]
    num = int(input())
    ans = 0
    for draw in range(num):
        color = list(map(int, input().split()))
        for i in range(color[0], color[2] + 1):
            for j in range(color[1], color[3] + 1):
                if arr[i][j] != 0 and arr[i][j] != color[4]:
                    arr[i][j] = 3
                    ans += 1
                else:
                    arr[i][j] = color[4]
    print('#{} {}'.format(tc, ans))