def sort(m: list, lo: int, hi: int):
    if(lo < hi):
        p = partition(m, lo, hi)
        
        sort(m, lo, p-1)
        sort(m, p+1, hi)
#    return m

def partition(x: list,lo:int,hi:int):
    pivot = x[hi]
    i = lo-1

    for j in range(lo,hi):
        if(x[j] < pivot):
            i += 1
            x[j], x[i] = x[i],x[j]

    i += 1
    x[i],x[hi] = x[hi],x[i]

    return i

a = [3,13,5,234,55,2]
print(a)
#print(sort(a,0,5))
sort(a,0,5)
print(a)
b = [3,12,2,6]
print(b)
sort(b,0,3)
print(b)
#print(sort(b,0,3))
