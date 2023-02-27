n = int(input())
jum = list(map(int,input().split()))
max = max(jum)

result = []
for i in jum:
    result.append(i / max * 100)
print(sum(result)/n)
