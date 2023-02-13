'''
백준 4948
베르트랑 공준

임의의 자연수 n에 대하여, n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다
예) 10 < x <= 20

'''

def isPrime(n,m):
    lst = [False,False] + [True] * (m)
    for i in range(2,int(m**0.5)+1):
        if lst[i]:
            for j in range(i+i,m+1,i):
                lst[j] = False
    return [i for i in range(n+1,m+1) if lst[i] == True]

from sys import stdin

while True:
    x = int(stdin.readline())

    if x == 0:
        break

    y = x * 2

    lst = isPrime(x,y)
    print(len(lst))
