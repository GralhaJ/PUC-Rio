def elimina(i, a):
    if i == a:
        return 0
    if i % 10 == a:
        return i // 10, elimina(i//10, a)
    return i, elimina(i//10, a)
  
    
print(elimina(123,1))