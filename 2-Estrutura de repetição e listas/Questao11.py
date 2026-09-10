# Relatório analítico de lista numérica
# Relatório analítico de lista 

def verificaParidade(numeros):
    pares = []
    impares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("======================")
    print("=========PARES========")
    print(pares)
    print("========IMPARES=======")
    print(impares)
    print("======================")

def somaMedia(numeros):
    soma = 0

    for n in numeros:
        soma = soma + n

        media = soma / len(numeros)

    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")

def maiorMenor(numeros):
    maior = numeros[0]
    menor = numeros[0]

    for n in numeros:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    print(f"Maior: {maior}")
    print(f"Menor: {menor}")


numeros = []

for n in range(1,11):
    numero = int(input(f"Digite o {n}° número: "))
    numeros.append(numero)

print(numeros)
verificaParidade(numeros)
somaMedia(numeros)
maiorMenor(numeros)