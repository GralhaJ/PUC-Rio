def imprime_string_vertical_invertida(s):
    if len(s) == 1:
        print(s)
        return
    print(s[-1])
    return imprime_string_vertical_invertida(s[:-1])

imprime_string_vertical_invertida('abcdef')