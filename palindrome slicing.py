x = []
for num in range(100,1000):
    if str(num) == str(num)[::-1]:
        x.append(num)

middle = len(x) // 2
middle5 = x[middle-2 : middle+3]

print(middle5)




