def pertence(c, s):
    if s == '':
        return False
    if c == s[0]:
        return True
    return pertence(c, s[1:])
    
c = 's'
s = 'joao'
print(pertence(c,s))