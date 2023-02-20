'''
문자열 문제를 가장한 딕셔너리 문제
'''


n = int(input())

dic = {}

for _ in range(n):
    word = input()
    if len(word) not in dic:
        dic[len(word)] = [word]
    else:
        dic[len(word)].append(word)

for item in sorted(dic.items()):
    lst = sorted(set(item[1]))
    for val in lst :
        print(val)

