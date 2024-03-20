#exercicio12

n = 30
idades = [10, 13, 12, 14, 15, 12, 10, 10, 12, 13, 10, 13, 12, 14, 15, 12, 10, 10, 12, 13, 10, 13, 12, 14, 15, 12, 10, 10, 12, 13]
alturas = [1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40, 1.30, 1.50, 1.40]
altura_media = 0
resposta = 0

for altura in alturas:
    altura_media += altura / n

for i in range(n):
    if idades[i] > 13 and alturas[i] < altura_media:
        resposta += 1

print(f'\nA quantidade de alunos com mais de 13 anos e altura inferios à média é de {resposta}.\n')