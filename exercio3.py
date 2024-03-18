exercio3

notas = []
n = 4
media = 0

for i in range(n):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    notas.append(nota)
    media += nota / n

print(f'\nAs notas são: {notas}')
print(f'A média das notas é: {media}\n')