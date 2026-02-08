maxi = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1): 
        num = i * j
        if num <= maxi:
            break
        if str(num) == str(num)[::-1]:
            maxi = num
print(maxi)
