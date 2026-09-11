# Análise linguística completa de uma frase

frase = input("Digite uma frase: ")

palavras = frase.split()

quantidadeCaracteres = len(frase)
quantidadePalavras = len(palavras)

primeiraPalavra = palavras[0]
ultimaPalavra = palavras[-1]

letra = input("Digite uma letra para procurar: ")

quantidadeLetra = frase.lower().count(letra.lower())

print("\n")
print(f"Quantidade de caracteres: {quantidadeCaracteres}")
print(f"Quantidade de palavras: {quantidadePalavras}")
print(f"Primeira palavra: {primeiraPalavra}")
print(f"Última palavra: {ultimaPalavra}")
print(f"Quantidade de ocorrências de '{letra}': {quantidadeLetra}")
print(f"Frase em maiúsculas: {frase.upper()}")
print(f"Frase em minúsculas: {frase.lower()}")
