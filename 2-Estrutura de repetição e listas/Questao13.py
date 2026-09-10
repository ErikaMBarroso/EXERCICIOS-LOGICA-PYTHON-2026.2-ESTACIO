# Agenda de contatos com funcionalidade de consulta

contatos = []

for c in range(1, 6):
    nome = input(f"Digite o nome do {c}° contato: ")
    telefone = input(f"Digite o número do contato {nome}: ")
    email = input(f"Digite o email do contato {nome}: ")

    novoContato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(novoContato)


contatoBuscado = input("Qual contato você deseja consultar?\n")

encontrado = False

for contato in contatos:
    if contato["nome"].lower() == contatoBuscado.lower():
        print(f"Nome: {contato['nome']}\nTelefone: {contato['telefone']}\nEmail: {contato['email']}")
        encontrado = True
        break


if not encontrado:
    print("Contato não encontrado.")
