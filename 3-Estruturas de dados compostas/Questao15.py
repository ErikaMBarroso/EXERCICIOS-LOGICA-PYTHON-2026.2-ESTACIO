# Cadastro e análise populacional de cidades

def maiorMenor(cidades):
    cMaisPopulosa = cidades[0]
    cMenosPopulosa = cidades[0]

    for c in cidades:
        if c['habitantes'] > cMaisPopulosa['habitantes']:
            cMaisPopulosa = c
        if c['habitantes'] < cMenosPopulosa['habitantes']:
            cMenosPopulosa = c

    print(f"Cidade com maior população: {cMaisPopulosa['nome']}")
    print(f"Cidade com menor população: {cMenosPopulosa['nome']}")


def somaMedia(cidades):
    soma = 0

    for c in cidades:
        soma = soma + c['habitantes']

    media = soma / len(cidades)

    print(f"Soma das populações: {soma}")
    print(f"Média das populações: {media:.2f}")


cidades = []

for c in range(1, 3):
    nome = input(f"Digite o nome da {c} cidade: ")
    estado = input(f"Digite o nome do estado de {nome}: ")
    while len(estado) != 2:
        estado = input("Digite a sigla do estado: ")
    while True:
        habitantes_input = input(f"Digite a população de {nome}: ")
        try:
            habitantes_float = float(habitantes_input)
            habitantes = int(habitantes_float)
            break

        except ValueError:
            print("Digite um valor válido")

    novaCidade = {
        'nome': nome,
        'estado': estado,
        'habitantes': habitantes
    }
    cidades.append(novaCidade)

print("========================================")
maiorMenor(cidades)
somaMedia(cidades)
print("========================================")

for c in cidades:
    print(
        f"Nome: {c['nome']}\n"
        f"Estado: {c['estado']}\n"
        f"População: {c['habitantes']}\n"
        f"______________________________________"
    )