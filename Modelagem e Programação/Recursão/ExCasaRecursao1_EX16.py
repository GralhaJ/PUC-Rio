def sucessores(n):
    i = n % 10
    if i == 9:
        return 0
    return sucessores(n//10), i + 1
    

print(sucessores(12345))
    