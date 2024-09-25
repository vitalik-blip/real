num1 = int(input('Введите сумму вклада: '))
num2 = float(input('Введите процент: '))
num3 = int(input('Введите сумму цели: '))
num4 = num1 + num2 + num3
i = 0
print(round(num4, 0))
while num1 < num3:
    num1 *= 1 + num2 / 100
    num1 = int(100 * num1) / 100
    i += 1
    print(f'Понадобится {i} лет.')