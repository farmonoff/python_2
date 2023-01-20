n, summa = int(input('n = ')), 0

for i in range(1, n + 1):
    print(' '*(n - i), '@ ' * i)
    summa += i

print(summa)