# 일반적인 print를 확인하여 중간중간 결과 확인
def my_print(idx, N):
    print("#{}까지의 합은 {}이다.".format(idx, N))

def my_sum(N):
    tmp = 0

    for i in range(N):
        tmp += i
        my_print(i, tmp)

    return tmp

ans = my_sum(10)

print(ans)
# 디버거를 사용할 때
# 1. 어디에 breakpoint를 찍어야하는지
# 2. step over는 무엇?
# 3. step into는 무엇?
# 4. step out은 무엇?
# 내가 원하는 곳부터 시작 가능
# 중간중간 내가 보고 싶은 변수를 이용해 결과를 볼 수 있다.