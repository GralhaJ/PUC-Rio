def imprime_vertical(n):
    if n < 10:
        print(n)
        return
    imprime_vertical(n//10)
    imprime_vertical(n%10)
    
    
imprime_vertical(1234)