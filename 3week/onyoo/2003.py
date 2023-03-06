from sys import stdin


n,m = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))


left = 0
right = 1

answer = 0


while right <= n and left <= right:
    hap = sum(lst[left:right])
    if hap == m :
        answer += 1
        right  += 1
    elif hap < m :
        right += 1
    else :
        left += 1

print(answer)
