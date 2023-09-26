def digitos(n):
    if n < 10:
        return n
    return 1 + digitos(n//10)

print(digitos(123))