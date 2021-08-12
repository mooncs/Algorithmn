for i in range(1, int(input()) + 1):
    N = input()
    card = list(map(int, list(input())))
    counting = [0] * 10
    cnt = 0
    max_value = 0

    for k in card:
        counting[k] += 1

    for j in range(len(counting) - 1, -1, -1):
        if counting[j] > max_value:
            max_value = counting[j]
            cnt = j

    print('#{} {} {}'.format(i, cnt, max_value))