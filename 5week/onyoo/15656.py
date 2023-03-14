'''
오름차순 수열
'''
from sys import stdin
n,m = map(int,stdin.readline().split())
lst = sorted(list(map(int,stdin.readline().split())))
arr = []
def DFS(start):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start,len(lst)):
        if lst[i] in arr :
            continue
        arr.append(lst[i])
        DFS(i+1)
        arr.pop()

DFS(0)
