# Sistema completo de gerenciamento acadêmico

import os

mediaAprovacao = 7.0
mediaRecuperacao = 5.0
numNotas = 3

def limparTela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def calcularMedia(notas):
    return sum(notas) / len(notas)


def calcularSituacao(media):
    if media >= mediaAprovacao:
        return "Aprovado"
    elif media >= mediaRecuperacao:
        return "Recuperação"
    else:
        return "Reprovado"


def criarEstudante(nome, idade, curso, notas):
    media = calcularMedia(notas)
    situacao = calcularSituacao(media)

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": tuple(notas),
        "media": media,
        "situacao": situacao
    }

    return estudante


def encontrarEstudante(estudantes, nome):
    for i in range(len(estudantes)):
        if estudantes[i]["nome"].lower() == nome.lower():
            return i

    return -1


def exibirEstudante(estudante):
    print("\n----------------------------------------")
    print(f"Nome: {estudante['nome']}")
    print(f"Idade: {estudante['idade']} anos")
    print(f"Curso: {estudante['curso']}")

    print("Notas: ", end="")

    for i, nota in enumerate(estudante["notas"], start=1):
        print(f"{nota:.1f}", end="")

        if i < len(estudante["notas"]):
            print(" | ", end="")

    print(f"\nMédia: {estudante['media']:.2f}")
    print(f"Situação: {estudante['situacao']}")
    print("----------------------------------------")


def lerNome():
    while True:
        nome = input("Nome: ").strip()

        if nome != "":
            return nome

        print("O nome não pode ficar vazio.")


def lerIdade():
    while True:
        try:
            idade = int(input("Idade: "))

            if idade > 0:
                return idade
            else:
                print("A idade deve ser um número inteiro positivo.")

        except ValueError:
            print("Digite uma idade válida.")


def lerCurso():
    while True:
        curso = input("Curso: ").strip()

        if curso != "":
            return curso

        print("O curso não pode ficar vazio.")


def lerNota(numero):
    while True:
        try:
            nota = float(input(f"Nota {numero} (0 a 10): "))

            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")


def lerNotas():
    notas = []

    for i in range(1, numNotas + 1):
        notas.append(lerNota(i))

    return notas


def cadastrarEstudante(estudantes):
    limparTela()

    print("========================================")
    print("       CADASTRO DE ESTUDANTE")
    print("========================================")

    nome = lerNome()

    if encontrarEstudante(estudantes, nome) != -1:
        print("\nJá existe um estudante cadastrado com esse nome.")
        pausar()
        return

    idade = lerIdade()
    curso = lerCurso()
    notas = lerNotas()

    estudante = criarEstudante(nome, idade, curso, notas)
    estudantes.append(estudante)

    print("\nEstudante cadastrado com sucesso!")

    pausar()


def listarEstudantes(estudantes):
    limparTela()

    print("========================================")
    print("         LISTA DE ESTUDANTES")
    print("========================================")

    if len(estudantes) == 0:
        print("\nNenhum estudante cadastrado")
        pausar()
        return

    for numero, estudante in enumerate(estudantes, start=1):
        print(f"\nESTUDANTE {numero}")
        exibirEstudante(estudante)

    pausar()


def consultarEstudante(estudantes):
    limparTela()

    print("========================================")
    print("         CONSULTAR ESTUDANTE")
    print("========================================")

    if len(estudantes) == 0:
        print("\nNenhum estudante cadastrado")
        pausar()
        return

    nome = input("\nDigite o nome do estudante: ").strip()

    indice = encontrarEstudante(estudantes, nome)

    if indice == -1:
        print("\nEstudante não encontrado.")
    else:
        print("\nEstudante encontrado:")
        exibirEstudante(estudantes[indice])

    pausar()


