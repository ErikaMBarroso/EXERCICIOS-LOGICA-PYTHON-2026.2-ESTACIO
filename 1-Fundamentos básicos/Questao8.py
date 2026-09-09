# Estatística descritiva de conjunto numérico

def verificarSinal(numeros):
    positivos = []
    negativos = []

    for n in numeros:
        if n > 0:
            positivos.append(n)
        elif n < 0:
            negativos.append(n)

    print(f"Positivos: {len(positivos)}")
    print(f"Negativos: {len(negativos)}")

def verificarParidade(numeros):
    pares = []
    impares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print(f"Pares: {len(pares)}")
    print(f"Ímpares: {len(impares)}")

numeros = []
soma = 0

for i in range(1,11):
    numero = int(input(f"Digite o {i}° número: "))
    numeros.append(numero)

for n in numeros:
    soma = soma + n

media = soma / len(numeros)
        
print(f"Soma: {soma}")
verificarSinal(numeros)
verificarParidade(numeros)
print(f"Média: {media}")