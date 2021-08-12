

# # input() 문자열 한줄 통으로 입력이 된다.
# a = input()
# print(a, type(a))

# # 정수 한개를 입력받고 싶다.
# T = int(input())
# # 문제에서 첫줄에는 항상 test_case개수가 주어지고
# # 출력으로는 #tc_num ans
# for tc in range(1, T+1):
#     ans = 0
#     print("#{} {}".format(tc, ans))

# # 정수를 여러개 입력 받는 방법
# a, b, c, d, e = map(int, input().split())
# a = list(map(int, input().split()))

# # 한줄짜리 문자열을 리스트로 바꾸고 싶을 때
# # abcde
# a = list(input())
# b = [input()]   # 굳이 할 필요가 없는 처리
# print(a, b)

# # a b c d e
# a = input().split()
# b = list(input().split())   # 2차원이 아니라 a와 동일한 처리이기 때문에 굳이...?
# print(a, b)

# 123456789 입력 원소 하나씩 정수로 리스트
a = list(map(int, input()))
print(a)
