# Cadastro e apresentação de perfil pessoal

nome = input("Digite seu nome completo:")

while True:
    idade = input("Digite sua idade: ")
    try:
        idade = int(idade)

        if idade > 0:
            break
        else:
            print("Valor digitado inválido.")
    except ValueError:
        print("Valor digitado inválido.")

while True:
    altura = input("Digite sua altura: ")
    try:
        altura = float(altura.replace(",", "."))

        if altura > 0:
            break
        else:
            print("Valor digitado inválido.")
    except ValueError:
        print("Valor digitado inválido.")

cidade = input("Digite a cidade de residência:")

print(f"|Nome:{nome}\n|Idade: {idade}\n|Altura: {altura}\n|Cidade:{cidade}")