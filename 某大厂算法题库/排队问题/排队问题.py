num = [2, 5, 3, 4, 1]
res = []

for index1, val1 in enumerate(num):
    sub2 = num[index1+1:]
    for index2, val2 in enumerate(sub2):
        last = sub2[index2+1:]
        for val3 in last:
            if val1 < val2 < val3 or val1 > val2 > val3:
                print(val1, val2, val3)
                res.append((val1, val2, val3))

print(res)
