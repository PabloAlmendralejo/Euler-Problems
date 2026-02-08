N = 600851475143
factor = 2
while factor * factor <= N:
    if N % factor == 0:
        N //= factor
    else:
        factor += 1 if factor == 2 else 2  
print(N)