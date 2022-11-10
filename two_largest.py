def twomax(ls: list, left, right):
    max1 = ls[left]
    max2 = ls[left]

    if left == right:
        return None

    if right - left == 1:
        if ls[right] >= ls[left]:
            max1 = ls[right]
            max2 = ls[left]
        else:
            max1 = ls[left]
            max2 = ls[right]
        return max1, max2

    m = (left + right) // 2

    l = twomax(ls, left, m)
    r = twomax(ls, m, right)

    if r[0] >= l[0]:
        max1 = r[0]
        if r[1] >= l[0]:
            max2 = r[1]
        else:
            max2 = l[0]
    else:
        max1 = l[0]
        if l[1] <= r[0]:
            max2 = l[1]
        else:
            max2 = r[0]

    return max1, max2


print(twomax([1, 5, 2, 4, 3], 0, 4))
print(twomax([1, 100, 2, 4, 3], 0, 4))
print(twomax([34, 20, 23, 4, 900], 0, 4))
