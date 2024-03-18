exercicio8

n = 5
idades = []
alturas = []

for i in range(n):
    idade = int(input(f'\nDigite a idade da {i + 1}ª pessoa: '))
    altura = float(input(f'Digite a altura da {i + 1}ª pessoa: '))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

print(f'\nIdades na ordem inversa: {idades}')
print(f'Alturas na ordem inversa: {alturas}\n')