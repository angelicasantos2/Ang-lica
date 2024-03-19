#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

def vetor_numeros_inteiros(n):
    vetor = []

    for i in range(5):
        numero = int(input('Digite o número inteiro'))
        vetor.append(numero)
    
    return vetor
vetor = vetor_numeros_inteiros(5)
print(vetor)