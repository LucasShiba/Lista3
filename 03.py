numero = 0
while numero > 10 or numero <= 0:
    numero = int(input('Que número você quer? '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
