def itoa(number):
    change = []
    while number:
        remainder = number % 10
        change.append(chr(remainder+48))
        number //= 10
    for i in range(len(change)//2):
        change[i], change[len(change)-1-i] = change[len(change)-1-i], change[i]
    return ''.join(change)

def atoi(word):
    change = 0
    N = len(word)
    for i in range(N):
        change += (ord(word[i])-48)*10**(N-1-i)
    return change

print(itoa(1234))
print(type(itoa(1234)))
print(atoi('1234'))
print(type(atoi('1234')))