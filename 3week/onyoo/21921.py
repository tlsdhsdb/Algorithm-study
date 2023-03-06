from sys import stdin

n,x = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))

#window = x

hap = [sum(lst[:x])]

for i in range(0,n-x):
    hap.append(hap[i]-lst[i]+lst[i+x])


max_hap = max(hap)

if max_hap == 0:
    print("SAD")
else:
    print(max_hap)
    print(hap.count(max_hap))


