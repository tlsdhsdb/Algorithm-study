'''
배열 합치기
'''
from sys import stdin


n,m = map(int,stdin.readline().split())

arr1 = list(map(int,stdin.readline().split()))
arr2 = list(map(int,stdin.readline().split()))

answer = sorted(arr1+arr2)

print(*answer)


