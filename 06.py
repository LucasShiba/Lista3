numeros = []
novo_calculo = True
while novo_calculo:
    for i in range(2):
        numero = -1
        while numero < 0 or numero > 10:
            numero = int(input((f'Digite o {i + 1}° número: ')))
        numeros.append(numero)

    print(f'Média: {sum(numeros) / 2}')
    dec = input('Deseja fazer um novo cálculo? (s/N) ')
    novo_calculo = dec == 's'
 