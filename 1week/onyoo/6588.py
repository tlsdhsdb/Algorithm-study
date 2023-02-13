'''
6588 골드바흐의 추측
시간제한 0.5초

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
100만 이하의 모든 짝수에 대해서, 이 추측을 검증해야함

최소 NlogN 시간복잡도
'''
from sys import stdin

def isPrime(num):
    lst = [False,False] + [True] * (num-1)
    for i in range(2,int(num**0.5)+1):
        if lst[i]:
            for j in range(i+i,num,i):
                lst[j] = False

    return lst

MAX = 1000000

lst = isPrime(MAX)

while True:
    m = int(stdin.readline())

    if m == 0:
        break

    for i in range(2,len(lst)):
        if lst[i] and lst[m-i]:
            print(m,"=",i,"+",m-i)
            break
        elif i == m:
            print("Goldbach's conjecture is wrong.")
