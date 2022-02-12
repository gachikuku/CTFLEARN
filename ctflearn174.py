with open("data.dat") as f:
    total = 0
    lines = f.readlines()
    for i in lines:
        zeroes = 0
        ones = 0
        for j in list(i[0:-1]):
            if j == '0':
                zeroes += 1
            elif j == '1':
                ones += 1
        if zeroes%3 == 0 or ones%2 == 0:
            total += 1
    print(total)
