'''
문자가 연속으로 해서 나타나는 경우
문자열,구현문제
'''


n = int(input())

answer = 0

for _ in range(n):
    item = input()
    ex = ''
    tmp = []
    isGroup = True

    for ch in item:
        if ch in tmp and ex is not ch :
            isGroup = False
            break
        if ex is not ch:
            tmp.append(ch)
        ex = ch
    if isGroup:
        answer += 1

print(answer)
