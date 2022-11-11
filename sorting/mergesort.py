def merge(x: list, y: list):
    result = []

    l_idx, r_idx = 0,0

    while(l_idx < len(x) and r_idx < len(y)):
        if(x[l_idx] < y[r_idx]):
            result.append(x[l_idx])
            l_idx += 1
        else:
            result.append(y[r_idx])
            r_idx += 1

    if(x):
        result.extend(x[l_idx:])

    if(y):
        result.extend(y[r_idx:])

    return result

def sort(m: list):
    """
    :type m: object
    """
    if(len(m) <= 1):
        return m

    middle = len(m)//2

    left = m[:middle]
    right = m[middle:]

    left = sort(left)
    right = sort(right)

    return merge(left, right)


a = [25, 3, 1, 15, 12, 27]
b = [1718, 90, 7, 5, 2, 33]

print(a)
print(sort(a))

print(b)
print(sort(b))

