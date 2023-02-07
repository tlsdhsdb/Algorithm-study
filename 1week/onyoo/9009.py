from sys import stdin

n = int(stdin.readline())


for _ in range(n):
    num = int(stdin.readline())
    result = []
    fib = [0,1]
    k = 2
    while fib[k-1] <= num:
        fib.append(fib[k-1]+fib[k-2]) # 피보나치 수열
        k += 1
    k -= 1 # fib[k-1] 을 기준으로 비교하기 때문에 한 단계 뒤로 가야함
    # k-1을 비교하는 이유 ?
    # 지정된 수보다 작은 수 중 가장 큰 수를 구하기 위해서는 지정된 수를 넘는 그 사이를 알아야함
    # 지정된 수를 넘는 그 경계값 (하지만 지정된 수 보다 큰) 보다 하나 작은 수가 우리가 원하는 수이기 때문에 -1을 해주는 것이다

    while k > 0 and num > 0:
        if fib[k] <= num:
            result.append(fib[k])
            num -= fib[k]
        k -= 1

    for k in range(len(result),0,-1):
        print(result[k-1],end=' ')
    print()




