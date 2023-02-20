#곱셈 관련 함수 
def mul(num):
    return eval('*'.join([str(i) for i in num]))
    
#유클리드 호제법
def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A

N=int(input())
Nnumbers = list(map(int,input().split()))
M=int(input())
Mnumbers = list(map(int,input().split()))

A=mul(Nnumbers)
B=mul(Mnumbers)

print('%s' %str(gcd(A,B))[-9:])
