# 박준영
for case in range(10):
    T = int(input())    #
    B = list(map(int, input().split()))     # 빌딩 리스트
    ans = 0     # 답

    for i in range(2, T-2):
        max_B = 0
        if B[i] > B[i-1] and B[i] > B[i-2] and B[i] > B[i+1] and B[i] > B[i+2]:
            for j in (B[i-2], B[i-1], B[i+1], B[i+2]):
                if max_B < j:
                    max_B = j
            ans += B[i] - max_B

    print('#{} {}'.format(case+1, ans))


# 성아영
def my_max(*args):
    max_num = args[0]
    for num in args:
        if num > max_num:
            max_num = num
    return max_num


for T in range(1, 11):
    test_case = int(input())
    height = list(map(int, input().split()))
    result = 0
    for idx in range(2, test_case - 2):
        max_height = my_max(height[idx - 2], height[idx - 1], height[idx + 1], height[idx + 2])
        if height[idx] > max_height:
            result += (height[idx] - max_height)

    print("#{} {}".format(T, result))