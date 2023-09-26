def duplica_caracteres(s):
    if len(s) == 1:
        return s+s
    return 2*s[0] + duplica_caracteres(s[1:])

print(duplica_caracteres('mesa'))