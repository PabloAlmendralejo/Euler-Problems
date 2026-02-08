num = 20
while True:
    divisible = True
    for i in range(1, 21):
        if num % i != 0: 
            divisible = False
            break
    if divisible:
        break
    num += 20  
print(num)
