# Ordenação manual de três números inteiros

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

mediana = (n1 + n2 + n3) - maior - menor

print(f"O maior número é: {maior}")
print(f"A mediana é: {mediana}")
print(f"O menor número é: {menor}")