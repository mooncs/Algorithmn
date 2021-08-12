def prefix_sum():
    T = int(input())
    for tc in range(1, T + 1):
        len_sum = list(map(int, input().strip().split()))
        numbers = list(map(int, input().strip().split()))
        sum_min, sum_max = 1000000, 0

        # 초기값 설정, 주어진 조건은 1이상의 정수이므로 필요없음
        # for i in range(len_sum[1]):
        #     sum_min += numbers[i]
        #     sum_max += numbers[i]

        # ?
        for i in range(0, len_sum[0] - (len_sum[1] - 1)):
            temp = 0
            for j in range(len_sum[1]):
                temp += numbers[i + j]
            if sum_min > temp:
                sum_min = temp
            if sum_max < temp:
                sum_max = temp

        print("#{} {}".format(tc, sum_max - sum_min))


prefix_sum()