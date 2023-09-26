def qntd_caractere(c, s):
    if s == '':
        return False
    if c == s[0]:
        return 1 + qntd_caractere(c, s[1:])
    return qntd_caractere(c, s[1:])

c = 'c'
s = 'aaabbc'
print(qntd_caractere(c, s))