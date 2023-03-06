from sys import stdin

n = int(stdin.readline())

arr = sorted(list(map(int,stdin.readline().split())))

hap = int(stdin.readline())

i,j = 0,n-1
cnt = 0

while i != j:

    if arr[i] + arr[j] == hap:
        cnt += 1
        i += 1
    elif arr[i] + arr[j] > hap:
        j -= 1
    else :
        i += 1

print(cnt)
