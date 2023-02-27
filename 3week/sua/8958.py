N = int(input())
for _ in range(N):
    A=list(map(str,input()))
    sum = 0 
    score = 0 
    for i in range (len(A)):
        if A[i]  == 'O':
            sum = sum + 1
            score += sum
        else : 
            sum = 0
    print(score)
