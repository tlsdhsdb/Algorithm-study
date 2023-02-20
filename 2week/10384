'''
문자열 : 팬그램,모든 알파벳을 적어도 한번씩 사용한 영어문장
더블 팬그램 -> 모든 알파벳을 적어도 두번씩 사용한 문장
'''

n = int(input())

for i in range(1,n+1):
    sentence = input()
    dic = {}
    for s in sentence:
        alpha = s.lower()
        if not s.isalpha():
            continue
        if alpha not in dic:
            dic[alpha] = 1
        else :
            dic[alpha] += 1
    if len(dic.keys()) >= 26:
        mini = min(list(dic.values()))
        if mini == 1:
            print(f'Case {i}: Pangram!')
        elif mini == 2:
            print(f'Case {i}: Double pangram!!')
        elif mini == 3:
            print(f'Case {i}: Triple pangram!!!')
    else:
        print(f'Case {i}: Not a pangram')
