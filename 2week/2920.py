'''
차례대로 연주 ?
'''

from sys import stdin

lst = list(map(int,stdin.readline().split()))

answer = ""

if lst[0] == 1 :
    answer = 'ascending'
    num = 1
    for i in lst:
        if i != num:
            answer = 'mixed'
            break
        num += 1

elif lst[0] == 8:
    answer = 'descending'
    num  = 8
    for i in lst:
        if i != num :
            answer = 'mixed'
            break
        num -= 1
else :
    answer = 'mixed'

print(answer)
