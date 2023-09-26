def qntd_caracteres(s):
    if s == '':
        return 0
    return 1 + qntd_caracteres(s[1:])

print(qntd_caracteres('joaogabriel'))