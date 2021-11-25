def print_till_zero(n):
    print(n)
    if n == 1:
        return 1
    else:
        return print_till_zero(n - 1)


print_till_zero(10)
