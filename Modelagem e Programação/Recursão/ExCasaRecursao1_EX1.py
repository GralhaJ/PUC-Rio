def produto(x, y):
    if x == 0 or y == 0:
        return 0
    return x + produto(x, y-1)

print(produto(5,3))

