fibo1 = 1
fibo2 = 2
sum = 0
while fibo1 < 4000000:
    aux = fibo2
    fibo2 = fibo1 + fibo2
    fibo1 = aux
    if fibo2 % 2 == 0:
        sum+=fibo2

print(sum)
