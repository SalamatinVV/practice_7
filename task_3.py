def degree(b, n):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0
    if n == 0:
        return 1
    if even(n):
        return degree(b, n/2)**2
    return b*degree(b, n-1)


print(degree(2, 10))
