D,K = map(int,input().split())

rc = [0 for i in range(D)]
rc[0],rc[1] = 1,1

while(True):
    for i in range(2,D): #2부터 D-1까지
        rc[i] = rc[i-1]+rc[i-2]
    
    if rc[D-1] == K:
        print(rc[0],rc[1],sep="\n")
        break
    elif rc[D-1] > K:
        rc[0] += 1
        rc[1] = rc[0]  #B는 항상 A보다 커야 하기 때문에 B=A로 초기화
    else:
        rc[1] += 1
