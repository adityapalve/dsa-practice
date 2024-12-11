seq = list(input()) 

def max_count(seq):
    if not seq:
        return 0

    curr_count = 1
    max_count = 1

    for i in range(1, len(seq)):
        if seq[i-1] == seq[i]:
            curr_count += 1
        else:
            max_count = max(max_count, curr_count)
            curr_count = 1

    max_count = max(max_count, curr_count)
    return max_count

print(max_count(seq))