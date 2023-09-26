def imprime_string_vertical(s):
    if len(s) == 1:
        print(s)
        return
    print(s[0])
    return imprime_string_vertical(s[1:])

imprime_string_vertical('carol')