n=int(input())
dic={}
for i in range(n):
    a=input()
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1
booklist=[]
num=max(dic.values())

for i in dic:
    if num==dic[i]:
        booklist.append(i)

booklist.sort()
print(booklist[0])
