# Geração de tabuada de multiplicação

numero = int(input("Digite um número: "))

for n in range(1,11):
    produto = n * numero
    print(f"{numero} x {n} = {produto}")