from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    r,s = stdin.readline().split()
    answer = ''
    for ch in s:
        for _ in range(int(r)):
            answer += ch
    print(answer)

#문자열
