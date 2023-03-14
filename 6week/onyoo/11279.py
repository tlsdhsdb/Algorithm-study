from sys import stdin
import heapq

n = int(stdin.readline())

pq = []

for _ in range(n):
    x = int(stdin.readline())
    heapq.heappush(pq,(-1) * x)
    if x == 0:
        print(heapq.heappop(pq) * (-1))
