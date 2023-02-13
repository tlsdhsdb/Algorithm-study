from sys import stdin


def gcd(x,y):
    l = x if x > y else y #large
    s = y if x > y else x #small

    while s != 0:
        s,l = l % s,s

    return l


#최대공약수

n = int(stdin.readline())
arr_n = list(map(int,stdin.readline().split()))
a = 1

for n in arr_n:
    a *= n

m = int(stdin.readline())
arr_m = list(map(int,stdin.readline().split()))
b = 1

for n in arr_m:
    b *= n

answer = gcd(a,b)


length = len(str(answer))
if length >= 9:
    print(str(answer)[length-9:])
else :
    print(answer)
