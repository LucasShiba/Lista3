numero_alunos = int(input('Qual o número de alunos? '))
soma = 0
for i in range(numero_alunos):
    soma += float(input(f'Qual a nota do aluno {i + 1}? '))

print(f'A média é {soma / numero_alunos:.2f}')
