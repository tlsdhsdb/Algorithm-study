from itertools import combinations

testCase=int(input())

for _ in range(testCase):
    num=int(input())
    wlist=list(input() for i in range(num))
    comb=combinations(wlist, 2)
    
    for sa, sb in comb:
        add1= sa+sb
        add2= sb+sa
        if add1 == add1[::-1]:
            print(add1)
            break
        if add2==add2[::-1]:
            print(add2)
            break
    else:
        print(0)
