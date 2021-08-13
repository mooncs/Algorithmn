word = list('삼성청년소프트웨어아카데미')
n = len(word)  # 글자수
for i in range(n//2):
    word[i], word[n-1-i] = word[n-1-i], word[i]
print(''.join(word))

word2 = '삼성청년소프트웨어아카데미'
print(word2[::-1])

reverse = ''.join(reversed(word2))
print(reverse)
