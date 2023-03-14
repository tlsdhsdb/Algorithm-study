'''
N개의 자연수는 모두 다른 수
'''
import sys
from sys import stdin

sys.setrecursionlimit(100000)

n,m = map(int,stdin.readline().split())
lst = sorted(list(map(int,stdin.readline().split())))
arr = []
def DFS():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(len(lst)):
        if lst[i] in arr:
            continue
        arr.append(lst[i])
        DFS()
        arr.pop()


DFS()