def alterarDados(estudantes):
    limparTela()

    print("========================================")
    print("           ALTERAR DADOS")
    print("========================================")

    if len(estudantes) == 0:
        print("\nNenhum estudante cadastrado")
        pausar()
        return

    nome = input("\nDigite o nome do estudante: ").strip()

    indice = encontrarEstudante(estudantes, nome)

    if indice == -1:
        print("\nEstudante não encontrado.")
        pausar()
        return

    estudante = estudantes[indice]

    print("\nDados atuais:")
    exibirEstudante(estudante)

    print("\nO que deseja alterar?")
    print("1 - Nome")
    print("2 - Idade")
    print("3 - Curso")
    print("4 - Notas")
    print("0 - Cancelar")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        novoNome = lerNome()

        outroIndice = encontrarEstudante(estudantes, novoNome)

        if outroIndice != -1 and outroIndice != indice:
            print("\nJá existe outro estudante com esse nome.")
        else:
            estudante["nome"] = novoNome
            print("\nNome alterado com sucesso.")

    elif opcao == "2":
        estudante["idade"] = lerIdade()
        print("\nIdade alterada com sucesso.")

    elif opcao == "3":
        estudante["curso"] = lerCurso()
        print("\nCurso alterado com sucesso.")

    elif opcao == "4":
        novasNotas = lerNotas()

        estudante["notas"] = tuple(novasNotas)
        estudante["media"] = calcularMedia(novasNotas)
        estudante["situacao"] = calcularSituacao(estudante["media"])

        print("\nNotas alteradas com sucesso.")
        print(f"Nova média: {estudante['media']:.2f}")
        print(f"Nova situação: {estudante['situacao']}")

    elif opcao == "0":
        print("\nOperação cancelada.")

    else:
        print("\nOpção inválida.")

    pausar()


def removerEstudante(estudantes):
    limparTela()

    print("========================================")
    print("          REMOVER ESTUDANTE")
    print("========================================")

    if len(estudantes) == 0:
        print("\nNenhum estudante cadastrado")
        pausar()
        return

    nome = input("\nDigite o nome do estudante: ").strip()

    indice = encontrarEstudante(estudantes, nome)

    if indice == -1:
        print("\nEstudante não encontrado.")
        pausar()
        return

    estudantes.pop(indice)

    print("\nEstudante removido com sucesso.")

    pausar()



def gerarRelatorio(estudantes):
    limparTela()

    print("========================================")
    print("          RELATÓRIO DA TURMA")
    print("========================================")

    total = len(estudantes)

    if total == 0:
        print("\nNão há estudantes cadastrados.")
        pausar()
        return

    medias = []

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:
        media = estudante["media"]
        medias.append(media)

        if estudante["situacao"] == "Aprovado":
            aprovados += 1
        elif estudante["situacao"] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1

    maiorMedia = max(medias)
    menorMedia = min(medias)
    mediaGeral = sum(medias) / total

    print(f"\nEstudantes: {total}")
    print(f"Maior média: {maiorMedia:.2f}")
    print(f"Menor média: {menorMedia:.2f}")
    print(f"Média geral: {mediaGeral:.2f}")

    print("\nSITUAÇÃO ACADÊMICA")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")

    pausar()


def exibirMenu():
    print("========================================")
    print("          SISTEMA ACADÊMICO")
    print("========================================")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")
    print("========================================")


def executarSistema():
    estudantes = []

    while True:
        limparTela()
        exibirMenu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrarEstudante(estudantes)

        elif opcao == "2":
            listarEstudantes(estudantes)

        elif opcao == "3":
            consultarEstudante(estudantes)

        elif opcao == "4":
            alterarDados(estudantes)

        elif opcao == "5":
            removerEstudante(estudantes)

        elif opcao == "6":
            gerarRelatorio(estudantes)

        elif opcao == "0":
            limparTela()

            print("========================================")
            print("       SISTEMA ACADÊMICO ENCERRADO")
            print("========================================")
            print("Obrigado por utilizar o sistema!")

            break

        else:
            print("\nOpção inválida. Escolha uma opção do menu.")
            pausar()


if __name__ == "__main__":
    executarSistema()