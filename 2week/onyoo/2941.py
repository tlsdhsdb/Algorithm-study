#문자열 문제
#replcae를 잘 활용해보자

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']


value = input()


for i in alpha:
    value = value
    value = value.replace(i,'*')

print(len(value))
