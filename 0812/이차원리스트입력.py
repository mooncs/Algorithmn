N, M = map(int, input().split())

# # 1. 빈 리스트를 만들어 넣고 1차 리스트를 append
# arr = []
# for _ in range(N):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)

# for i in arr:
#     print(i)


# # 2. 행의 공간을 미리 확보해두고 해당 자리를 바꾼다.
# arr = [0]*N

# for i in range(N):
#     arr[i] = list(map(int, input().split()))


# # 3. 리스트 내포
# arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     print(*i)

# N*M크기의 0으로 가득찬 이차원 배열
arr = [[0]*M for _ in range(N)]