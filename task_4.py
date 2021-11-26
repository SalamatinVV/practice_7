def max_in(list):
    k = 0
    for i in list:
        if i >= k:
            k = i
    return k


a = [123, 13, 21, 12341, 4255, 67432, 1, 45]
print(max_in(a))
