from sys import stdin
from collections import deque

n,k = map(int,stdin.readline().split())

que = deque([i+1 for i in range(n)])
arr = []
cnt = 0

while que:
    cnt += 1
    if cnt % k == 0 :
        arr.append(que.popleft())
    else:
        que.append(que.popleft())


answer = '<' + ', '.join(str(i) for i in arr) + '>'
print(answer)
