'''
같은 수를 여러 번 골라도 된다
'''
from sys import stdin

n,m = map(int,stdin.readline().split())
arr = []
def DFS():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1,n+1):
        arr.append(i)
        DFS()
        arr.pop()

DFS()
