numero = int(input('Que número você quer? '))

if numero <= 0:
    print('O número deve ser maior que zero!')
    exit()

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
