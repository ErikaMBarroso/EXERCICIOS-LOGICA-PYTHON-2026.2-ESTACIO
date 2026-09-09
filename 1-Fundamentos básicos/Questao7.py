# Análise simultânea de sinal e paridade

numero = int(input("digite um número: "))

if numero == 0:
    print("O número é nulo")
elif numero > 0:
    if numero % 2 == 0:
        print("O número é positivo e par")
    else:
        print("O número é positivo e ímpar")
elif numero < 0:
    if numero % 2 == 0:
        print("O número é negativo e par")
    else:
        print("O número é negativo e ímpar")