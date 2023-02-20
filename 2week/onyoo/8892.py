'''
팰린드롬
어느방향으로 읽어도 항상 같은 방법으로 읽을 수 있는 단어
aaba 1121
ba 21
ababa 12121
bbaa 2211
baaba 21121
'''

def panlindrom(lst):
    length = len(lst)
    #인덱스가 다르면, 다른 단어임!!
    for i in range(length):
        for j in range(length):
            if i == j :
                continue
            else:
                word = lst[i] + lst[j]
                if word == word[::-1]:
                    return word
    return 0

t = int(input())

for _ in range(t):
    k = int(input())
    arr = [input() for _ in range(k)]
    answer = panlindrom(arr)

    if answer == 0:
        print(0)
    else:
        print(answer)
