#  Sistema interativo com menu de opções

def cadastrarNumeros():
    numero = int(input("\nDigite o número a ser cadastrado: "))

    return numero

def listarNumeros(listaNumeros):
    if len(listaNumeros) == 0:
        print("Nenhum número cadastrado")
    else:
        print(listaNumeros)

def exibeMaior(listaNumeros):
    if len(listaNumeros) == 0:
        print("Nenhum número cadastrado")
    else:
        maior = listaNumeros[0]

        for n in listaNumeros:
            if n > maior:
                maior = n

        print(f"Maior número: {maior}")

def exibeMenor(listaNumeros):
    if len(listaNumeros) == 0:
        print("Nenhum número cadastrado")
    else:
        menor = listaNumeros[0]

        for n in listaNumeros:
            if n < menor:
                menor = n

        print(f"Menor número: {menor}")

def calculaMedia(listaNumeros):
    if len(listaNumeros) == 0:
        print("Nenhum número cadastrado")
    else:
        soma = 0

        for n in listaNumeros:
            soma = soma + n

        media = soma / len(listaNumeros)

        print(f"Média: {media:.2f}")

listaNumeros = []

while True:
    print("========== GERENCIAMENTO DE NÚMEROS ==========")

    opcao = int(
        input(
            "1 - Cadastrar número\n"
            "2 - Listar números\n"
            "3 - Exibir maior número\n"
            "4 - Exibir menor número\n"
            "5 - Calcular média\n"
            "0 - Encerrar programa\n"
        )
    )

    match opcao:
        case 1:
            listaNumeros.append(cadastrarNumeros())
        case 2:
            listarNumeros(listaNumeros)
        case 3:
            exibeMaior(listaNumeros)
        case 4:
            exibeMenor(listaNumeros)
        case 5:
            calculaMedia(listaNumeros)
        case 0:
            break
        case _:
            print("Opção inválida")
