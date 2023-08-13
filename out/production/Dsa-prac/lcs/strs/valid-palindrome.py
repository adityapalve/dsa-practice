def validpalidrome(s):
    s = s.lower()
    i , j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


input = "A man, a plan, a canal: Panama"
print(validpalidrome(input))