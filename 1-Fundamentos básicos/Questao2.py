# Calculadora de operações aritméticas fundamentais

def formata_numero(num, parenteses=False):
    if num == int(num):
        numero = str(int(num))
    else:
        numero = f"{num:.2f}".replace(".", ",")

    if parenteses and num < 0:
        return f"({numero})"

    return numero

def adicao(num1, num2):
    soma = num1 + num2

    print(f"{formata_numero(num1)} + {formata_numero(num2, True)} = {formata_numero(soma)}")

def subtracao(num1, num2):
    sub = num1 - num2

    print(f"{formata_numero(num1)} - {formata_numero(num2, True)} = {formata_numero(sub)}")

def multiplicacao(num1, num2):
    produto = num1 * num2

    print(f"{formata_numero(num1)} × {formata_numero(num2, True)} = {formata_numero(produto)}")

def divisao(num1, num2):
    if num2 == 0:
        print(f"{formata_numero(num1)} ÷ {formata_numero(num2, True)} = Divisão por zero não permitida")
    else:
        div = num1 / num2
        print(f"{formata_numero(num1)} ÷ {formata_numero(num2, True)} = {formata_numero(div)}")

def divInteira(num1, num2):
    if num2 == 0:
        print(f"{formata_numero(num1)} // {formata_numero(num2, True)} = Divisão por zero não permitida")
    else:
        dInt = num1 // num2
        print(f"{formata_numero(num1)} // {formata_numero(num2, True)} = {formata_numero(dInt)}")

def restoDiv(num1, num2):
    if num2 == 0:
        print(f"{formata_numero(num1)} % {formata_numero(num2, True)} = Divisão por zero não permitida")
    else:
        rDiv = num1 % num2
        print(f"{formata_numero(num1)} % {formata_numero(num2, True)} = {formata_numero(rDiv)}")

def potenciacao(num1, num2):
    pot = num1 ** num2

    sobrescritos = {"0": "⁰","1": "¹","2": "²","3": "³","4": "⁴",
    "5": "⁵","6": "⁶","7": "⁷","8": "⁸","9": "⁹","-": "⁻",",": "˙"
    }

    expoente = formata_numero(num2)
    formatado = "".join(sobrescritos[digit] for digit in expoente)

    print(f"{formata_numero(num1)}{formatado} = {formata_numero(pot)}")

num1 = float(input("Digite o primeiro número: ").replace(",", "."))

num2 = float(input("Digite o segundo número: ").replace(",", "."))

adicao(num1, num2)
subtracao(num1, num2)
multiplicacao(num1, num2)
divisao(num1, num2)
divInteira(num1, num2)
restoDiv(num1, num2)
potenciacao(num1, num2)
