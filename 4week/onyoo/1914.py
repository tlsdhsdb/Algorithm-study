from sys import stdin

n = int(stdin.readline())

answer = []
def hanoi(n,from_pos,to_pos,aux_pos):
    if n == 1:
        answer.append([from_pos,to_pos])
        return
    hanoi(n-1,from_pos,aux_pos,to_pos)
    answer.append([from_pos,to_pos])
    hanoi(n-1,aux_pos,to_pos,from_pos)


print(2**n-1) #횟수는 무조건 2**n-1

if n <= 20:
    hanoi(n, 1, 3, 2)
    for i in answer:
        print(*i)
