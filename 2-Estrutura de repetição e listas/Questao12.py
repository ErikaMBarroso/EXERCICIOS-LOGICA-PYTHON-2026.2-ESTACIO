#  Cadastro e inventário de produtos em estoque

produtos = []

for p in range(1, 3):
    nome = input(f"Digite o nome do {p}° produto: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    qtdEstoque = int(input(f"Digite a quantidade em estoque de {nome}: "))

    novoProduto = {
        'nome': nome,
        'preco': preco,
        'qtdEstoque': qtdEstoque
    }
    produtos.append(novoProduto)


for p in range(len(produtos)):
    print("")
    print(f"PRODUTO {p + 1}")
    print(f"Produto: {produtos[p]['nome']}\nPreço unitário: R$ {produtos[p]['preco']:.2f}\nQuantidade em estoque: {produtos[p]['qtdEstoque']}")
    print("")


valorTotal = 0

for p in produtos:
    valorTotal += p["qtdEstoque"] * p["preco"]


maiorPreco = 0
produtoMaisCaro = None

for p in produtos:
    if p["preco"] > maiorPreco:
        maiorPreco = p["preco"]
        produtoMaisCaro = p


print(f"O valor total do estoque: R$ {valorTotal:.2f}")
print(f"O produto mais caro: {produtoMaisCaro['nome']}")
