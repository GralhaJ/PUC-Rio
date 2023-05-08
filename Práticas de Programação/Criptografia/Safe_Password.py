def Safe(s):
    n = len(s)
    numeros = '0123456789'
    a = 0
    b = 0
    c = 0
    if n >= 8:
        for i in range(n):
            if s[i] >= 'A' and s[i] <= 'Z':
                a = 1
            if s[i] >= 'a' and s[i] <= 'z':
                b = 1
            if s[i] in numeros:
                c = 1
    
    if a == b == c == 1:
        return True
    else:
        return False
        
s = input('Digite sua senha: ')
print(Safe(s))
                    
                        
                
            