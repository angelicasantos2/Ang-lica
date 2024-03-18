exercicio10

n = 10
vetor_a = []
vetor_b = []
vetor_ab = []

for i in range(2):
    for j in range(n):
        elemento = input(f'\nDigite o {j + 1}º elemento do vetor {i + 1}: ')
        if i == 0:
            vetor_a.append(elemento)
        else:
            vetor_b.append(elemento)

for i in range(n):
    elemento_a = vetor_a[i]
    vetor_ab.append(elemento_a)
    elemento_b = vetor_b[i]
    vetor_ab.append(elemento_b)

print(f'\nVetor 1: {vetor_a}')
print(f'Vetor 2: {vetor_b}')
print(f'Vetor de elementos intercalados: {vetor_ab}\n')