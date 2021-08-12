N = 4
hamburger = ['순쇠고기패티', '양상추', '치즈', '양파']
# for i in range(16):
for i in range(1 << N):     # 위와 동일
    # print(i)
    # print(bin(i))
    for j in range(N):
        if i & (1<<j):
            # 여기에 걸렸다는 것은 해당 j번째 비트가 1이라는 뜻이고, 값이 존재한다는 뜻이다.
            print(hamburger[j], end=' ')
    print()

# print(5&3)    # & 1인지 확인