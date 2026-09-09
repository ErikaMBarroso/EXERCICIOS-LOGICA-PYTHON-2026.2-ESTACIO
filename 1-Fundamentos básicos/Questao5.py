# Classificação etária com validação de entrada

idade = int(input("Digite sua idade: "))
while idade < 0:
    idade = int(input("Digite uma idade válida: "))

if idade <= 12:
    print("Você é classificado como criança")
elif idade < 18:
    print("Você é classificado como adolesccente")
elif idade < 60:
    print("Você é classificado como adulto")
else: 
    print("Você é classificado como idoso")