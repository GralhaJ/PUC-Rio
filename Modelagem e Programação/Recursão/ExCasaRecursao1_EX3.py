def aparece(n):
    if n < 10:
        if n == 3 or n == 4:
            return 1
        return 0
    if n % 10 == 3 or n % 10 == 4:
        return 1 + aparece(n//10)
    return aparece(n//10)

print(aparece(23424))
