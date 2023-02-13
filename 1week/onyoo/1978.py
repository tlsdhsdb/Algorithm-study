#주어진 N개의 중에서 소수가 몇개인지 찾아서 출력
#N은 100이하

def isPrime(num):
    if num == 1 :
        #1은 소수가 아니에요
        return False
    for i in range(2,int(num*0.5)+1):
        if num % i == 0:
            return False
    return True



from sys import stdin

n = int(stdin.readline())
answer = 0

num = list(map(int,stdin.readline().split()))
for i in num:
    if isPrime(i):
        answer += 1

print(answer)
