num1 = [1, 8, 9]
num2 = [2, 1]
res = []

carry = 0
i = -1
lens1 = len(num1)
lens2 = len(num2)

min_index = min(lens1, lens2) * -1

while i >= min_index:
    val = num1[i] + num2[i] + carry
    if val >= 10:
        carry = 1
        res.insert(0, val - 10)
    else:
        carry = 0
        res.insert(0, val)
    i -= 1

if lens1 != lens2:
    if lens1 > lens2:
        last = num1
        min_index = lens1 * -1
    else:
        last = num2
        min_index = lens2 * -1

    while i >= min_index:
        val = last[i] + carry
        if val >= 10:
            carry = 1
            res.insert(0, val-10)
        else:
            carry = 0
            res.insert(0, val)
        i -= 1

if carry:
    res.insert(0, carry)

print(res)
