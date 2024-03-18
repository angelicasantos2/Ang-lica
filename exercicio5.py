exercicio5

n = 20
numeros = []
pares = []
impares = []

for i in range(n):
    numero = int(input(f'Digite o {i + 1}° número inteiro: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'\nNumeros: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}\n')