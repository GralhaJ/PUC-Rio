def imprime_vertical_invertido(n):
    if n < 10:
        print(n)
        return
    print(n % 10)
    imprime_vertical_invertido(n//10)

imprime_vertical_invertido(123)