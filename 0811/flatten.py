# user_input = []
# temp_input = []
# for tc in range(20):
#     if tc % 2:
#         temp_input.append(list(map(int, input().split())))
#         user_input.append(temp_input)
#         temp_input = []
#     else:
#         temp_input.append(int(input()))
# # 최대값 찾기
# def my_max(arr):
#     maxi = arr[0]
#     for i in arr:
#         if i > maxi:
#             maxi = i
#     return maxi
# # 최소값 찾기
# def my_min(arr):
#     mini = arr[0]
#     for i in arr:
#         if i < mini:
#             mini = i
#     return mini
#
# def dump(D, arr):
#     maxi = my_max(arr)
#     mini = my_min(arr)
#     if D < 1:
#         return maxi - mini
#     else:
#         arr[arr.index(maxi)] -= 1
#         arr[arr.index(mini)] += 1
#         D -= 1
#         return dump(D, arr)
#
# result = []
# for case in user_input:
#     dum = dump(case[0], case[1])
#     result.append(dum)
#
# for i in range(len(result)):
#     print('#{} {}'.format(i + 1, result[i]))

# 2
for test_case in range(1, 11):  # 테스트 케이스
    N = int(input())  # 덤프의 수
    nums = list(map(int, input().split()))  # 입력받을 리스트

    for _ in range(N):  # N번만큼 실행
        for i in range(len(nums) - 1, 0, -1):  # 버블정렬로 오름차순 정렬
            for j in range(0, i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        nums[-1] = (nums[-1] - 1)  # 정렬된 상태에서 마지막 값 -1, 처음 값 +1
        nums[0] = (nums[0] + 1)    # N번만큼 반복하면 마지막 값과 처음 값은 빠져있는 상태

    for i in range(len(nums) - 1, 0, -1):  # 버블 정렬로 한 번 더 정렬 이번이 진짜 오름차순
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    result = nums[-1] - nums[0]  # 마지막 값 == 제일 큰 값에서 처음 값 == 제일 작은 값
    print("#{} {}".format(test_case, result))
About