# # 1
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     num = list(map(int, input().split()))
#
#     for i in range(len(num)):
#         for j in range(i, len(num)):
#             if num[i] > num[j]:
#                 num[i], num[j] = num[j], num[i]
#
#     print('#{0} {1}'.format(tc, (num[-1] - num[0])))

# 2
def MyMax(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


def MyMin(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num


T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(tc + 1, MyMax(nums) - MyMin(nums)))