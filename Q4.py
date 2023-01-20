for num  in range(2, 100):
    if num % 2 and num % 3 and num % 5 and num % 7:
        num = int(str(num)[::-1])
        if num % 2 and num % 3 and num % 5 and num % 7:
            print(f'{str(num)[::-1]} <- - -> {num}')

