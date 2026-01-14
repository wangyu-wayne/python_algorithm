def integer_break(n):
    key_map = {1: 1, 2: 1, 3: 2, 4: 4}
    if n in key_map:
        return key_map.get(n)

    # n>5
    tmp = n % 3
    r = 0
    if tmp == 1:
        k = (n - 4) // 3
        tmp = 4
    elif tmp == 2:
        k = (n - 2) // 3
    else:
        k = n // 3
        tmp = 1
    return pow(3, k) * tmp


print(integer_break(10))
