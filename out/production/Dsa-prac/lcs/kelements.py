# the top K frequence elements in a list
def topK(l, k):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]

