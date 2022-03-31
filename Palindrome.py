def palindrome(st):
    i = 0
    j = len(st) - 1
    if i >= j:
        return 1
    if st[i] != st[j]:
        return 0
    return palindrome(st[i + 1 : j])
