t = int(input())

def binarysearch(p, target):
    l = 1
    r = p
    cnt = 0
    while l <= r:
        mid = int((l + r) / 2)
        cnt += 1
        if mid == target:
            return cnt
        elif mid > target:
            r = mid
        else:
            l = mid

    return 1000

for tc in range(t):
    p, a, b = map(int, input().split())
    acnt = binarysearch(p, a)
    bcnt = binarysearch(p, b)

    if acnt > bcnt:
        win = 'B'
    elif acnt < bcnt:
        win = 'A'
    else:
        win = 0
    print('#{} {}'.format(tc + 1, win))