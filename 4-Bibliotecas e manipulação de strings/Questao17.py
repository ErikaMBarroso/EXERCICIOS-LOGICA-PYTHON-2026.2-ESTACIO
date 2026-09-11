# Cálculos matemáticos com o módulo math

import math

try:
    print("\n")
    numero = float(input("Digite um número: "))
    print("===============================")
        
    if numero >= 0:
        raiz_quadrada = math.sqrt(numero)
        print(f"Raiz quadrada: {raiz_quadrada:.2f}")
    else:
        print("Raiz quadrada: Não existe raiz quadrada para negativos")
    
    print(f"Módulo: {math.fabs(numero)}")

    print(f"Teto: {math.ceil(numero)}")

    print(f"Piso: {math.floor(numero)}")

    if numero >= 0 and numero.is_integer():
        numero_inteiro = int(numero)
        print(f"Fatorial de {numero_inteiro}: {math.factorial(numero_inteiro)}")
    else:
        print("Fatorial: Não aplicável (o número precisa ser inteiro e não negativo)")

    print("===============================")
        
except ValueError:
    print("Valor inválido")
