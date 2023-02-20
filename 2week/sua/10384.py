testCase=int(input())
for _ in range(testCase):
    sentence=input().upper()
    alpha_list=[0]*26
    for i in sentence:
        if i.isalpha():
            alpha_list[ord(i)-65]+=1
    if min(alpha_list)>=3: print("Case %d: Triple pangram!!!"%(_+1))
    elif min(alpha_list)>=2: print("Case %d: Double pangram!!"%(_+1))
    elif min(alpha_list)>=1: print("Case %d: Pangram!"%(_+1))
    else :print("Case %d: Not a pangram"%(_+1))
