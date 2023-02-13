#M 이상 N 이하의 소수를 모두 출력
#M,N <= 1,000,000

from sys import stdin

m,n = map(int,stdin.readline().split())

def isPrime(x,y):
    lst = [False,False] + [True] * (y)
    for i in range(2,int(y**0.5)+1):
        if lst[i]:
            for j in range(i+i,y+1,i):
                lst[j] = False
    return [i for i in range(x,y+1) if lst[i] == True]

lst = isPrime(m,n)

for item in lst:
    print(item)
