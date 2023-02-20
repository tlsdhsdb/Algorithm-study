n=int(input())
m=int(input())


k=m-n #각 과일별로 최소 1개씩은 훔친다
p=1
q=1
r=1

for i in range(1,n+k):
  p*=i

for j in range(1,n):
  q*=j 

for k in range(1,k+1):
  r*=k

result=p/(q*r)
print(int(result))
