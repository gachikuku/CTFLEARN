from luhn import *
card = 5432100000001234
while card:
    nums = [int(d) for d in str(card)]
    if card%123457==0 and verify(str(card))==True and nums[-4:]==[1,2,3,4]:
        print(card)
        break
    else:
        card += 10000
