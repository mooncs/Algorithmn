# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i					# 0번째 원소
#     for j in range(2):
#         bit[1] = j				# 1번째 원소
#         for k in range(2):
#             bit[2] = k			# 2번째 원소
#             for l in range(2):
#                 bit[3] = l		# 3번째 원소
#                 print(bit)		# 생성된 부분집합 출력

N, K = map(int, input().split())
A = [1, 2, 3, 4, 5]
cnt = 0
for i in range(1<<len(A)):      # 부분집합의 수, 0~2ⁿ 2ⁿ개 각각의 부분집합
    # print(i)
    subset = []
    for j in range(len(A)):     # 어떤 원소를 가진 부분집합인지 확인하기 위해서 반복문 실행
        if i & (1<<j):
            subset.append(A[j])
    # print(subset)
    if len(subset) == N and sum(subset) == K:
        cnt += 1
print(cnt)

'''
예를 들어, 
j가 26이면 011010
-----------------------------
1<<0    : 000001
          000000 -> 해당 없음
i<<1    : 000010
          000010 -> 2를 부분집합의 원소로 가진다.
1<<2    : 000100
          000000 -> 해당 없음
i<<3    : 000010
          001000 -> 4를 부분집합의 원소로 가진다.
1<<4    : 010000
          010000 -> 5를 부분집합의 원소로 가진다.
=> subset = [2, 4, 5]
'''