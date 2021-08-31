numero_alunos = int(input('Qual o número de alunos? '))
soma = 0
maior = 0
for i in range(numero_alunos):
    nota = float(input(f'Qual a nota do aluno {i + 1}? '))
    soma += nota
    if nota > maior:
        maior = nota

print(f'A média é {soma / numero_alunos:.2f}. A maior nota é {maior}')
