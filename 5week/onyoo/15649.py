def DFS():
    # 스택의 길이가 M이면 퇴각
    if len(s) == M:
        print(*s)
        return

    for i in range(1, N + 1):
        if i in s:
            # 1,1 2,2 3,3 4,4 등의 경우의 수를 방지함
            continue
        s.append(i)
        DFS()  # 함수 다시 호출
        # 길이를 충족하면
        s.pop()  # 원상복귀


N, M = map(int, input().split())
s = []  # 출력 수열 넣을 stack
DFS()
