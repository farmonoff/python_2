count = int()

for i in range(3,100):
    if i % 10 == 3 or i // 10 == 3:
        count += 1
        print(i, end = ' ')
print()        
print(count, 'ta 3 soni mavjud' )