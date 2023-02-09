from sys import stdin

t = int(stdin.readline())
MAX = 1000000
def primeList(n):
    che = [False, False] + [True] * n
    end = int(n**0.5) # 최대 약수가 제곱근 이하이기 때문

    for i in range(2,end+1):
        if che[i] == True:
            for j in range(i+i,n,i):
                che[j] = False

    # 소수면 true값을 가지는 리스트
    return che

che = primeList(MAX)

for _ in range(t):
    n = int(stdin.readline())
    prime = []
    answer = 0

    for i in range(2,n+1):
        if che[i] == True:
            prime.append(i)

    start = 0
    end = len(prime)-1
    #투포인터
    while start <= end :
        hap = prime[start] + prime[end]
        if hap < n:
            start += 1
        elif hap > n :
            end -= 1
        else :
           answer +=1
           start += 1
           end -= 1

    print(answer)

#pypy에서만 돌아감
#loop 최적화 할 필요가 있다
#이분탐색의 시간복잡도 O(logN)
#투포인터의 시간복잡도 O(N)
